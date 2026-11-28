#!/usr/bin/env python3
"""W1 – Einspiel-Paket „Verstehen in Tests“, Stufe 1 (inhalte/mathe-profi/vtest-1/plan.md), nach dem Muster tools/bestand_berichtigung1_sql.py.

Aufruf:  python3 -I tools/vtest_sql.py --runde 1a                -> Übersicht (prüft alles wie tools/vtest_pruefen.py, schreibt nichts)
         python3 -I tools/vtest_sql.py --runde 1a--sql           -> Einspiel-Paket (ein Aufruf, eine Transaktion) nach stdout
         python3 -I tools/vtest_sql.py --runde 1a--sql --probe   -> Probelauf: dieselben Prüfungen, am Ende absichtlich Fehler = ALLES zurückgerollt
         python3 -I tools/vtest_sql.py --runde 1a--pakete        -> schreibt tools/tests/aus/vtest<Runde>_{probe,einspielen}.sql, druckt Größe/md5
         (--pakete --pruefen: schreibt nichts, Rückgabe 1, wenn die Dateien nicht dem Stand entsprechen)
         Testumgebung: --auswahl/--ordner/--plan/--themen/--themenliste wie bei tools/vtest_pruefen.py
NICHT AUSFÜHREN ohne den ausdrücklichen Satz des Nutzers. Ändert nichts an App-Code, Lernständen oder Quelldateien.

Was ein Paket tut – je VERSTEHENS-LERNZIEL der Runde (eine „Gruppe“, wird nur ganz oder gar nicht geändert):
  1. die neue Verstehens-Test-Aufgabe und die neuen Korrektur- und Sicherungs-Aufgaben über schule.aufgaben_einfuegen einfügen (pool, typ, form, stufe,
     zaehlt = ja), Regel und Fehlbilder in schule.aufgabe_regel / aufgabe_fehlbild schreiben;
  2. die alte Test-Aufgabe dieses Lernziels sperren (freigegeben = false; dafür kurz Einheit 'geprueft' und zurück, wie die Bestands-Berichtigung) –
     erst NACHDEM die neue eingefügt und geprüft ist; nie bleibt eine Etappe ohne freigegebene Test-Aufgabe (Nachprüfung: genau eine, die neue).
  Platz (reihenfolge), bewusst gesetzt:
     test       max_r + 80000 + 1000·Block + Nr. der Gruppe in der Einheit (hinter allen Übungs-Runden-Blöcken 1000·R und vor der Berichtigung 90000):
                der Flugtest zeigt die Rechen-Aufgaben zuerst, die Verstehens-Aufgaben danach (Einstieg mit Gewohntem);
     korrektur, sicherung  −100000 + 1000·Block + laufende Nr. in der Einheit (NEGATIV = vor jedem Bestand): Korrektur (`order by reihenfolge limit 1`
                unter den ungesehenen) und Nachtest (`order by gestellt, zuletzt nulls first, reihenfolge`) ziehen bei diesem Lernziel zuerst die neuen
                Verstehens-Aufgaben, in der Reihenfolge der Datei; erst wenn sie verbraucht sind, wieder den Rechen-Bestand. Rechen-Lernziele bleiben unberührt.
Block = Feld „block“ der Runde in auswahl.json (1a = 1, 1b = 2, 2 = 3, 3 = 4; 1..9).
Zustände je Gruppe: neu (alte Test-Aufgabe = die einzige freigegebene des Lernziels, keine neue da) | fertig (alte gesperrt, alle neuen da und gleich dem Soll
in allen Feldern, Regel, Fehlbildern; genau eine freigegebene Test-Aufgabe = die neue) | zurueckgestellt (offener Verweis, Gruppe bleibt UNBERÜHRT) | sonst Abbruch.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import vtest_pruefen as P  # noqa: E402
import regelbezug_sql as R  # noqa: E402
import nf_einspielen as NF  # noqa: E402

AUS = WURZEL / 'tools/tests/aus'
BLOCK_TEST = 80000
BLOCK_VORN = -100000
TRIGGER_SOLL = ('einheit:einheit_schutz', 'aufgabe:aufgabe_schutz', 'aufgabe:aufgabe_bedingung_schutz', 'aufgabe_regel:aufgabe_regel_schutz', 'aufgabe_fehlbild:aufgabe_fehlbild_schutz')


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def daten(k):
    """Gruppen (je Verstehens-Lernziel) mit allem, was das SQL braucht. Bricht ab, wenn die Prüfung (W2) Fehler meldet."""
    fehler, _, je, ein = P.runde_pruefen(k)
    if fehler:
        raise SystemExit('ABBRUCH (Prüfung wie tools/vtest_pruefen.py):\n  ' + '\n  '.join(fehler[:60]) + (f'\n  … ({len(fehler)} Fehler)' if len(fehler) > 60 else ''))
    if not 1 <= k['block'] <= 9: raise SystemExit('block 1..9 (Platzschema)')
    gruppen = []
    for s in sorted(ein, key=lambda s: k['plan'][s]['id']):
        pe = k['plan'][s]
        e = pe['id']
        gi, j = 0, 0
        for l in pe['lz']:
            if l not in ein[s]['verstehen']: continue
            gi += 1
            alt = k['alt_test'][(s, l)]
            xs = je[(s, l)]
            items = []
            for pool in P.POOLS:
                for x in (x for x in xs if x['pool'] == pool):
                    row = P.zeile(x)
                    if pool == 'test': r = pe['max_r'] + BLOCK_TEST + 1000 * k['block'] + gi
                    else:
                        j += 1
                        if j >= 1000: raise SystemExit(f'{s}: mehr als 999 Korrektur-/Sicherungs-Aufgaben')
                        r = BLOCK_VORN + 1000 * k['block'] + j
                    row['r'] = r
                    fb, weg = R.fehlbilder(x, row)
                    assert not weg and len(fb) == len(x.get('fehlbilder') or []), (x['kennung'], weg)
                    items.append(dict(k=x['kennung'], pool=pool, row=row, nr=r, nf=row['f'], na=row.get('a'), regel=x.get('regel'), fb=fb))
            gruppen.append(dict(gk=f'{k["kuerzel"]}:{e}:{l}', e=e, s=s, l=l, af=alt['f'], aa=alt.get('a'), ao=alt['o'], items=items))
    return gruppen


def q(s):
    return 'null' if s is None else "'" + str(s).replace("'", "''") + "'"


def j(x):
    s = json.dumps(x, ensure_ascii=False)
    assert '$vtj$' not in s
    return f'$vtj${s}$vtj$::jsonb'


def jn(x):
    return 'null::jsonb' if x is None else j(x)


VERWEIS_TEXT = """    gef := '{}';
    if exists (select 1 from schule.misch_ausgabe m where m.aufgabe_id = @.alt_id and m.eingeloest_am is null and m.verfallen_am is null and m.ausgegeben_am > now() - interval '24 hours') then gef := gef || 'offene Mischkarte'::text; end if;
    if exists (select 1 from schule.testsitzung s where @.alt_id = any(s.aufgaben) and s.status is distinct from 'abgeschlossen' and s.abgeschlossen_am is null) then gef := gef || 'laufende Testsitzung mit der alten Test-Aufgabe'::text; end if;
    if exists (select 1 from schule.versuch v where v.aufgabe_id = @.alt_id and v.anlauf = 1 and not v.richtig and v.am > now() - interval '2 hours'
         and not exists (select 1 from schule.versuch w where w.lernender_id = v.lernender_id and w.aufgabe_id = v.aufgabe_id and w.am > v.am)) then gef := gef || 'falscher 1. Anlauf ohne zweiten Versuch'::text; end if;
    if exists (select 1 from schule.lernziel_stand s where s.einheit_id = @.e and s.lernziel = @.l and s.status = 'fehler') then gef := gef || 'offene Korrektur (Status fehler) – die Korrektur soll die Art der falschen (alten Rechen-)Aufgabe behalten'::text; end if;"""


def VERWEIS(var):
    return VERWEIS_TEXT.replace('@', var)


SOLL_VGL = """(neu.einheit_id, neu.freigegeben, neu.pool, neu.variante_gruppe, neu.antworttyp, neu.loesung, neu.reihenfolge, neu.frage, neu.antworten, neu.stufe, neu.typ, neu.form, neu.zaehlt,
          neu.teilfaehigkeit, neu.tipp, neu.loesungsweg, neu.expedition_id, neu.teil, neu.art, neu.punkte_max, neu.thema_id)
         is distinct from (@.e, true, @.pool, @.l, @.nrow->>'y', @.nrow->'o', @.nr, @.nf, @.na, (@.nrow->>'s')::smallint, @.nrow->>'g', @.nrow->>'form', @.nrow->>'zaehlt',
          @.nrow->>'t', @.nrow->>'h', @.nrow->>'w', null::bigint, null::text, case @.pool when 'test' then 'blocktest' else 'nachtest' end, 1, (select ei.thema_id from schule.einheit ei where ei.id = @.e))"""


def SOLL(var):
    return SOLL_VGL.replace('@', var)


FB_VGL = """(select r.regel from schule.aufgabe_regel r where r.aufgabe_id = neu.id) is distinct from @.regel
         or (select count(*) from schule.aufgabe_fehlbild x where x.aufgabe_id = neu.id) <> jsonb_array_length(@.fb)
         or exists (select 1 from jsonb_array_elements(@.fb) y where not exists (select 1 from schule.aufgabe_fehlbild x where x.aufgabe_id = neu.id and x.nr = (y->>'nr')::smallint
              and (x.art, x.luecke, x.wert, x.beschreibung, x.fehlbild, x.regel) is not distinct from (y->>'art', (y->>'luecke')::smallint, y->>'wert', y->>'text', y->>'fehlbild', y->>'regel')))"""


def paket(k, gruppen, probe=False):
    gw, nw = [], []
    for g in gruppen:
        gw.append(f"    ({q(g['gk'])}, {g['e']}, {q(g['l'])}, {j(g['af'])}, {jn(g['aa'])}, {j(g['ao'])}, {len(g['items'])})")
        for it in g['items']:
            nw.append(f"    ({q(it['k'])}, {q(g['gk'])}, {g['e']}, {q(g['l'])}, {q(it['pool'])}, {j(it['row'])}, {it['nr']}, {j(it['nf'])}, {jn(it['na'])}, {q(it['regel'])}, {j(it['fb'])})")
    n_g = len(gruppen)
    n_i = sum(len(g['items']) for g in gruppen)
    n_fb = sum(len(it['fb']) for g in gruppen for it in g['items'])
    n_rg = sum(1 for g in gruppen for it in g['items'] if it['regel'])
    ein = sorted({g['e'] for g in gruppen})
    kz = k['kuerzel']
    modus = 'PROBELAUF (rollt am Ende ALLES zurück)' if probe else 'Einspielen'
    ende = ("  raise exception '%', v_kurz || ' | PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt) | Einzelheiten: ' || v_bericht::text;\n" if probe
            else "  raise notice '%', v_kurz || ' | eingespielt | Einzelheiten: ' || v_bericht::text;\n")
    trg_soll = ', '.join(f"'{t}'" for t in TRIGGER_SOLL)
    return f"""-- {kz} „Verstehen in Tests“ Stufe 1 ({modus}): {n_g} Verstehens-Lernziele, {n_i} neue Aufgaben, {n_rg} Regeln, {n_fb} Fehlbilder, {len(ein)} Einheiten.
