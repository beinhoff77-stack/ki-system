"""NF-S Probe 2 (Härtung, ZUSÄTZLICH zu tools/tests/aus/nf_s_probe.sql, die freigegebenen NF-S-Dateien bleiben unverändert):
  tools/tests/aus/nf_s_probe2.sql   rein lesend; endet IMMER mit „PROBELAUF2 bestanden, ALLES zurückgerollt …“ (oder „NF-S PROBE2 ABBRUCH …“)
Unterschied zur ersten Probe: funktioniert in JEDEM Zustand (alt, neu, gemischt) – die ALTEN Texte werden als temporäre Funktionen (pg_temp) angelegt und gegen die
LEBENDEN Funktionen verglichen (also auch, wenn NF-S schon eingespielt ist); Fehler werden getrennt gezählt und brechen ab; eine Abweichung ist nur erlaubt, wenn am konkreten
Lernziel (auswahl) bzw. an einem Pflicht-Lernziel des Kindes (stand) eine gesperrte Sicherungsaufgabe steht; bei nachtest_stand dürfen sich nur vorrat_runden und nachschub_noetig
ändern; Eigenschaften werden vollständig verglichen (Signatur, Rückgabetyp, Sprache, Volatilität, Definer, STRICT, search_path, Parallelität, Kosten, LEAKPROOF).
test_starten_intern wird nicht aufgerufen (VOLATILE, schreibt).
Aufruf: python3 -I tools/tests/nf_probe2.py [--pruefen]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nf_einspielen as NF  # noqa: E402

DATEI = NF.AUS / 'nf_s_probe2.sql'
EIG = 'proparallel u, procost 100, proleakproof f'


def paket():
    an, sn = NF.auswahl_alt(), NF.stand_alt()
    an2, sn2 = NF.auswahl_neu(), NF.stand_neu()
    assert '$function$' not in an + sn + an2 + sn2
    return f"""-- NF-S Probe 2 (rein lesend, rollt am Ende ALLES zurück). Zusatz zur ersten Probe; funktioniert in jedem Zustand (alt/neu/gemischt).
-- Die alten (Live-Stand) und die neuen Funktionstexte werden als temporäre Funktionen pg_temp.nf_alt_*/nf_neu_* angelegt: Wirkung = alt gegen neu; zusätzlich muss die lebende Funktion das Ergebnis ihres eigenen Zustands liefern:
-- Fehler getrennt zählen (Abbruch), Abweichung nur mit gesperrter Sicherungsaufgabe am konkreten Lernziel (auswahl) bzw. an einem Pflicht-Lernziel des Kindes (stand),
-- bei nachtest_stand nur in vorrat_runden/nachschub_noetig. Nur Zahlen im Bericht. md5 alt auswahl {NF.AUSWAHL_ALT_MD5}, stand {NF.STAND_ALT_MD5}, test_starten_intern {NF.TSI_ALT_MD5}.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $nf2$
declare v_a constant regprocedure := to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)');
  v_s constant regprocedure := to_regprocedure('schule.nachtest_stand(bigint, bigint)');
  v_t constant regprocedure := to_regprocedure('schule.test_starten_intern(bigint, jsonb)');
  eig_a constant text := '{NF.EIGENSCHAFTEN}|{EIG}'; eig_t constant text := '{NF.EIGENSCHAFTEN_TSI}|{EIG}';
  fehler text[] := '{{}}'; zst jsonb := '{{}}'; d text; e text; r record; va text; vb text; n_a int := 0; n_s int := 0; n_a_diff int := 0; n_s_diff int := 0; n_err int := 0; n_unerw int := 0;
  n_erlaubt int := 0; n_gesp int; fe text[] := '{{}}'; vc text; n_live int := 0;
