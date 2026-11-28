#!/usr/bin/env python3
"""Einspiel-Paket für Bestands-Berichtigung 1 (23 berichtigte Aufgaben, inhalte/mathe-profi/bestand-berichtigung-1/vorschlag.json).

Aufruf:  python3 -I tools/bestand_berichtigung1_sql.py                -> Übersicht (Zuordnung BB1-… -> endgültige Kennung, Zählungen), schreibt nichts
         python3 -I tools/bestand_berichtigung1_sql.py --sql          -> Einspiel-Paket (ein Aufruf, eine Transaktion) nach stdout
         python3 -I tools/bestand_berichtigung1_sql.py --sql --probe  -> Probelauf: dieselben Prüfungen, am Ende absichtlich Fehler = ALLES zurückgerollt
         python3 -I tools/bestand_berichtigung1_sql.py --abbildung    -> abbildung.json (BB1-… -> Kennung, Einheit, Platz, Vorgänger) nach stdout
         python3 -I tools/bestand_berichtigung1_sql.py --pakete       -> schreibt tools/tests/aus/bestand_berichtigung1_{probe,einspielen}.sql, druckt Größe/md5
         python3 -I tools/bestand_berichtigung1_sql.py --pakete --pruefen -> schreibt nichts; Rückgabe 1, wenn die Dateien nicht dem Stand entsprechen

NICHT AUSFÜHREN ohne den ausdrücklichen Satz des Nutzers. Das Paket ändert nichts an App-Code, Kinder-Lernständen oder Quelldateien.
Was es tut (je Paar „alte Aufgabe -> berichtigte neue“): erkennt die alte Aufgabe (Einheit, Vorrat, Lernkarte, Typ, Frage-JSON, Antworten, Lösung, Platz),
fügt die neue über schule.aufgaben_einfuegen ein (gleiche Einheit/Lernkarte/Vorrat), schreibt Regel und Fehlbilder (schule.aufgabe_regel / aufgabe_fehlbild)
und sperrt die alte (freigegeben = false; dafür kurz Einheit 'geprueft' und zurück, wie 20261123_tl_s_teilung.sql). Alles in einer Transaktion mit
Selbstprüfung (siehe Kopfkommentar der erzeugten Datei).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
import regelbezug_sql as R  # noqa: E402
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import nf_einspielen as NF  # noqa: E402

BB = WURZEL / 'inhalte/mathe-profi/bestand-berichtigung-1'
AUS = WURZEL / 'tools/tests/aus'
BLOCK = 90000          # Platz der neuen Aufgaben: max_r + 90000 + laufende Nummer in der Einheit (frei von den Runden-Blöcken 1000·R)
FELDER = ('l', 't', 'p', 's', 'g', 'y', 'f', 'a', 'o', 'h', 'w')
THEMEN_PRAEFIX = {'zahlen.natuerlich': 'K5A', 'bruch.prozent': 'K6'}   # Aufgaben ohne Kennung (inhalte/themen): Schema der Runden desselben Themas (K5A-Vnnn / K6-Vnnn)
FORM = {'Lückenweg': 'lueckenweg', 'Umkehren': 'umkehren', 'Brücke': 'bruecke', 'Anwenden': 'anwenden'}


def lesen(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def daten():
    """Liste der Paare (sortiert nach BB1-Kennung) mit allem, was das SQL braucht; prüft die Zuordnung zu den Quelldateien (nur lesend)."""
    vs = lesen(BB / 'vorschlag.json')['aufgaben']
    plan = lesen(WURZEL / 'inhalte/plan/rollend-einheiten.json')['einheiten']
    aus, _ = R.eingespielt()
    rep = R.repo_eintraege()
    nummer = {}            # Schema-Präfix -> höchste vergebene Nummer
    for k in rep:
        m = re.match(r'^([A-Z0-9]+)-V(\d+)$', k)
        if m: nummer[m.group(1)] = max(nummer.get(m.group(1), 0), int(m.group(2)))
    belegt = set(rep)
    platz = {}             # Einheit -> laufende Nummer
    out = []
    for v in sorted(vs, key=lambda x: x['kennung']):
        er, neu = v['ersetzt'], v['aufgabe']
        e = er['einheit_id']
        pe = plan[v['thema']]
        assert pe['id'] == e, (v['kennung'], pe['id'], e)
        # --- Vorgänger (so, wie er in der Datenbank steht)
        quelle = lesen(WURZEL / er['datei'])
        if er['kennung']:
            eintrag = rep[er['kennung']]
            alt_roll = eintrag['aufgabe']
            treffer = [(k, row) for k, row in aus.items() if k[0] == e and row['f'] == alt_roll['f'] and row['l'] == alt_roll['l']]
            assert len(treffer) == 1, (v['kennung'], 'Vorgänger nicht eindeutig im eingespielten Bestand', len(treffer))
            (_, ar), alt = treffer[0]
            assert alt['f'] == er['alte_frage_json'] and alt.get('o') == alt_roll['o'] and alt['y'] == alt_roll['y'], v['kennung']
            alt_pool, alt_form, alt_zaehlt = alt['p'], alt.get('form'), alt.get('zaehlt')
            praefix = er['kennung'].split('-V')[0]
        else:
            alt = quelle['aufgaben'][er['index_in_datei']]
            assert alt['f'] == er['alte_frage_json'], v['kennung']
            ar = None                       # Platz der Themen-Aufgaben steht nicht im Repo: Erkennung über Inhalt
            alt_pool, alt_form, alt_zaehlt = alt['p'], None, None
            praefix = THEMEN_PRAEFIX[v['thema']]
        assert alt['y'] == neu['y'] and alt['l'] == neu['l'] and alt['p'] == neu['p'] and alt['s'] == neu['s'], (v['kennung'], 'Vorrat/Lernkarte/Stufe/Typ geändert')
        assert alt['f'] != neu['f'] or alt.get('a') != neu.get('a'), (v['kennung'], 'neue Aufgabe gleicht der alten (aufgaben_einfuegen würde nichts einfügen)')
        # --- endgültige Kennung
        nummer[praefix] = nummer.get(praefix, 0) + 1
        kennung = f'{praefix}-V{nummer[praefix]:03d}'
        assert kennung not in belegt; belegt.add(kennung)
        platz[e] = platz.get(e, 0) + 1
        r_neu = pe['max_r'] + BLOCK + platz[e]
        # --- neue Aufgabe als JSON für aufgaben_einfuegen
        form = v.get('form') if v.get('form') is not None else FORM.get(v.get('typ'))
        row = {f: neu[f] for f in FELDER if neu.get(f) is not None}
        row['r'] = r_neu
        row['form'], row['zaehlt'] = (form, v.get('zaehlt')) if er['kennung'] else (None, None)
        regel = v.get('regel') or None
        if regel and not R.KENNUNG.match(regel): raise SystemExit(f'{v["kennung"]}: Regel „{regel}“ ist keine Kennung')
        fb, weg = R.fehlbilder(v, row)
        assert not weg, (v['kennung'], dict(weg))
        assert len(fb) == len(v['fehlbilder']) and fb, v['kennung']
        out.append(dict(bb=v['kennung'], kennung=kennung, e=e, thema=v['thema'], pool=alt_pool, l=neu['l'], y=neu['y'], s=neu['s'],
                        af=er['alte_frage_json'], aa=er['alte_antworten'], ao=alt['o'], ar=ar, alt_kennung=er['kennung'], alt_idx=er['index_in_datei'], row=row, nr=r_neu,
                        nf=neu['f'], na=neu.get('a'), regel=regel, fb=fb, grund=v.get('grund'), datei=er['datei']))
    return out


def q(s):
    return 'null' if s is None else "'" + str(s).replace("'", "''") + "'"


def jn(x):
    return 'null::jsonb' if x is None else j(x)


def j(x):
    s = json.dumps(x, ensure_ascii=False)
    assert '$bbj$' not in s
    return f'$bbj${s}$bbj$::jsonb'


def abbildung(paare):
    return {'stand': '2026-11-28', 'paket': 'bestand-berichtigung-1',
            'hinweis': 'BB1-… (Arbeitskennung in vorschlag.json) -> endgültige Kennung im Schema der Runde; Platz = Spalte reihenfolge der neuen Aufgabe; '
                       'Vorgänger = die zu sperrende Aufgabe (Kennung nur bei Runden-Aufgaben; Themen-Aufgaben haben keine Kennung).',
            'aufgaben': [{'bb': p['bb'], 'kennung_neu': p['kennung'], 'einheit_id': p['e'], 'thema': p['thema'], 'vorrat': p['pool'], 'lernkarte': p['l'],
                          'platz_neu': p['nr'], 'vorgaenger_kennung': p['alt_kennung'], 'vorgaenger_platz': p['ar'], 'vorgaenger_datei': p['datei'],
                          'regel': p['regel'], 'fehlbilder': len(p['fb'])} for p in paare]}

VERWEIS_TEXT = """    gef := '{{}}';
    if exists (select 1 from schule.misch_ausgabe m where m.aufgabe_id = @.alt_id and m.eingeloest_am is null and m.verfallen_am is null and m.ausgegeben_am > now() - interval '24 hours') then gef := gef || 'offene Mischkarte'::text; end if;
    if exists (select 1 from schule.testsitzung s where @.alt_id = any(s.aufgaben) and s.status <> 'abgeschlossen' and s.abgeschlossen_am is null) then gef := gef || 'laufende Testsitzung'::text; end if;
    if exists (select 1 from schule.versuch v where v.aufgabe_id = @.alt_id and v.anlauf = 1 and not v.richtig and v.testsitzung_id is null and v.am > now() - interval '2 hours'
         and not exists (select 1 from schule.versuch w where w.lernender_id = v.lernender_id and w.aufgabe_id = v.aufgabe_id and w.am > v.am)) then gef := gef || 'falscher 1. Anlauf ohne zweiten Versuch'::text; end if;"""


def VERWEIS(var):
    return VERWEIS_TEXT.replace('@', var).replace("'{{}}'", "'{}'")


def paket(paare, probe=False):
    werte = []
    for p in paare:
        nf, na = p['nf'], p['na']
        werte.append(f"    ({q(p['bb'])}, {q(p['kennung'])}, {p['e']}, {q(p['pool'])}, {q(p['l'])}, {q(p['y'])}, {j(p['af'])}, {jn(p['aa'])}, {j(p['ao'])}, "
                     f"{'null' if p['ar'] is None else p['ar']}, {j(p['row'])}, {p['nr']}, {j(nf)}, {jn(na)}, {q(p['regel'])}, {j(p['fb'])})")
    n = len(paare)
    n_regel = sum(1 for p in paare if p['regel'])
    n_fb = sum(len(p['fb']) for p in paare)
    einheiten = sorted({p['e'] for p in paare})
    modus = 'PROBELAUF (rollt am Ende ALLES zurück)' if probe else 'Einspielen'
    ende = ("  raise exception 'PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt): %', v_bericht::text;\n" if probe
            else "  raise notice 'BB1 eingespielt: %', v_bericht::text;\n")
    return f"""-- Bestands-Berichtigung 1 ({modus}): {n} Paare (alte Aufgabe -> berichtigte neue), {n_regel} Regeln, {n_fb} Fehlbilder, {len(einheiten)} Einheiten.