-- Erzeugt mit tools/vtest_sql.py aus {k['ordner'].relative_to(WURZEL).as_posix() if k['ordner'].is_relative_to(WURZEL) else k['ordner'].name}. NICHT ohne den Satz des Nutzers ausführen.
-- VORAUSSETZUNG: NF-S (nachtest_auswahl/nachtest_stand/test_starten_intern exakt in der neuen Fassung mit Freigabefilter) – sonst Abbruch.
-- LERNPAUSE: von vor dem Aufruf bis zu seinem Ende (Sekunden); Begründung und Zeitgrenzen: inhalte/mathe-profi/vtest-1/plan.md, Abschnitt Ausführung.
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT. Jede Abweichung = Abbruch, ALLES zurück. Wiederholbar: ein zweiter Lauf erkennt „fertig“ (voller Sollvergleich) und schreibt nichts.
-- Je Verstehens-Lernziel (Gruppe): neu | fertig | zurueckgestellt (offener Verweis: laufende Testsitzung mit der alten Test-Aufgabe, offene Mischkarte, falscher
-- 1. Anlauf ohne Folgeversuch, ODER ein Kind hat das Lernziel im Status 'fehler' (offene Korrektur) – die Gruppe bleibt UNBERÜHRT, später nachholen) | sonst Abbruch.
-- Ablauf: Erkennen -> Einheitszeilen sperren (FOR NO KEY UPDATE) -> Verweisprüfung 1 -> Vorher-Stand -> einfügen + Regel/Fehlbilder -> Antwortprobe
-- -> je Einheit: Test-Start-Sperre aller Kinder (pg_advisory_xact_lock wie test_starten_intern), Verweisprüfung 2 (neuer Verweis = Abbruch), Einheit 'geprueft',
-- alte Test-Aufgaben freigegeben = false, Einheit 'freigegeben' -> Nachprüfungen: je Gruppe genau EINE freigegebene Test-Aufgabe (die neue); Zahl freigegebener
-- Aufgaben je Einheit/Lernziel/Vorrat genau um das Soll verändert (test ±0, uebung/bonus ±0); die neuen Korrektur-/Sicherungs-Aufgaben stehen in der Zugreihenfolge
-- (reihenfolge, id) VOR allen übrigen dieses Lernziels; Lernkarten-Regeln (karte_ziel/typen/schwer/anwenden) gleich; Trigger-Satz gleich (feste Soll-Liste, Mengenvergleich);
-- Fingerabdruck der unberührten Zeilen von aufgabe/einheit/aufgabe_regel/aufgabe_fehlbild gleich; in keiner anderen Tabelle des Schemas schule eine von dieser
-- Transaktion geschriebene Zeile (xmin) – Lernstände der Kinder werden nie verändert. GRENZEN wie in der Bestands-Berichtigung (xmin sieht keine Löschungen,
-- Sequenzen, externe Effekte; Trigger-Textsuche sieht delegierte Schreibvorgänge nicht; versuch/karte_stand ohne Fingerabdruck wegen laufender Aktivität).
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
do $vt$
declare z record; z2 record; alt schule.aufgabe; neu schule.aufgabe; fehler text[] := '{{}}'; zurueck text[] := '{{}}'; gef text[] := '{{}}';
  n_alt int; n_neu int; n_frei int; cnt bigint; id1 bigint; f jsonb; v jsonb; b jsonb; v_vor jsonb; v_nach jsonb; xid_ xid := pg_current_xact_id()::xid;
  n_grp_neu int := 0; n_grp_fertig int := 0; n_ins int := 0; n_gesperrt int := 0; n_regel_neu int := 0; n_fb_neu int := 0; n_soll_ok int := 0; n_fb_ok int := 0;
  tr record; kk record; trg text; trg_vor text; trg_nach text; wert text; fn text; fp_vor text[]; fp_nach text[]; erw jsonb; audit jsonb := '{{}}'; tab text;
  v_bericht jsonb; v_kurz text;