begin
  if v_a is null or v_s is null or v_t is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.lernender') is null or to_regclass('schule.lernziel_stand') is null then
    raise exception 'NF-S PROBE2 ABBRUCH: Funktionen oder Tabellen fehlen'; end if;
  -- 1. Zustände und vollständige Eigenschaften
  for r in select x.n, x.o, x.alt, x.neu, x.soll from (values ('auswahl', v_a, '{NF.AUSWAHL_ALT_MD5}', '{NF.md5(NF.auswahl_neu())}', eig_a), ('stand', v_s, '{NF.STAND_ALT_MD5}', '{NF.md5(NF.stand_neu())}', eig_a),
                            ('test_starten_intern', v_t, '{NF.TSI_ALT_MD5}', '{NF.md5(NF.tsi_neu())}', eig_t)) x(n, o, alt, neu, soll) loop
    select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, ''), pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname,
           'proparallel ' || p.proparallel::text, 'procost ' || p.procost::text, 'proleakproof ' || (case when p.proleakproof then 't' else 'f' end)) into d, e
      from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    zst := zst || jsonb_build_object(r.n, case md5(d) when r.alt then 'alt' when r.neu then 'neu' else 'unbekannt' end);
    if md5(d) not in (r.alt, r.neu) then fehler := fehler || format('%s: Funktionstext weder alt noch neu (md5 %s)', r.n, md5(d)); end if;
    if e not like (case when r.n = 'test_starten_intern' then 'v|f|f|%' else 's|f|f|%' end) then fehler := fehler || format('%s: Volatilität/Definer/STRICT: %s', r.n, e); end if;
    if position('search_path=""' in replace(e, '\\"', '"')) = 0 then fehler := fehler || format('%s: search_path nicht leer: %s', r.n, e); end if;
    if position('proparallel u|procost 100|proleakproof f' in e) = 0 then fehler := fehler || format('%s: Parallelität/Kosten/LEAKPROOF abweichend: %s', r.n, e); end if;
  end loop;
  if position('p_l bigint, p_e bigint, p_lz text, p_anzahl integer|bigint[]|sql|' in (select concat_ws('|', pg_get_function_arguments(oid), prorettype::regtype::text, (select lanname from pg_language where oid = prolang), '') from pg_proc where oid = v_a)) = 0
     or position('p_lernender bigint, p_einheit bigint|jsonb|plpgsql|' in (select concat_ws('|', pg_get_function_arguments(oid), prorettype::regtype::text, (select lanname from pg_language where oid = prolang), '') from pg_proc where oid = v_s)) = 0
     or position('p_lernender bigint, p_daten jsonb|jsonb|plpgsql|' in (select concat_ws('|', pg_get_function_arguments(oid), prorettype::regtype::text, (select lanname from pg_language where oid = prolang), '') from pg_proc where oid = v_t)) = 0 then
    fehler := fehler || 'Argumente, Rückgabetyp oder Sprache einer der drei Funktionen weichen ab'::text; end if;
  if array_length(fehler, 1) > 0 then raise exception 'NF-S PROBE2 ABBRUCH (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;
  -- 2. Alte Texte als temporäre Funktionen (Live-Stand), nur in dieser Transaktion
  execute $a$
create function pg_temp.nf_alt_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
 returns bigint[] language sql stable set search_path to ''
as $function${an}$function$
$a$;
  execute $s$
create function pg_temp.nf_alt_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function${sn}$function$
$s$;
  execute $a$
create function pg_temp.nf_neu_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
 returns bigint[] language sql stable set search_path to ''
as $function${an2}$function$
$a$;
  execute $s$