-- VORAUSSETZUNG: NF-S (nachtest_auswahl/nachtest_stand/test_starten_intern nur mit freigegebenen Aufgaben, tools/tests/aus/nf_s_einspielen.sql) ist eingespielt – sonst Abbruch.
-- LERNPAUSE: von VOR der Verweisprüfung bis zum Ende dieses Aufrufs (Mischkarten-Fenster, siehe inhalte/mathe-profi/bestand-berichtigung-1/einspielen.md).
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT. Jede Abweichung = Abbruch, ALLES zurück. Wiederholbar: ein zweiter Lauf erkennt „schon berichtigt“ (voller Sollvergleich) und schreibt nichts.
-- Je Paar: Zustand neu (alte freigegeben, neue fehlt) | fertig (alte gesperrt, neue da und gleich dem Soll in ALLEN Feldern, Regel und Fehlbildern) | zurueckgestellt (offener Verweis:
-- das Paar bleibt UNBERÜHRT – weder neue Aufgabe noch Sperre, damit die Lernkarte nie eine Aufgabe mehr zählt) | sonst Abbruch (nicht erkannt, Zwischenstand, Einheit nicht freigegeben).
-- Reihenfolge: Einheitszeilen sperren (FOR NO KEY UPDATE) -> Verweisprüfung 1 -> einfügen -> Antwortprobe (alle Soll-Antworten richtig, alle Fehlantworten gültig und falsch, Fehlbild erkannt)
-- -> je Einheit: Verweisprüfung 2 unmittelbar vor dem Sperren (neuer Verweis = Abbruch) -> Einheit 'geprueft', freigegeben = false, Einheit 'freigegeben' -> Nachprüfungen.
-- Offener Verweis auf die alte Aufgabe: ausgegebene, nicht eingelöste Mischkarte (<24 h), laufende Testsitzung mit der Aufgabe, falscher 1. Anlauf ohne Folgeversuch (<2 h).
-- Nebenwirkungsprüfung: (1) Trigger auf einheit/aufgabe/aufgabe_regel/aufgabe_fehlbild: Textsuche in der Funktion (kein Schreiben/Melden); (2) Trigger-Satz samt Funktionstext vorher = nachher;
-- (3) in KEINER Tabelle des Schemas schule steht eine von dieser Transaktion geschriebene Zeile (xmin) außer aufgabe (neu + gesperrt), aufgabe_regel, aufgabe_fehlbild, einheit;
-- (4) Fingerabdruck (md5 über die Zeilen) der UNBERÜHRTEN Zeilen von aufgabe, einheit, aufgabe_regel, aufgabe_fehlbild vorher = nachher; (5) karte_ziel / karte_typen_noetig /
-- karte_schwer_noetig / karte_anwenden_noetig (alle vier Pflicht) je betroffener Lernkarte vorher = nachher; (6) Zahl freigegebener Aufgaben je Einheit/Vorrat/Lernkarte gleich;
-- (7) Einheitszeile nach dem Statuswechsel Spalte für Spalte gleich. GRENZEN (ehrlich): xmin sieht keine Löschungen, Sequenzänderungen, externe Effekte, fremde Schemas und nicht
-- zuverlässig Untertransaktionen; die Trigger-Textsuche sieht delegierte/dynamische Schreibvorgänge nicht (dafür (3)); versuch/karte_stand/… haben wegen laufender Kinder-Aktivität
-- keinen Fingerabdruck, nur (3); eine nach Verweisprüfung 2 gezogene Mischkarte schließt nur die Lernpause aus.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '120s', true);
do $bb1$
declare z record; z2 record; alt schule.aufgabe; neu schule.aufgabe; fehler text[] := '{{}}'; zurueck text[] := '{{}}';
  n_alt int; n_neu int; cnt bigint; f jsonb; v jsonb; b jsonb; v_vor jsonb; v_nach jsonb; xid_ xid := pg_current_xact_id()::xid; d text;
  n_neu_ges int := 0; n_gesperrt int := 0; n_fertig int := 0; n_regel_neu int := 0; n_fb_neu int := 0; tr record; trg text; trg_vor text; trg_nach text; gef text[] := '{{}}';
  v_bericht jsonb; audit jsonb := '{{}}'; erw jsonb; tab text; kk record; wert text; fn text; fp_vor text[]; fp_nach text[]; n_soll_ok int := 0; n_fb_ok int := 0;