begin
  -- 0. Voraussetzungen (RB-S, FT-S, NF-S, Karten-Funktionen, Tabellen, keine Prüfbedingung auf reihenfolge)
  if to_regclass('schule.aufgabe_fehlbild') is null or to_regclass('schule.aufgabe_regel') is null
     or to_regprocedure('schule.fehlbild_finden(schule.aufgabe, jsonb)') is null or to_regprocedure('schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)') is null
     or to_regprocedure('schule.aufgaben_einfuegen(bigint, jsonb)') is null or to_regprocedure('schule.antwort_bewerten(schule.aufgabe, jsonb)') is null then
    raise exception '{kz} ABBRUCH: erst RB-S und FT-S einspielen'; end if;
  if (select count(*) from pg_attribute where attrelid = 'schule.aufgabe'::regclass and attname in ('form', 'zaehlt', 'freigegeben', 'typ', 'expedition_id', 'teil') and not attisdropped) <> 6
     or position('x->>''form''' in pg_get_functiondef('schule.aufgaben_einfuegen(bigint, jsonb)'::regprocedure)) = 0 then
    raise exception '{kz} ABBRUCH: erst FT-S einspielen (Spalten form/zaehlt, aufgaben_einfuegen)'; end if;
  if to_regclass('schule.misch_ausgabe') is null or to_regclass('schule.testsitzung') is null or to_regclass('schule.versuch') is null
     or to_regclass('schule.lernziel_stand') is null or to_regclass('schule.lernender') is null then
    raise exception '{kz} ABBRUCH: Tabellen misch_ausgabe/testsitzung/versuch/lernziel_stand/lernender fehlen (Verweisprüfung nicht möglich)'; end if;
  foreach fn in array array['karte_ziel', 'karte_typen_noetig', 'karte_schwer_noetig', 'karte_anwenden_noetig'] loop
    if to_regprocedure('schule.' || fn || '(bigint, text)') is null then raise exception '{kz} ABBRUCH: schule.%(bigint, text) fehlt', fn; end if;
  end loop;
  if to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)') is null or to_regprocedure('schule.nachtest_stand(bigint, bigint)') is null
     or to_regprocedure('schule.test_starten_intern(bigint, jsonb)') is null
     or md5((select prosrc from pg_proc where oid = to_regprocedure('schule.test_starten_intern(bigint, jsonb)'))) is distinct from '{NF.md5(NF.tsi_neu())}'
     or md5((select prosrc from pg_proc where oid = to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)'))) is distinct from '{NF.md5(NF.auswahl_neu())}'
     or md5((select prosrc from pg_proc where oid = to_regprocedure('schule.nachtest_stand(bigint, bigint)'))) is distinct from '{NF.md5(NF.stand_neu())}' then
    raise exception '{kz} ABBRUCH: erst NF-S einspielen (nachtest_auswahl, nachtest_stand und test_starten_intern müssen exakt die neue Fassung mit Freigabefilter haben)'; end if;
  if exists (select 1 from pg_constraint c where c.conrelid = 'schule.aufgabe'::regclass and c.contype = 'c' and pg_get_constraintdef(c.oid) ~ 'reihenfolge') then
    raise exception '{kz} ABBRUCH: eine Prüfbedingung auf schule.aufgabe.reihenfolge (z. B. > 0) – die negativen Plätze der Korrektur-/Sicherungs-Aufgaben sind dann nicht möglich (plan.md)'; end if;
  create temp table vt_g on commit drop as
    select x.*, null::bigint alt_id, null::text zustand, null::text grund_zurueck from (values
{(',' + chr(10)).join(gw)}
  ) x(gk, e, l, af, aa, ao, n_soll);
  create temp table vt_n on commit drop as
    select x.*, null::bigint neu_id from (values
{(',' + chr(10)).join(nw)}
  ) x(k, gk, e, l, pool, nrow, nr, nf, na, regel, fb);
  -- 1. Erkennen und Zustand je Gruppe
  for z in select * from vt_g order by gk collate "C" loop
    if (select ei.status from schule.einheit ei where ei.id = z.e) is distinct from 'freigegeben' then
      fehler := fehler || format('%s: Einheit %s ist nicht freigegeben (oder fehlt)', z.gk, z.e); continue; end if;
    select count(*), min(x.id) into n_alt, id1 from schule.aufgabe x
     where x.einheit_id = z.e and x.pool = 'test' and x.variante_gruppe is not distinct from z.l
       and x.frage is not distinct from z.af and x.antworten is not distinct from z.aa and x.loesung is not distinct from z.ao;
    if n_alt <> 1 then fehler := fehler || format('%s: alte Test-Aufgabe %s-mal gefunden (erwartet genau 1; Lernkarte, Frage, Antworten, Lösung wie inhalte/themen)', z.gk, n_alt); continue; end if;
    update vt_g set alt_id = id1 where gk = z.gk;
    select * into alt from schule.aufgabe where id = id1;
    select count(*) into n_neu from vt_n n where n.gk = z.gk and exists (select 1 from schule.aufgabe x where x.einheit_id = n.e and x.frage is not distinct from n.nf and x.antworten is not distinct from n.na);
    select count(*), min(x.id) into n_frei, id1 from schule.aufgabe x where x.einheit_id = z.e and x.pool = 'test' and x.variante_gruppe is not distinct from z.l and x.freigegeben;
    if n_neu = 0 then
      if alt.freigegeben is distinct from true then fehler := fehler || format('%s: alte Test-Aufgabe %s ist schon gesperrt, die neuen fehlen (Etappe ohne Test-Aufgabe?)', z.gk, alt.id); continue; end if;
      if n_frei <> 1 then fehler := fehler || format('%s: das Lernziel hat %s freigegebene Test-Aufgaben (erwartet genau die alte)', z.gk, n_frei); continue; end if;
      if exists (select 1 from schule.aufgabe x join vt_n n on n.gk = z.gk and x.einheit_id = n.e and x.reihenfolge = n.nr) then
        fehler := fehler || format('%s: ein Platz (reihenfolge) des Pakets ist in Einheit %s schon belegt', z.gk, z.e); continue; end if;
      update vt_g set zustand = 'neu' where gk = z.gk;
    elsif n_neu = z.n_soll then
      if alt.freigegeben is distinct from false then fehler := fehler || format('%s: alte (%s) und neue Aufgaben sind gleichzeitig gültig – Zwischenstand, nicht von diesem Paket', z.gk, alt.id); continue; end if;
      for z2 in select * from vt_n where gk = z.gk order by nr loop
        select count(*) into cnt from schule.aufgabe x where x.einheit_id = z2.e and x.frage is not distinct from z2.nf and x.antworten is not distinct from z2.na;
        select * into neu from schule.aufgabe x where x.einheit_id = z2.e and x.frage is not distinct from z2.nf and x.antworten is not distinct from z2.na order by x.id limit 1;
        if cnt <> 1 or {SOLL('z2')} then
          fehler := fehler || format('%s: neue Aufgabe %s steht schon da, weicht aber vom Soll ab (alle Felder nullsicher verglichen)', z2.k, neu.id); continue; end if;
        if {FB_VGL.replace('@', 'z2')} then
          fehler := fehler || format('%s: neue Aufgabe %s hat andere Regel/Fehlbilder als das Soll', z2.k, neu.id); continue; end if;
        update vt_n set neu_id = neu.id where k = z2.k;
      end loop;
      if n_frei <> 1 or id1 is distinct from (select neu_id from vt_n where gk = z.gk and pool = 'test') then
        fehler := fehler || format('%s: nach dem Einspielen muss genau EINE freigegebene Test-Aufgabe da sein (die neue), gefunden %s', z.gk, n_frei); continue; end if;
      update vt_g set zustand = 'fertig' where gk = z.gk;
    else
      fehler := fehler || format('%s: %s von %s neuen Aufgaben stehen schon da – Zwischenstand, nicht von diesem Paket', z.gk, n_neu, z.n_soll);
    end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception '{kz} ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 1b. Einheitszeilen der zu ändernden Gruppen sperren (FOR NO KEY UPDATE: Fremdschlüssel-Einfügungen der Kinder werden nicht blockiert); erst danach die Verweisprüfung
  perform 1 from schule.einheit where id in (select e from vt_g where zustand = 'neu') order by id for no key update;
  -- 2. Verweisprüfung 1 -> Gruppe zurückstellen (bleibt unberührt)
  for z in select * from vt_g where zustand = 'neu' order by gk collate "C" loop
{VERWEIS('z')}
    if array_length(gef, 1) > 0 then
      update vt_g set zustand = 'zurueckgestellt', grund_zurueck = array_to_string(gef, ', ') where gk = z.gk;
      zurueck := zurueck || (z.gk || ' (alte Aufgabe ' || z.alt_id || '): ' || array_to_string(gef, ', '));
    end if;
  end loop;
  select count(*) into n_grp_neu from vt_g where zustand = 'neu';
  select count(*) into n_grp_fertig from vt_g where zustand = 'fertig';
  -- 3. Vorher-Stand
  create temp table vt_e on commit drop as select distinct e id from vt_g where zustand = 'neu';
  create temp table vt_c on commit drop as select x.einheit_id e, x.variante_gruppe l, x.pool, count(*) filter (where x.freigegeben) vor, null::bigint nach
    from schule.aufgabe x where x.einheit_id in (select id from vt_e) group by 1, 2, 3;
  create temp table vt_k on commit drop as select distinct e, l, null::text karte_vor, null::text karte_nach from vt_g where zustand = 'neu';
  for kk in select * from vt_k loop
    wert := '';
    foreach fn in array array['karte_ziel', 'karte_typen_noetig', 'karte_schwer_noetig', 'karte_anwenden_noetig'] loop
      execute format('select coalesce(schule.%I($1, $2)::text, ''-'')', fn) into trg using kk.e, kk.l; wert := wert || fn || '=' || trg || ';';
    end loop;
    update vt_k set karte_vor = wert where e = kk.e and l = kk.l;
  end loop;
  select coalesce(string_agg(cl.relname || ':' || g.tgname || ':' || md5(pg_get_triggerdef(g.oid)) || ':' || md5(p.prosrc), ',' order by cl.relname collate "C", g.tgname collate "C"), '') into trg_vor
    from pg_trigger g join pg_class cl on cl.oid = g.tgrelid join pg_proc p on p.oid = g.tgfoid
   where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild');
  for tr in select cl.relname, tg.tgname, p.proname, p.prosrc from pg_trigger tg join pg_class cl on cl.oid = tg.tgrelid join pg_proc p on p.oid = tg.tgfoid
            where not tg.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild') loop
    if tr.prosrc ~* '(insert\\s+into|delete\\s+from|update\\s+[a-z_.]+\\s+set|pg_notify|net\\.http|http_|dblink|truncate)' then
      fehler := fehler || format('Trigger %s.%s (Funktion %s) schreibt oder meldet vielleicht – von Hand prüfen', tr.relname, tr.tgname, tr.proname); end if;
  end loop;
  -- FESTE Soll-Liste der Schutz-Trigger (Tabelle:Name), Mengenvergleich in beide Richtungen, Vergleich byteweise (collate "C")
  if exists (select 1 from (select (cl.relname || ':' || g.tgname) collate "C" as n from pg_trigger g join pg_class cl on cl.oid = g.tgrelid
                             where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild')) ist
              full join (select unnest(array[{trg_soll}]) collate "C" as n) soll on ist.n = soll.n where ist.n is null or soll.n is null) then
    fehler := fehler || format('Trigger auf einheit/aufgabe/aufgabe_regel/aufgabe_fehlbild weichen von der festen Soll-Liste ab (erwartet {", ".join(TRIGGER_SOLL)}); gefunden: %s',
      coalesce((select string_agg(cl.relname || ':' || g.tgname, ', ' order by cl.relname collate "C", g.tgname collate "C") from pg_trigger g join pg_class cl on cl.oid = g.tgrelid
       where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild')), '(keine)')); end if;
  if array_length(fehler, 1) > 0 then raise exception '{kz} ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  create temp table vt_a on commit drop as select x.id, to_jsonb(x) - 'freigegeben' vor, null::jsonb nach from schule.aufgabe x where x.id in (select alt_id from vt_g where zustand = 'neu');
  fp_vor := array[(select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.aufgabe x where x.id not in (select alt_id from vt_g where zustand = 'neu')),
                  (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.einheit x where x.id not in (select id from vt_e)),
                  (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id), '')) from schule.aufgabe_regel x),
                  (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id, x.nr), '')) from schule.aufgabe_fehlbild x)];
  -- 4. Neue Aufgaben einfügen (je Aufgabe einzeln: genau 1), Werte prüfen, Regel und Fehlbilder schreiben
  for z2 in select n.* from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu' order by n.gk collate "C", n.nr loop
    cnt := schule.aufgaben_einfuegen(z2.e, jsonb_build_array(z2.nrow));
    if cnt <> 1 then fehler := fehler || format('%s: %s statt 1 Aufgabe eingefügt (gleiche Frage/Antworten schon in der Einheit?)', z2.k, cnt); continue; end if;
    select * into neu from schule.aufgabe x where x.einheit_id = z2.e and x.frage is not distinct from z2.nf and x.antworten is not distinct from z2.na;
    update vt_n set neu_id = neu.id where k = z2.k;
    n_ins := n_ins + 1;
    if neu.id is null or {SOLL('z2')} then
      fehler := fehler || format('%s: eingefügte Aufgabe %s hat nicht die Werte des Pakets', z2.k, neu.id); continue; end if;
    if z2.regel is not null then
      insert into schule.aufgabe_regel (aufgabe_id, regel) values (neu.id, z2.regel) on conflict do nothing;
      get diagnostics cnt = row_count; n_regel_neu := n_regel_neu + cnt;
    end if;
    for f in select * from jsonb_array_elements(z2.fb) loop
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, luecke, wert, beschreibung, fehlbild, regel)
      values (neu.id, (f->>'nr')::smallint, f->>'art', (f->>'luecke')::smallint, f->>'wert', f->>'text', f->>'fehlbild', f->>'regel') on conflict do nothing;
      get diagnostics cnt = row_count; n_fb_neu := n_fb_neu + cnt;
    end loop;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception '{kz} ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 4b. Antwortprobe (neu UND fertig): Soll-Antwort richtig, jede Fehlantwort gültig, falsch und als genau dieses Fehlbild erkannt
  for z2 in select n.* from vt_n n join vt_g g on g.gk = n.gk where g.zustand in ('neu', 'fertig') order by n.gk collate "C", n.nr loop
    select * into neu from schule.aufgabe where id = z2.neu_id;
    v := case z2.nrow->>'y' when 'zahl' then jsonb_build_object('wert', replace(z2.nrow->'o'->>'wert', '.', ',')) when 'luecken' then jsonb_build_object('werte', z2.nrow->'o'->'werte')
                  when 'auswahl' then jsonb_build_object('index', z2.nrow->'o'->'index') end;
    b := schule.antwort_bewerten(neu, v);
    if coalesce((b->>'format_ok')::boolean, false) and coalesce((b->>'richtig')::boolean, false) then n_soll_ok := n_soll_ok + 1;
    else fehler := fehler || format('%s: die Soll-Antwort %s wird nicht als richtig bewertet (%s)', z2.k, v, b); end if;
    for f in select * from jsonb_array_elements(z2.fb) loop
      v := schule.fehlbild_probeantwort(neu, f->>'art', (f->>'luecke')::int, f->>'wert');
      b := schule.antwort_bewerten(neu, v);
      if not coalesce((b->>'format_ok')::boolean, false) or coalesce((b->>'richtig')::boolean, true) then
        fehler := fehler || format('%s: Fehlbild %s – Antwort %s wird nicht als gültig und falsch bewertet (%s)', z2.k, f->>'nr', v, b); continue; end if;
      if schule.fehlbild_finden(neu, v) is distinct from (f->>'nr')::smallint then fehler := fehler || format('%s: Fehlbild %s wird an der Antwort %s nicht wiedererkannt', z2.k, f->>'nr', v); continue; end if;
      n_fb_ok := n_fb_ok + 1;
    end loop;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception '{kz} ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 5. Alte Test-Aufgaben sperren (je Einheit: Test-Start-Sperre, Verweisprüfung 2, kurz 'geprueft', freigegeben = false, zurück 'freigegeben'; Einheitszeile danach gleich)
  perform pg_advisory_xact_lock(hashtext('schule_test'), x.id::int) from (select l.id from schule.lernender l order by l.id) x;
  for tr in select id from vt_e order by id loop
    perform 1 from schule.einheit where id = tr.id for no key update;
    for z in select * from vt_g where zustand = 'neu' and e = tr.id order by gk collate "C" loop
{VERWEIS('z')}
      if array_length(gef, 1) > 0 then
        raise exception '{kz} ABBRUCH, alles zurückgerollt: % hat nach der ersten Prüfung einen offenen Verweis bekommen (alte Aufgabe %: %) – Lernpause einhalten und nochmals ausführen', z.gk, z.alt_id, array_to_string(gef, ', ');
      end if;
    end loop;
    select to_jsonb(x) into v_vor from schule.einheit x where x.id = tr.id;
    if v_vor->>'status' is distinct from 'freigegeben' then fehler := fehler || format('Einheit %s ist nicht freigegeben', tr.id); continue; end if;
    update schule.einheit set status = 'geprueft' where id = tr.id;
    update schule.aufgabe set freigegeben = false where id in (select alt_id from vt_g where zustand = 'neu' and e = tr.id) and freigegeben;
    get diagnostics cnt = row_count;
    n_gesperrt := n_gesperrt + cnt;
    if cnt <> (select count(*) from vt_g where zustand = 'neu' and e = tr.id) then fehler := fehler || format('Einheit %s: %s statt %s alte Test-Aufgaben gesperrt', tr.id, cnt, (select count(*) from vt_g where zustand = 'neu' and e = tr.id)); end if;
    update schule.einheit set status = 'freigegeben' where id = tr.id;
    select to_jsonb(x) into v_nach from schule.einheit x where x.id = tr.id;
    if v_nach is distinct from v_vor then fehler := fehler || format('Einheit %s hat sich durch den Statuswechsel verändert (Nebenwirkung): vorher %s, nachher %s', tr.id, left(v_vor::text, 300), left(v_nach::text, 300)); end if;
  end loop;
  update vt_a set nach = (select to_jsonb(x) - 'freigegeben' from schule.aufgabe x where x.id = vt_a.id);
  if exists (select 1 from vt_a x where x.nach is distinct from x.vor) or exists (select 1 from schule.aufgabe x where x.id in (select id from vt_a) and x.freigegeben is distinct from false) then
    fehler := fehler || 'eine alte Test-Aufgabe ist nicht gesperrt oder hat sich in einer anderen Spalte als freigegeben verändert'::text; end if;
  if array_length(fehler, 1) > 0 then raise exception '{kz} ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 6. Nachprüfungen
  -- 6a. je Gruppe (neu und fertig): genau eine freigegebene Test-Aufgabe, die neue
  for z in select * from vt_g where zustand in ('neu', 'fertig') loop
    select count(*), min(x.id) into n_frei, id1 from schule.aufgabe x where x.einheit_id = z.e and x.pool = 'test' and x.variante_gruppe is not distinct from z.l and x.freigegeben;
    if n_frei <> 1 or id1 is distinct from (select neu_id from vt_n where gk = z.gk and pool = 'test') then
      fehler := fehler || format('%s: %s freigegebene Test-Aufgaben nach dem Paket (Soll: genau die neue)', z.gk, n_frei); end if;
    -- 6b. Zugreihenfolge: die neuen Korrektur-/Sicherungs-Aufgaben stehen vor allen übrigen freigegebenen dieses Lernziels
    for tab in select unnest(array['korrektur', 'sicherung']) loop
      if (select coalesce(array_agg(x.id order by x.reihenfolge, x.id), '{{}}') from (select a.id, a.reihenfolge from schule.aufgabe a where a.einheit_id = z.e and a.pool = tab
            and a.variante_gruppe is not distinct from z.l and a.freigegeben order by a.reihenfolge, a.id limit (select count(*) from vt_n where gk = z.gk and pool = tab)) x)
         is distinct from (select coalesce(array_agg(n.neu_id order by n.nr), '{{}}') from vt_n n where n.gk = z.gk and n.pool = tab) then
        fehler := fehler || format('%s: die neuen %s-Aufgaben stehen nicht vorn in der Zugreihenfolge (reihenfolge, id)', z.gk, tab); end if;
    end loop;
  end loop;
  -- 6c. Zahl freigegebener Aufgaben je Einheit/Lernziel/Vorrat: genau um das Soll verändert
  insert into vt_c (e, l, pool, vor) select distinct n.e, n.l, n.pool, 0 from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu'
    and not exists (select 1 from vt_c c where c.e = n.e and c.l is not distinct from n.l and c.pool = n.pool);
  update vt_c c set nach = (select count(*) from schule.aufgabe x where x.einheit_id = c.e and x.variante_gruppe is not distinct from c.l and x.pool = c.pool and x.freigegeben);
  if exists (select 1 from vt_c c where c.nach - c.vor is distinct from (select count(*) from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu' and n.e = c.e
               and n.l is not distinct from c.l and n.pool = c.pool and n.pool <> 'test')) then
    fehler := fehler || ('Zahl freigegebener Aufgaben weicht vom Soll ab: ' || (select string_agg(format('%s/%s/%s %s -> %s', e, l, pool, vor, nach), '; ') from vt_c c
      where c.nach - c.vor is distinct from (select count(*) from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu' and n.e = c.e and n.l is not distinct from c.l and n.pool = c.pool and n.pool <> 'test'))); end if;
  -- 6d. Lernkarten-Regeln, Trigger, Fingerabdruck, Schreib-Prüfung über das ganze Schema
  for kk in select * from vt_k loop
    wert := '';
    foreach fn in array array['karte_ziel', 'karte_typen_noetig', 'karte_schwer_noetig', 'karte_anwenden_noetig'] loop
      execute format('select coalesce(schule.%I($1, $2)::text, ''-'')', fn) into trg using kk.e, kk.l; wert := wert || fn || '=' || trg || ';';
    end loop;
    update vt_k set karte_nach = wert where e = kk.e and l = kk.l;
  end loop;
  if exists (select 1 from vt_k where karte_vor is distinct from karte_nach) then
    fehler := fehler || ('Lernkarten-Regeln ändern sich: ' || (select string_agg(format('%s/%s: %s -> %s', e, l, karte_vor, karte_nach), ' | ') from vt_k where karte_vor is distinct from karte_nach)); end if;
  select coalesce(string_agg(cl.relname || ':' || g.tgname || ':' || md5(pg_get_triggerdef(g.oid)) || ':' || md5(p.prosrc), ',' order by cl.relname collate "C", g.tgname collate "C"), '') into trg_nach
    from pg_trigger g join pg_class cl on cl.oid = g.tgrelid join pg_proc p on p.oid = g.tgfoid
   where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild');
  if trg_vor is distinct from trg_nach then fehler := fehler || 'der Trigger-Satz hat sich während des Pakets verändert'::text; end if;
  fp_nach := array[(select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.aufgabe x where x.id not in (select alt_id from vt_g where zustand = 'neu')
                      and x.id not in (select n.neu_id from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu')),
                   (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.einheit x where x.id not in (select id from vt_e)),
                   (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id), '')) from schule.aufgabe_regel x where x.aufgabe_id not in (select n.neu_id from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu')),
                   (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id, x.nr), '')) from schule.aufgabe_fehlbild x where x.aufgabe_id not in (select n.neu_id from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu'))];
  if fp_vor is distinct from fp_nach then fehler := fehler || 'Fingerabdruck der unberührten Zeilen (aufgabe, einheit, aufgabe_regel, aufgabe_fehlbild) hat sich geändert (fremde Änderung oder Nebenwirkung)'::text; end if;
  erw := jsonb_build_object('aufgabe', n_ins + n_gesperrt, 'aufgabe_regel', n_regel_neu, 'aufgabe_fehlbild', n_fb_neu, 'einheit', (select count(*) from vt_e));
  for tab in select cl.relname from pg_class cl where cl.relnamespace = 'schule'::regnamespace and cl.relkind = 'r' order by 1 loop
    execute format('select count(*) from schule.%I where xmin = $1', tab) into cnt using xid_;
    if cnt > 0 or erw ? tab then audit := audit || jsonb_build_object(tab, cnt); end if;
    if cnt <> coalesce((erw->>tab)::int, 0) then fehler := fehler || format('Tabelle schule.%s: %s von diesem Paket geschriebene Zeilen, erwartet %s (Nebenwirkung?)', tab, cnt, coalesce((erw->>tab)::int, 0)); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception '{kz} ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  v_kurz := format('{kz} BERICHT: Lernziele %s (neu %s, schon fertig %s, zurückgestellt %s) | Aufgaben neu %s (test %s, korrektur %s, sicherung %s) | alte Test-Aufgaben gesperrt %s | Regeln %s, Fehlbilder %s | Einheiten geändert %s',
    (select count(*) from vt_g), n_grp_neu, n_grp_fertig, coalesce(array_length(zurueck, 1), 0), n_ins,
    (select count(*) from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu' and n.pool = 'test'),
    (select count(*) from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu' and n.pool = 'korrektur'),
    (select count(*) from vt_n n join vt_g g on g.gk = n.gk where g.zustand = 'neu' and n.pool = 'sicherung'),
    n_gesperrt, n_regel_neu, n_fb_neu, (select count(*) from vt_e));
  v_bericht := jsonb_build_object('lernziele', (select count(*) from vt_g), 'neu', n_grp_neu, 'fertig', n_grp_fertig, 'zurueckgestellt', to_jsonb(zurueck),
    'aufgaben_neu', n_ins, 'alte_gesperrt', n_gesperrt, 'regeln_neu', n_regel_neu, 'fehlbilder_neu', n_fb_neu, 'einheiten_geaendert', (select count(*) from vt_e),
    'sollantworten_richtig', n_soll_ok, 'fehlantworten_gueltig_und_falsch', n_fb_ok, 'je_lernziel_genau_eine_test_aufgabe', true, 'neue_vorn_in_der_zugreihenfolge', true,
    'lernkarten_regeln_gleich', true, 'fingerabdruck_unberuehrter_zeilen_gleich', true, 'nf_s_vorhanden', true, 'trigger', trg_nach, 'schreibzeilen_je_tabelle', audit, 'fehler', 0);
{ende}end $vt$;
select einheit_id, pool, count(*) filter (where freigegeben) as freigegeben, count(*) filter (where not freigegeben) as gesperrt from schule.aufgabe
 where einheit_id in ({', '.join(map(str, ein)) or 'null'}) and pool in ('test', 'korrektur', 'sicherung') group by 1, 2 order by 1, 2;
"""


def pakete(k, gruppen):
    n = f'vtest{k["runde"]}'
    return [(f'{n}_probe.sql', paket(k, gruppen, True)), (f'{n}_einspielen.sql', paket(k, gruppen, False))]


def uebersicht(gruppen):
    print(f'{len(gruppen)} Verstehens-Lernziele, {sum(len(g["items"]) for g in gruppen)} Aufgaben, {sum(len(i["fb"]) for g in gruppen for i in g["items"])} Fehlbilder')
    for g in gruppen:
        print(f'  {g["gk"]:34} ' + '  '.join(f'{i["k"]}:{i["pool"][:4]}@{i["nr"]}' for i in g['items']))


def main():
    argv = sys.argv[1:]
    k = P.kontext(**P.optionen(argv))
    gruppen = daten(k)
    if not gruppen: raise SystemExit('ABBRUCH: keine Gruppe')
    if '--sql' in argv:
        print(paket(k, gruppen, '--probe' in argv), end=''); return
    if '--pakete' in argv:
        out = pakete(k, gruppen)
        for nm, t in out:
            assert len(t.encode('utf-8')) < 3_000_000 and not re.search(r'^\s*\\', t, re.M) and not re.search(r'^\s*(begin|commit|rollback)\s*;', t, re.M | re.I), nm
        if '--pruefen' in argv:
            alt = [nm for nm, t in out if not (AUS / nm).exists() or (AUS / nm).read_text(encoding='utf-8') != t]
            if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
            print('OK'); return
        print('| Datei | Bytes | md5 |\n|---|---|---|')
        for nm, t in out:
            (AUS / nm).write_text(t, encoding='utf-8')
            print(f'| `tools/tests/aus/{nm}` | {len(t.encode("utf-8"))} | `{md5(t)}` |')
        return
    uebersicht(gruppen)


if __name__ == '__main__':
    main()