create function pg_temp.nf_neu_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function${sn2}$function$
$s$;
  select count(*) into n_gesp from schule.aufgabe a where a.pool = 'sicherung' and not a.freigegeben;
  -- 3. nachtest_auswahl: alt (Kopie) gegen lebend, je Kind × Einheit/Lernziel × Menge; Fehler getrennt
  for r in select l.id l, g.e, g.lz, m.n, exists (select 1 from schule.aufgabe a where a.einheit_id = g.e and a.variante_gruppe is not distinct from g.lz and a.pool = 'sicherung' and not a.freigegeben) gesperrt
             from schule.lernender l cross join (select distinct a.einheit_id e, a.variante_gruppe lz from schule.aufgabe a where a.pool = 'sicherung') g cross join (values (1), (2), (3), (5)) m(n) loop
    n_a := n_a + 1; va := null; vb := null;
    begin va := pg_temp.nf_alt_auswahl(r.l, r.e, r.lz, r.n)::text; exception when others then n_err := n_err + 1; fe := fe || ('auswahl alt ' || sqlstate); end;
    begin vb := pg_temp.nf_neu_auswahl(r.l, r.e, r.lz, r.n)::text; exception when others then n_err := n_err + 1; fe := fe || ('auswahl neu ' || sqlstate); end;
    begin vc := schule.nachtest_auswahl(r.l, r.e, r.lz, r.n)::text; exception when others then n_err := n_err + 1; fe := fe || ('auswahl lebend ' || sqlstate); vc := null; end;
    if vc is distinct from (case zst->>'auswahl' when 'alt' then va else vb end) then n_live := n_live + 1; end if;
    if va is distinct from vb then
      n_a_diff := n_a_diff + 1;
      if r.gesperrt then n_erlaubt := n_erlaubt + 1; else n_unerw := n_unerw + 1; end if;
    end if;
  end loop;
  -- 4. nachtest_stand: je Kind × Einheit; nur vorrat_runden/nachschub_noetig dürfen abweichen, und nur mit gesperrter Sicherungsaufgabe an einem Pflicht-Lernziel des Kindes
  for r in select l.id l, en.id e, exists (select 1 from schule.aufgabe a join schule.lernziel_stand s on s.lernender_id = l.id and s.einheit_id = en.id and s.pflicht and s.lernziel = a.variante_gruppe
                                            where a.einheit_id = en.id and a.pool = 'sicherung' and not a.freigegeben) gesperrt
             from schule.lernender l cross join schule.einheit en loop
    n_s := n_s + 1; va := null; vb := null;
    begin va := pg_temp.nf_alt_stand(r.l, r.e)::text; exception when others then n_err := n_err + 1; fe := fe || ('stand alt ' || sqlstate); end;
    begin vb := pg_temp.nf_neu_stand(r.l, r.e)::text; exception when others then n_err := n_err + 1; fe := fe || ('stand neu ' || sqlstate); end;
    begin vc := schule.nachtest_stand(r.l, r.e)::text; exception when others then n_err := n_err + 1; fe := fe || ('stand lebend ' || sqlstate); vc := null; end;
    if vc is distinct from (case zst->>'stand' when 'alt' then va else vb end) then n_live := n_live + 1; end if;
    if va is distinct from vb then
      n_s_diff := n_s_diff + 1;
      if va is null or vb is null or (va::jsonb - 'vorrat_runden' - 'nachschub_noetig') is distinct from (vb::jsonb - 'vorrat_runden' - 'nachschub_noetig') or not r.gesperrt then
        n_unerw := n_unerw + 1; else n_erlaubt := n_erlaubt + 1; end if;
    end if;
  end loop;
  if n_err > 0 then raise exception 'NF-S PROBE2 ABBRUCH: % Aufrufe mit Fehler (getrennt gezählt, z. B. %)', n_err, array_to_string(fe[1:5], '; '); end if;
  if n_live > 0 then raise exception 'NF-S PROBE2 ABBRUCH: % lebende Aufrufe liefern nicht das Ergebnis ihres eigenen Zustands (alt/neu)', n_live; end if;
  if n_unerw > 0 then raise exception 'NF-S PROBE2 ABBRUCH: % Abweichungen ohne erlaubten Grund (kein gesperrtes Sicherungs-Lernziel bzw. andere Felder als vorrat_runden/nachschub_noetig)', n_unerw; end if;
  raise exception 'PROBELAUF2 bestanden, ALLES zurückgerollt (nichts geändert): %', jsonb_build_object('zustand', zst, 'verglichen_auswahl', n_a, 'verglichen_stand', n_s, 'abweichend_auswahl', n_a_diff,
    'abweichend_stand', n_s_diff, 'erlaubt_wegen_gesperrter_sicherungsaufgaben', n_erlaubt, 'unerwartet', n_unerw, 'lebend_abweichend_vom_eigenen_zustand', n_live, 'fehler', n_err, 'gesperrte_sicherungsaufgaben_live', n_gesp)::text;
end $nf2$;
"""


def main():
    t = paket()
    assert '\n\\' not in t
    if '--pruefen' in sys.argv:
        if not DATEI.exists() or DATEI.read_text(encoding='utf-8') != t: print('nicht auf dem Stand: nf_s_probe2.sql', file=sys.stderr); sys.exit(1)
        print('OK'); return
    DATEI.write_text(t, encoding='utf-8')
    print(f'| `tools/tests/aus/nf_s_probe2.sql` | {len(t.encode("utf-8"))} | `{NF.md5(t)}` |')


if __name__ == '__main__':
    main()