begin
  -- Voraussetzungen (RB-S, FT-S, NF-S, Karten-Funktionen, Tabellen)
  if to_regclass('schule.aufgabe_fehlbild') is null or to_regclass('schule.aufgabe_regel') is null
     or to_regprocedure('schule.fehlbild_finden(schule.aufgabe, jsonb)') is null or to_regprocedure('schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)') is null
     or to_regprocedure('schule.aufgaben_einfuegen(bigint, jsonb)') is null or to_regprocedure('schule.antwort_bewerten(schule.aufgabe, jsonb)') is null then
    raise exception 'BB1: erst RB-S (20261204_rb_s_regelbezug.sql) und FT-S einspielen'; end if;
  if (select count(*) from pg_attribute where attrelid = 'schule.aufgabe'::regclass and attname in ('form', 'zaehlt', 'freigegeben', 'typ', 'expedition_id', 'teil') and not attisdropped) <> 6
     or position('x->>''form''' in pg_get_functiondef('schule.aufgaben_einfuegen(bigint, jsonb)'::regprocedure)) = 0 then
    raise exception 'BB1: erst FT-S einspielen (Spalten form/zaehlt, aufgaben_einfuegen)'; end if;
  if to_regclass('schule.misch_ausgabe') is null or to_regclass('schule.testsitzung') is null or to_regclass('schule.versuch') is null then
    raise exception 'BB1 ABBRUCH: Tabellen misch_ausgabe/testsitzung/versuch fehlen (Verweisprüfung nicht möglich)'; end if;
  foreach fn in array array['karte_ziel', 'karte_typen_noetig', 'karte_schwer_noetig', 'karte_anwenden_noetig'] loop
    if to_regprocedure('schule.' || fn || '(bigint, text)') is null then raise exception 'BB1 ABBRUCH: schule.%(bigint, text) fehlt (Pflichtprüfung der Lernkarten-Regeln)', fn; end if;
  end loop;
  if to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)') is null or to_regprocedure('schule.nachtest_stand(bigint, bigint)') is null
     or to_regprocedure('schule.test_starten_intern(bigint, jsonb)') is null
     or md5((select prosrc from pg_proc where oid = to_regprocedure('schule.test_starten_intern(bigint, jsonb)'))) <> '{NF.md5(NF.tsi_neu())}'
     or md5((select prosrc from pg_proc where oid = to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)'))) <> '{NF.md5(NF.auswahl_neu())}'
     or md5((select prosrc from pg_proc where oid = to_regprocedure('schule.nachtest_stand(bigint, bigint)'))) <> '{NF.md5(NF.stand_neu())}' then
    raise exception 'BB1 ABBRUCH: erst NF-S einspielen (nachtest_auswahl, nachtest_stand und test_starten_intern müssen exakt die neue Fassung mit Freigabefilter haben)'; end if;
  create temp table bb1_p on commit drop as
    select x.*, null::bigint alt_id, null::bigint neu_id, null::text zustand, null::text grund_zurueck from (values
{(',' + chr(10)).join(werte)}
  ) x(bb, k, e, pool, l, y, af, aa, ao, ar, nrow, nr, nf, na, regel, fb);
  -- 1. Erkennen und Zustand je Paar
  for z in select * from bb1_p order by bb collate "C" loop
    select count(*), min(x.id) into n_alt, cnt from schule.aufgabe x
     where x.einheit_id = z.e and x.pool is not distinct from z.pool and x.variante_gruppe is not distinct from z.l and x.antworttyp is not distinct from z.y
       and x.frage is not distinct from z.af and x.antworten is not distinct from z.aa and x.loesung is not distinct from z.ao and (z.ar is null or x.reihenfolge is not distinct from z.ar);
    update bb1_p set alt_id = cnt where bb = z.bb;
    select count(*), min(x.id) into n_neu, cnt from schule.aufgabe x where x.einheit_id = z.e and x.frage is not distinct from z.nf and x.antworten is not distinct from z.na;
    update bb1_p set neu_id = cnt where bb = z.bb;
    if n_alt > 1 or n_neu > 1 then fehler := fehler || format('%s: %s alte / %s neue Aufgaben gefunden (erwartet höchstens je eine)', z.bb, n_alt, n_neu); continue; end if;
    select * into alt from schule.aufgabe where id = (select alt_id from bb1_p where bb = z.bb);
    select * into neu from schule.aufgabe where id = (select neu_id from bb1_p where bb = z.bb);
    -- gemeinsame Voraussetzung für „neu“ UND „fertig“: die Einheit ist freigegeben (ein Paar ohne Fund wird unten ohnehin gemeldet)
    if (n_alt + n_neu) > 0 and (select status from schule.einheit where id = z.e) is distinct from 'freigegeben' then
      fehler := fehler || format('%s: Einheit %s ist nicht freigegeben', z.bb, z.e); continue; end if;
    if n_alt = 1 and n_neu = 0 then
      if not alt.freigegeben then fehler := fehler || format('%s: alte Aufgabe %s ist schon gesperrt, die neue fehlt', z.bb, alt.id); continue; end if;
      if exists (select 1 from schule.aufgabe x where x.einheit_id = z.e and x.reihenfolge = z.nr) then fehler := fehler || format('%s: Platz %s in Einheit %s schon belegt', z.bb, z.nr, z.e); continue; end if;
      update bb1_p set zustand = 'neu' where bb = z.bb;
    elsif n_alt = 1 and n_neu = 1 then
      if alt.freigegeben then fehler := fehler || format('%s: alte (%s) und neue (%s) Aufgabe sind beide gültig – Zwischenstand, nicht von diesem Paket', z.bb, alt.id, neu.id); continue; end if;
      -- fertig: neue Aufgabe VOLLSTÄNDIG gleich dem Soll (alle Felder), Regel und Fehlbilder gleich dem Soll
      if (neu.einheit_id, neu.freigegeben, neu.pool, neu.variante_gruppe, neu.antworttyp, neu.loesung, neu.reihenfolge, neu.frage, neu.antworten, neu.stufe, neu.typ, neu.form, neu.zaehlt,
          neu.teilfaehigkeit, neu.tipp, neu.loesungsweg, neu.expedition_id, neu.teil)
         is distinct from (z.e, true, z.pool, z.l, z.y, z.nrow->'o', z.nr, z.nf, z.na, (z.nrow->>'s')::smallint, z.nrow->>'g', z.nrow->>'form', z.nrow->>'zaehlt',
          z.nrow->>'t', z.nrow->>'h', z.nrow->>'w', null::bigint, null::text)
         or (neu.thema_id, neu.art, neu.punkte_max, neu.expedition_id, neu.teil) is distinct from (alt.thema_id, alt.art, alt.punkte_max, alt.expedition_id, alt.teil) then
        fehler := fehler || format('%s: neue Aufgabe %s steht schon da, weicht aber vom Soll ab (Einheit, Vorrat, Lernkarte, Antworttyp, Frage, Antworten, Lösung, Platz, Stufe, Typ, Form, zählt, Teilfähigkeit, Tipp, Lösungsweg, Expedition, Teil)', z.bb, neu.id); continue; end if;
      if (select r.regel from schule.aufgabe_regel r where r.aufgabe_id = neu.id) is distinct from z.regel
         or (select count(*) from schule.aufgabe_fehlbild x where x.aufgabe_id = neu.id) <> jsonb_array_length(z.fb)
         or exists (select 1 from jsonb_array_elements(z.fb) y where not exists (select 1 from schule.aufgabe_fehlbild x where x.aufgabe_id = neu.id and x.nr = (y->>'nr')::smallint
              and (x.art, x.luecke, x.wert, x.beschreibung, x.fehlbild, x.regel) is not distinct from (y->>'art', (y->>'luecke')::smallint, y->>'wert', y->>'text', y->>'fehlbild', y->>'regel'))) then
        fehler := fehler || format('%s: neue Aufgabe %s hat andere Regel/Fehlbilder als das Soll', z.bb, neu.id); continue; end if;
      update bb1_p set zustand = 'fertig' where bb = z.bb;
    elsif n_alt = 0 and n_neu = 1 then
      fehler := fehler || format('%s: neue Aufgabe %s steht da, die alte wird nicht erkannt (verändert?)', z.bb, neu.id);
    else
      fehler := fehler || format('%s: weder alte noch neue Aufgabe gefunden (Einheit %s, Vorrat %s, Lernkarte %s)', z.bb, z.e, z.pool, z.l);
    end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'BB1 ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 1b. Einheitszeilen der zu ändernden Paare sperren (FOR NO KEY UPDATE: Fremdschlüssel-Einfügungen der Kinder werden nicht blockiert); erst DANACH die Verweisprüfung
  perform 1 from schule.einheit where id in (select e from bb1_p where zustand = 'neu') order by id for no key update;
  -- 2. Verweisprüfung 1 -> Paar zurückstellen
  for z in select * from bb1_p where zustand = 'neu' order by bb collate "C" loop
{VERWEIS('z')}
    if array_length(gef, 1) > 0 then
      update bb1_p set zustand = 'zurueckgestellt', grund_zurueck = array_to_string(gef, ', ') where bb = z.bb;
      zurueck := zurueck || (z.bb || ' (Aufgabe ' || z.alt_id || '): ' || array_to_string(gef, ', '));
    end if;
  end loop;
  select count(*) into n_neu_ges from bb1_p where zustand = 'neu';
  select count(*) into n_fertig from bb1_p where zustand = 'fertig';
  -- 3. Vorher-Stand (nur für Paare, die geändert werden)
  create temp table bb1_k on commit drop as select distinct e, l, pool from bb1_p where zustand = 'neu';
  create temp table bb1_v on commit drop as select kx.e, kx.l, kx.pool, null::text karte_vor, null::text karte_nach,
    (select count(*) from schule.aufgabe x where x.einheit_id = kx.e and x.pool = kx.pool and x.variante_gruppe = kx.l and x.freigegeben) frei_vor, null::bigint frei_nach from bb1_k kx;
  for kk in select * from bb1_v loop
    wert := '';
    foreach fn in array array['karte_ziel', 'karte_typen_noetig', 'karte_schwer_noetig', 'karte_anwenden_noetig'] loop
      execute format('select coalesce(schule.%I($1, $2)::text, ''-'')', fn) into trg using kk.e, kk.l; wert := wert || fn || '=' || trg || ';';
    end loop;
    update bb1_v set karte_vor = wert where e = kk.e and l = kk.l and pool = kk.pool;
  end loop;
  select coalesce(string_agg(cl.relname || ':' || g.tgname || ':' || md5(pg_get_triggerdef(g.oid)) || ':' || md5(p.prosrc), ',' order by cl.relname, g.tgname), '') into trg_vor
    from pg_trigger g join pg_class cl on cl.oid = g.tgrelid join pg_proc p on p.oid = g.tgfoid
   where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild');
  -- Trigger auf einheit/aufgabe/aufgabe_regel/aufgabe_fehlbild dürfen weder schreiben noch melden (Textsuche in der Funktion); die bekannten Schutz-Trigger sind harmlos
  for tr in select cl.relname, tg.tgname, p.proname, p.prosrc from pg_trigger tg join pg_class cl on cl.oid = tg.tgrelid join pg_proc p on p.oid = tg.tgfoid
            where not tg.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild') loop
    if tr.prosrc ~* '(insert\\s+into|delete\\s+from|update\\s+[a-z_.]+\\s+set|pg_notify|net\\.http|http_|dblink|truncate)' then
      fehler := fehler || format('Trigger %s.%s (Funktion %s) schreibt oder meldet vielleicht – von Hand prüfen (select prosrc from pg_proc where proname = ''%s'')', tr.relname, tr.tgname, tr.proname, tr.proname); end if;
  end loop;
  -- FESTE Soll-Liste der Schutz-Trigger (Tabelle:Name): genau diese fünf, keine weiteren, keine fehlenden
  if exists (select 1 from (select cl.relname || ':' || g.tgname as n from pg_trigger g join pg_class cl on cl.oid = g.tgrelid
                             where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild')) ist
              full join (select unnest(array['einheit:einheit_schutz', 'aufgabe:aufgabe_schutz', 'aufgabe:aufgabe_bedingung_schutz', 'aufgabe_regel:aufgabe_regel_schutz', 'aufgabe_fehlbild:aufgabe_fehlbild_schutz']) as n) soll
                     on ist.n = soll.n where ist.n is null or soll.n is null) then   -- Mengenvergleich in beide Richtungen: unabhängig von der Kollation der Datenbank
    fehler := fehler || format('Trigger auf einheit/aufgabe/aufgabe_regel/aufgabe_fehlbild weichen von der festen Soll-Liste ab (erwartet einheit_schutz, aufgabe_schutz, aufgabe_bedingung_schutz, aufgabe_regel_schutz, aufgabe_fehlbild_schutz); gefunden: %s',
      coalesce((select string_agg(cl.relname || ':' || g.tgname, ', ' order by cl.relname, g.tgname) from pg_trigger g join pg_class cl on cl.oid = g.tgrelid
       where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild')), '(keine)')); end if;
  if array_length(fehler, 1) > 0 then raise exception 'BB1 ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  create temp table bb1_e on commit drop as select x.id from (select distinct e id from bb1_p where zustand = 'neu') x;
  create temp table bb1_a on commit drop as select x.id, to_jsonb(x) - 'freigegeben' vor, null::jsonb nach from schule.aufgabe x where x.id in (select alt_id from bb1_p where zustand = 'neu');
  -- Fingerabdruck der unberührten Zeilen (vorher)
  fp_vor := array[(select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.aufgabe x where x.id not in (select alt_id from bb1_p where zustand = 'neu')),
                  (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.einheit x where x.id not in (select id from bb1_e)),
                  (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id), '')) from schule.aufgabe_regel x),
                  (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id, x.nr), '')) from schule.aufgabe_fehlbild x)];
  -- 4. Neue Aufgaben einfügen, Regel und Fehlbilder schreiben
  for z in select * from bb1_p where zustand = 'neu' order by bb collate "C" loop
    select * into alt from schule.aufgabe where id = z.alt_id;
    n_neu := schule.aufgaben_einfuegen(z.e, jsonb_build_array(z.nrow));
    if n_neu <> 1 then fehler := fehler || format('%s: %s statt 1 Aufgabe eingefügt', z.bb, n_neu); continue; end if;
    select * into neu from schule.aufgabe x where x.einheit_id = z.e and x.frage is not distinct from z.nf and x.antworten is not distinct from z.na;
    update bb1_p set neu_id = neu.id where bb = z.bb;
    if neu.id is null or (neu.einheit_id, neu.freigegeben, neu.pool, neu.variante_gruppe, neu.antworttyp, neu.loesung, neu.reihenfolge, neu.frage, neu.antworten, neu.stufe, neu.typ, neu.form, neu.zaehlt,
          neu.teilfaehigkeit, neu.tipp, neu.loesungsweg, neu.expedition_id, neu.teil)
         is distinct from (z.e, true, z.pool, z.l, z.y, z.nrow->'o', z.nr, z.nf, z.na, (z.nrow->>'s')::smallint, z.nrow->>'g', z.nrow->>'form', z.nrow->>'zaehlt',
          z.nrow->>'t', z.nrow->>'h', z.nrow->>'w', null::bigint, null::text) then
      fehler := fehler || format('%s: eingefügte Aufgabe %s hat nicht die Werte des Pakets', z.bb, neu.id); continue; end if;
    -- Alt/Neu-Gleichheit: zählt NULL und 'ja' gelten als gleich (fachlich: schule.aufgabe_zaehlt = „zaehlt is distinct from 'nein'“, FT-S Regel 5); alles andere exakt
    if (alt.thema_id, alt.art, alt.stufe, alt.variante_gruppe, alt.antworttyp, alt.pool, alt.punkte_max, coalesce(alt.zaehlt, 'ja'), alt.expedition_id, alt.teil)
       is distinct from (neu.thema_id, neu.art, neu.stufe, neu.variante_gruppe, neu.antworttyp, neu.pool, neu.punkte_max, coalesce(neu.zaehlt, 'ja'), neu.expedition_id, neu.teil) then
      fehler := fehler || format('%s: neue Aufgabe %s unterscheidet sich von der alten %s in Thema/Art/Stufe/Lernkarte/Typ/Vorrat/Punkte/zählt', z.bb, neu.id, alt.id); continue; end if;
    if z.regel is not null then
      insert into schule.aufgabe_regel (aufgabe_id, regel) values (neu.id, z.regel) on conflict do nothing;
      get diagnostics cnt = row_count; n_regel_neu := n_regel_neu + cnt;
    end if;
    for f in select * from jsonb_array_elements(z.fb) loop
      insert into schule.aufgabe_fehlbild (aufgabe_id, nr, art, luecke, wert, beschreibung, fehlbild, regel)
      values (neu.id, (f->>'nr')::smallint, f->>'art', (f->>'luecke')::smallint, f->>'wert', f->>'text', f->>'fehlbild', f->>'regel') on conflict do nothing;
      get diagnostics cnt = row_count; n_fb_neu := n_fb_neu + cnt;
    end loop;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'BB1 ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 4b. Antwortprobe über die Bewertungsfunktion (neue UND schon vorhandene neue): Soll-Antwort richtig, jede Fehlantwort gültig und falsch und als genau dieses Fehlbild erkannt
  for z in select * from bb1_p where zustand in ('neu', 'fertig') order by bb collate "C" loop
    select * into neu from schule.aufgabe where id = z.neu_id;
    v := case z.y when 'zahl' then jsonb_build_object('wert', replace(z.nrow->'o'->>'wert', '.', ',')) when 'luecken' then jsonb_build_object('werte', z.nrow->'o'->'werte')
                  when 'auswahl' then jsonb_build_object('index', z.nrow->'o'->'index') end;
    b := schule.antwort_bewerten(neu, v);
    if coalesce((b->>'format_ok')::boolean, false) and coalesce((b->>'richtig')::boolean, false) then n_soll_ok := n_soll_ok + 1;
    else fehler := fehler || format('%s: die Soll-Antwort %s wird nicht als richtig bewertet (%s)', z.bb, v, b); end if;
    for f in select * from jsonb_array_elements(z.fb) loop
      v := schule.fehlbild_probeantwort(neu, f->>'art', (f->>'luecke')::int, f->>'wert');
      b := schule.antwort_bewerten(neu, v);
      if not coalesce((b->>'format_ok')::boolean, false) or coalesce((b->>'richtig')::boolean, true) then
        fehler := fehler || format('%s: Fehlbild %s – Antwort %s wird nicht als gültig und falsch bewertet (%s)', z.bb, f->>'nr', v, b); continue; end if;
      if schule.fehlbild_finden(neu, v) is distinct from (f->>'nr')::smallint then fehler := fehler || format('%s: Fehlbild %s wird an der Antwort %s nicht wiedererkannt', z.bb, f->>'nr', v); continue; end if;
      n_fb_ok := n_fb_ok + 1;
    end loop;
    if (select count(*) from schule.aufgabe_fehlbild x where x.aufgabe_id = neu.id) <> jsonb_array_length(z.fb)
       or (select r.regel from schule.aufgabe_regel r where r.aufgabe_id = neu.id) is distinct from z.regel then
      fehler := fehler || format('%s: Aufgabe %s hat andere Regel/Fehlbilder in der Datenbank als im Paket', z.bb, neu.id); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'BB1 ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 5. Alte Aufgaben sperren (je Einheit: Verweisprüfung 2, dann kurz 'geprueft', freigegeben = false, zurück 'freigegeben'; Einheitszeile danach unverändert)
  for tr in select id from bb1_e order by id loop
    perform 1 from schule.einheit where id = tr.id for no key update;
    for z2 in select * from bb1_p where zustand = 'neu' and e = tr.id order by bb collate "C" loop
{VERWEIS('z2')}
      if array_length(gef, 1) > 0 then
        raise exception 'BB1 ABBRUCH, alles zurückgerollt: % hat nach der ersten Prüfung einen offenen Verweis bekommen (Aufgabe %: %) – Lernpause einhalten und nochmals ausführen', z2.bb, z2.alt_id, array_to_string(gef, ', ');
      end if;
    end loop;
    select to_jsonb(x) into v_vor from schule.einheit x where x.id = tr.id;
    if v_vor->>'status' <> 'freigegeben' then fehler := fehler || format('Einheit %s ist nicht freigegeben', tr.id); continue; end if;
    update schule.einheit set status = 'geprueft' where id = tr.id;
    update schule.aufgabe set freigegeben = false where id in (select alt_id from bb1_p where zustand = 'neu' and e = tr.id) and freigegeben;
    get diagnostics cnt = row_count;
    n_gesperrt := n_gesperrt + cnt;
    if cnt <> (select count(*) from bb1_p where zustand = 'neu' and e = tr.id) then fehler := fehler || format('Einheit %s: %s statt %s Aufgaben gesperrt', tr.id, cnt, (select count(*) from bb1_p where zustand = 'neu' and e = tr.id)); end if;
    update schule.einheit set status = 'freigegeben' where id = tr.id;
    select to_jsonb(x) into v_nach from schule.einheit x where x.id = tr.id;
    if v_nach is distinct from v_vor then fehler := fehler || format('Einheit %s hat sich durch den Statuswechsel verändert (Nebenwirkung): vorher %s, nachher %s', tr.id, left(v_vor::text, 300), left(v_nach::text, 300)); end if;
  end loop;
  update bb1_a set nach = (select to_jsonb(x) - 'freigegeben' from schule.aufgabe x where x.id = bb1_a.id);
  if exists (select 1 from bb1_a x where x.nach is distinct from x.vor) or exists (select 1 from schule.aufgabe x where x.id in (select id from bb1_a) and x.freigegeben) then
    fehler := fehler || 'eine alte Aufgabe ist nicht gesperrt oder hat sich in einer anderen Spalte als freigegeben verändert'::text; end if;
  if array_length(fehler, 1) > 0 then raise exception 'BB1 ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  -- 6. Nachher: Lernkarten-Regeln, Zählungen, Trigger, Fingerabdruck, Schreib-Prüfung über das ganze Schema
  for kk in select * from bb1_v loop
    wert := '';
    foreach fn in array array['karte_ziel', 'karte_typen_noetig', 'karte_schwer_noetig', 'karte_anwenden_noetig'] loop
      execute format('select coalesce(schule.%I($1, $2)::text, ''-'')', fn) into trg using kk.e, kk.l; wert := wert || fn || '=' || trg || ';';
    end loop;
    select count(*) into cnt from schule.aufgabe x where x.einheit_id = kk.e and x.pool = kk.pool and x.variante_gruppe = kk.l and x.freigegeben;
    update bb1_v set karte_nach = wert, frei_nach = cnt where e = kk.e and l = kk.l and pool = kk.pool;
  end loop;
  if exists (select 1 from bb1_v where karte_vor is distinct from karte_nach or frei_vor <> frei_nach) then
    fehler := fehler || ('Lernkarten-Regeln ändern sich: ' || (select string_agg(format('Einheit %s/%s/%s: %s -> %s (freigegeben %s -> %s)', e, l, pool, karte_vor, karte_nach, frei_vor, frei_nach), ' | ')
                                                                from bb1_v where karte_vor is distinct from karte_nach or frei_vor <> frei_nach)); end if;
  select coalesce(string_agg(cl.relname || ':' || g.tgname || ':' || md5(pg_get_triggerdef(g.oid)) || ':' || md5(p.prosrc), ',' order by cl.relname, g.tgname), '') into trg_nach
    from pg_trigger g join pg_class cl on cl.oid = g.tgrelid join pg_proc p on p.oid = g.tgfoid
   where not g.tgisinternal and cl.relnamespace = 'schule'::regnamespace and cl.relname in ('einheit', 'aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild');
  if trg_vor <> trg_nach then fehler := fehler || 'der Trigger-Satz hat sich während des Pakets verändert'::text; end if;
  fp_nach := array[(select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.aufgabe x where x.id not in (select alt_id from bb1_p where zustand = 'neu')
                      and x.id not in (select neu_id from bb1_p where zustand = 'neu')),
                   (select md5(coalesce(string_agg(x::text, '|' order by x.id), '')) from schule.einheit x where x.id not in (select id from bb1_e)),
                   (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id), '')) from schule.aufgabe_regel x where x.aufgabe_id not in (select neu_id from bb1_p where zustand = 'neu')),
                   (select md5(coalesce(string_agg(x::text, '|' order by x.aufgabe_id, x.nr), '')) from schule.aufgabe_fehlbild x where x.aufgabe_id not in (select neu_id from bb1_p where zustand = 'neu'))];
  if fp_vor is distinct from fp_nach then fehler := fehler || 'Fingerabdruck der unberührten Zeilen (aufgabe, einheit, aufgabe_regel, aufgabe_fehlbild) hat sich geändert (fremde Änderung oder Nebenwirkung)'::text; end if;
  erw := jsonb_build_object('aufgabe', n_neu_ges * 2, 'aufgabe_regel', n_regel_neu, 'aufgabe_fehlbild', n_fb_neu, 'einheit', (select count(*) from bb1_e));
  for tab in select cl.relname from pg_class cl where cl.relnamespace = 'schule'::regnamespace and cl.relkind = 'r' order by 1 loop
    execute format('select count(*) from schule.%I where xmin = $1', tab) into cnt using xid_;
    if cnt > 0 or erw ? tab then audit := audit || jsonb_build_object(tab, cnt); end if;
    if cnt <> coalesce((erw->>tab)::int, 0) then fehler := fehler || format('Tabelle schule.%s: %s von diesem Paket geschriebene Zeilen, erwartet %s (Nebenwirkung?)', tab, cnt, coalesce((erw->>tab)::int, 0)); end if;
  end loop;
  if n_neu_ges > 0 and (select count(*) from schule.aufgabe x join bb1_p p on p.neu_id = x.id where p.zustand = 'neu' and x.freigegeben) <> n_neu_ges then fehler := fehler || 'Zahl der neuen gültigen Aufgaben stimmt nicht'::text; end if;
  if array_length(fehler, 1) > 0 then raise exception 'BB1 ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler[1:40], ' | '); end if;
  v_bericht := jsonb_build_object('paare', (select count(*) from bb1_p), 'neu_eingefuegt', n_neu_ges, 'alte_gesperrt', n_gesperrt, 'schon_berichtigt', n_fertig, 'zurueckgestellt', to_jsonb(zurueck),
    'regeln_neu', n_regel_neu, 'fehlbilder_neu', n_fb_neu, 'einheiten_geaendert', (select count(*) from bb1_e), 'sollantworten_richtig', n_soll_ok, 'fehlantworten_gueltig_und_falsch', n_fb_ok,
    'trigger', trg_nach, 'schreibzeilen_je_tabelle', audit, 'lernkarten_regeln_gleich', true, 'fingerabdruck_unberuehrter_zeilen_gleich', true, 'nf_s_vorhanden', true,
    'grenzen', 'xmin sieht keine Löschungen, Sequenzänderungen, externe Effekte, fremde Schemas, nicht zuverlässig Untertransaktionen; Trigger-Textsuche sieht delegierte/dynamische Schreibvorgänge nicht; kein Fingerabdruck für versuch/karte_stand (laufende Kinder-Aktivität); Mischkarte nach Verweisprüfung 2 nur durch Lernpause ausgeschlossen',
    'fehler', 0);
{ende}end $bb1$;
select count(*) filter (where freigegeben) as neu_gueltig, count(*) as neu_gesamt from schule.aufgabe where (einheit_id, reihenfolge) in ({', '.join(f"({p['e']}, {p['nr']})" for p in paare)});
"""


def uebersicht(paare):
    print(f'{len(paare)} Paare; Regeln {sum(1 for p in paare if p["regel"])}, Fehlbilder {sum(len(p["fb"]) for p in paare)}, Einheiten {len({p["e"] for p in paare})}')
    for p in paare:
        print(f'{p["bb"]:8} -> {p["kennung"]:10} Einheit {p["e"]:>3} Platz {p["nr"]:>6}  Vorrat {p["pool"]:9} {p["l"]:18} Vorgänger {p["alt_kennung"] or "(Themen-Aufgabe)":12} Platz alt {p["ar"]}')


def pakete(paare):
    return [('bestand_berichtigung1_probe.sql', paket(paare, True)), ('bestand_berichtigung1_einspielen.sql', paket(paare, False))]


def main():
    paare = daten()
    if '--abbildung' in sys.argv:
        print(json.dumps(abbildung(paare), ensure_ascii=False, indent=1)); return
    if '--sql' in sys.argv:
        print(paket(paare, '--probe' in sys.argv), end=''); return
    if '--pakete' in sys.argv:
        out = pakete(paare)
        for n, t in out:
            assert len(t.encode('utf-8')) < 1_500_000 and not re.search(r'^\s*\\', t, re.M) and not re.search(r'^\s*(begin|commit|rollback)\s*;', t, re.M | re.I), n
        if '--pruefen' in sys.argv:
            alt = [n for n, t in out if not (AUS / n).exists() or (AUS / n).read_text(encoding='utf-8') != t]
            if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
            print('OK'); return
        print('| Datei | Bytes | md5 |\n|---|---|---|')
        for n, t in out:
            (AUS / n).write_text(t, encoding='utf-8')
            print(f'| `tools/tests/aus/{n}` | {len(t.encode("utf-8"))} | `{md5(t)}` |')
        (BB / 'abbildung.json').write_text(json.dumps(abbildung(paare), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        return
    uebersicht(paare)


if __name__ == '__main__':
    main()
