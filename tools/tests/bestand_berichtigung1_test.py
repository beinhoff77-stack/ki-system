"""Test für das Einspiel-Paket Bestands-Berichtigung 1 (tools/bestand_berichtigung1_sql.py, tools/tests/aus/bestand_berichtigung1_*.sql).

Teil 1 (immer): Zuordnung BB1-… -> Kennung/Platz eindeutig und frei, 23 Paare, Pakete auf dem Stand (--pakete --pruefen), bestehende Pakete unberührt.
Teil 2 (nur mit lokalem Postgres): NACHBAU der Datenbank (wie regelbezug_sql_test.py, NICHT die echte), RB-S eingespielt, die drei Themen-Vorgänger über
  schule.aufgaben_einfuegen angelegt; dann: Probelauf rollt zurück; Einspielen (23 neu, 23 gesperrt, 14 Regeln, 69 Fehlbilder; Versuche/Karten/Sterne byteidentisch;
  Einheiten unverändert); zweiter Lauf = „schon berichtigt“, schreibt nichts; Negativfälle (nicht erkannt, Einheit nicht freigegeben, offener Verweis -> zurückgestellt
  und später nachgeholt, Zwischenstand, Trigger mit Nebenwirkung auf einheit); Gegenprobe mit verfälschtem Paket.
Aufruf: python3 -I tools/tests/bestand_berichtigung1_test.py   (endet mit OK; Teil 2 wird übersprungen, wenn kein Postgres da ist)
"""
import json
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import bestand_berichtigung1_sql as B  # noqa: E402
import regelbezug_sql_test as T  # noqa: E402
import regelbezug_sql as R  # noqa: E402

AUS = WURZEL / 'tools/tests/aus'
N = 23


def py(*args):
    p = subprocess.run([sys.executable, '-I', *args], capture_output=True, text=True, cwd=str(WURZEL))
    return p.returncode, p.stdout, p.stderr


def teil1():
    paare = B.daten()
    assert len(paare) == N
    ks = [p['kennung'] for p in paare]
    assert len(set(ks)) == N and not set(ks) & set(R.repo_eintraege()), 'Kennungen nicht eindeutig oder schon vergeben'
    plaetze = [(p['e'], p['nr']) for p in paare]
    assert len(set(plaetze)) == N
    aus, _ = R.eingespielt()
    assert not set(plaetze) & set(aus), 'Platz schon belegt'
    assert sum(1 for p in paare if p['regel']) == 14 and sum(len(p['fb']) for p in paare) == 69
    for p in paare:
        assert re.match(r'^[A-Z0-9]+-V\d{3}$', p['kennung'])
        assert p['row']['s'] == p['s'] and p['row']['l'] == p['l'] and p['row']['p'] == p['pool']
    # Tabellen: gedrehte Tabellen enthalten genau die Zellen der alten (Zeilenüberschriften der Kopfspalte dürfen gekürzt sein: nur T03)
    for p in paare:
        if not p['bb'].startswith('BB1-T'): continue
        go, gn = p['af']['grafik'], p['nf']['grafik']
        mo, mn = [go['kopf']] + go['zeilen'], [gn['kopf']] + gn['zeilen']
        tr = [list(r) for r in zip(*mo)]
        assert len(tr) == len(mn) and all(len(a) == len(b) for a, b in zip(tr, mn)), p['bb']
        if p['bb'] == 'BB1-T03':
            assert [r[1:] for r in tr[1:]] == [r[1:] for r in mn[1:]] or [r[0] for r in tr[1:]] == [r[0] for r in mn[1:]], p['bb']
            assert [r[0] for r in tr[1:]] == [r[0] for r in mn[1:]] and all(len(r) == len(mn[0]) for r in mn), p['bb']
        else:
            assert tr == mn, f'{p["bb"]}: Zellen der gedrehten Tabelle weichen ab'
        assert p['af']['text'] == p['nf']['text'] and p['ao'] == p['row']['o'], p['bb']
    rc, out, err = py('tools/bestand_berichtigung1_sql.py', '--pakete', '--pruefen')
    assert rc == 0, 'Pakete unter tools/tests/aus nicht auf dem Stand: python3 -I tools/bestand_berichtigung1_sql.py --pakete\n' + err
    einsp = (AUS / 'bestand_berichtigung1_einspielen.sql').read_text(encoding='utf-8')
    probe = (AUS / 'bestand_berichtigung1_probe.sql').read_text(encoding='utf-8')
    for t in (einsp, probe):
        assert not re.search(r'^\s*(begin|commit|rollback)\s*;', t, re.M | re.I) and not re.search(r'^\s*\\', t, re.M)
        assert t.startswith('-- Bestands-Berichtigung 1') and "set_config('lock_timeout', '3s', true)" in t and t.index('set_config') < t.index('do $bb1$')
    assert "raise exception 'PROBELAUF bestanden, ALLES zurückgerollt" in probe and 'PROBELAUF' not in einsp.split('do $bb1$')[1]
    abb = json.loads((B.BB / 'abbildung.json').read_text(encoding='utf-8'))
    assert [a['kennung_neu'] for a in abb['aufgaben']] == ks, 'abbildung.json nicht auf dem Stand'
    print('Teil 1: 23 Paare, Kennungen/Plätze frei und eindeutig, gedrehte Tabellen zellgleich, Pakete auf dem Stand')
    return paare


def sig(pg, tab):
    return pg.sql(f"\\pset tuples_only on\nselect md5(coalesce(string_agg(x::text, '|' order by x::text), '')) from schule.{tab} x;").strip()


def zahl(pg, sql):
    return int(pg.sql('\\pset tuples_only on\n' + sql).split()[0])


def aufbauen(pg, paare):
    pg.sql(T.nachbau_sql())
    pg.paket((AUS / 'rb_s_einspielen.sql').read_text(encoding='utf-8'))
    # Bausteine, die der Nachbau nicht hat (Definitionen aus den Migrationen bzw. minimal)
    kb = T.auszug('20261118_w150_f_stufen_typ_bonus.sql', 'create or replace function schule.aufgaben_einfuegen(', '$function$;\n')
    for alt, neu in (("reihenfolge, pool, typ)", "reihenfolge, pool, typ, form, zaehlt)"), ("x->>'g' from q", "x->>'g', x->>'form', x->>'zaehlt' from q")):
        assert kb.count(alt) == 1, alt
        kb = kb.replace(alt, neu)
    pg.sql(kb + """
create table schule.misch_ausgabe (id bigserial primary key, lernender_id bigint not null references schule.lernender(id), aufgabe_id bigint not null references schule.aufgabe(id),
  ausgegeben_am timestamptz not null default now(), eingeloest_am timestamptz, verfallen_am timestamptz);
create table schule.testsitzung (id bigserial primary key, lernender_id bigint, art text, einheit_id bigint, aufgaben bigint[], status text, abgeschlossen_am timestamptz);
alter table schule.aufgabe disable trigger aufgabe_schutz;
update schule.aufgabe a set thema_id = e.thema_id from schule.einheit e where e.id = a.einheit_id;
alter table schule.aufgabe enable trigger aufgabe_schutz;
""")
    # die drei Vorgänger ohne Kennung (inhalte/themen) wie im Bestand: über aufgaben_einfuegen
    for i, p in enumerate(x for x in paare if x['alt_kennung'] is None):
        d = json.loads((WURZEL / p['datei']).read_text(encoding='utf-8'))['aufgaben'][p['alt_idx']]
        row = {f: d[f] for f in B.FELDER if d.get(f) is not None}
        row['r'] = 5 + i
        pg.sql(f"select schule.aufgaben_einfuegen({p['e']}, $j${json.dumps([row], ensure_ascii=False)}$j$::jsonb);")
    assert zahl(pg, f"select count(*) from schule.aufgabe where freigegeben;") > 2000


def altid(p):
    return (f"(select id from schule.aufgabe where einheit_id = {p['e']} and pool = '{p['pool']}' and variante_gruppe = '{p['l']}' and frage = $j${json.dumps(p['af'], ensure_ascii=False)}$j$::jsonb)")


def teil2(paare):
    b = T.pg_bin()
    if not b:
        print('Teil 2 übersprungen (kein Postgres)'); return
    pg = T.PG(b)
    try:
        aufbauen(pg, paare)
        probe = (AUS / 'bestand_berichtigung1_probe.sql').read_text(encoding='utf-8')
        einsp = (AUS / 'bestand_berichtigung1_einspielen.sql').read_text(encoding='utf-8')
        p_b1 = next(p for p in paare if p['bb'] == 'BB1-B1')
        # Kind hat die alte Aufgabe schon beantwortet (Versuch, Karte, Sterne): bleiben unberührt
        pg.sql(f"select schule.uebung_pruefen_wd(2, jsonb_build_object('aufgabe_id', {altid(p_b1)}, 'client_id', 'bb1-t1', 'antwort', jsonb_build_object('wert', '280'), 'anlauf', 2));")
        assert zahl(pg, 'select count(*) from schule.versuch') == 1
        tabellen = ('versuch', 'karte_stand', 'sterne', 'lerntag', 'lernender', 'einheit', 'thema', 'regel')
        vor = {t: sig(pg, t) for t in tabellen}
        auf_vor = pg.sql("\\pset tuples_only on\nselect md5(string_agg(x::text, '|' order by id)) from schule.aufgabe x where id not in (select id from schule.aufgabe where false);").strip()
        n_auf, n_reg, n_fb = (zahl(pg, f'select count(*) from schule.{t}') for t in ('aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild'))

        def nichts_geaendert(was):
            assert zahl(pg, 'select count(*) from schule.aufgabe') == n_auf and zahl(pg, 'select count(*) from schule.aufgabe_regel') == n_reg \
                and zahl(pg, 'select count(*) from schule.aufgabe_fehlbild') == n_fb, was
            assert pg.sql("\\pset tuples_only on\nselect md5(string_agg(x::text, '|' order by id)) from schule.aufgabe x;").strip() == auf_vor, f'{was}: Aufgaben verändert'
            assert {t: sig(pg, t) for t in tabellen} == vor, f'{was}: Tabellen verändert'

        # --- Probelauf: Meldung mit Bericht, nichts bleibt
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert '"neu_eingefuegt": 23' in out and '"alte_gesperrt": 23' in out and '"regeln_neu": 14' in out and '"fehlbilder_neu": 69' in out, out[:1500]
        assert '"einheiten_geaendert": 18' in out and '"zurueckgestellt": []' in out and '"fehler": 0' in out, out[-1500:]
        nichts_geaendert('Probelauf')
        pg.sql(probe, erwartet_fehler='PROBELAUF bestanden')     # auch direkt (psql) lauffähig
        nichts_geaendert('Probelauf direkt')
        print('Probelauf: bestanden, zurückgerollt, Bericht 23 neu / 23 gesperrt / 14 Regeln / 69 Fehlbilder / 18 Einheiten')

        # --- Negativfälle (jeweils in EINER Transaktion mit Änderung; Abbruch rollt auch die Änderung zurück)
        zeile = paare[3]
        pg.sql("alter table schule.aufgabe disable trigger aufgabe_schutz;\n"
               f"update schule.aufgabe set loesung = loesung || '{{\"toleranz\": 0.5}}' where id = {altid(zeile)};\n" + f"do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;",
               erwartet_fehler='BB1 ABBRUCH')
        out = pg.sql("alter table schule.aufgabe disable trigger aufgabe_schutz;\n"
                     f"update schule.aufgabe set loesung = loesung || '{{\"toleranz\": 0.5}}' where id = {altid(zeile)};\n" + f"do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;",
                     erwartet_fehler='weder alte noch neue Aufgabe')
        assert zeile['bb'] in out
        nichts_geaendert('nicht erkannt')
        out = pg.sql("update schule.einheit set status = 'geprueft' where id = 11;\n" + f"do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;", erwartet_fehler='Einheit 11 ist nicht freigegeben')
        nichts_geaendert('Einheit nicht freigegeben')
        # Zwischenstand: neue Aufgabe von Hand eingefügt, alte noch gültig
        pg.sql(f"select schule.aufgaben_einfuegen({p_b1['e']}, $j${json.dumps([p_b1['row']], ensure_ascii=False)}$j$::jsonb);\n" + f"do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;",
               erwartet_fehler='beide gültig')
        nichts_geaendert('Zwischenstand')
        # Trigger mit Nebenwirkung auf einheit (a: sichtbar im Text, b: versteckt in einer Hilfsfunktion, c: ändert die Einheitszeile)
        tg = ("create function schule.t_a() returns trigger language plpgsql as $$ begin insert into schule.sterne (lernender_id, menge, grund, bezug) values (1, 1, 'x', 'y'); return new; end $$;\n"
              "create trigger t_a after update of status on schule.einheit for each row execute function schule.t_a();\n")
        pg.sql(tg + f"do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;", erwartet_fehler='schreibt oder meldet')
        tg = ("create function schule.hilf() returns void language plpgsql as $$ begin execute 'insert into schule.' || 'sterne (lernender_id, menge, grund, bezug) values (1, 1, ''x'', ''y'') on conflict do nothing'; end $$;\n"
              "create function schule.t_b() returns trigger language plpgsql as $$ begin perform schule.hilf(); return new; end $$;\n"
              "create trigger t_b after update of status on schule.einheit for each row execute function schule.t_b();\n")
        pg.sql(tg + f"do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;", erwartet_fehler='Tabelle schule.sterne')
        tg = ("alter table schule.einheit add column geaendert timestamptz;\n"
              "create function schule.t_c() returns trigger language plpgsql as $$ begin new.geaendert := clock_timestamp(); return new; end $$;\n"
              "create trigger t_c before update on schule.einheit for each row execute function schule.t_c();\n")
        out = pg.sql(tg + f"do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;", erwartet_fehler='durch den Statuswechsel verändert')
        nichts_geaendert('Trigger mit Nebenwirkung')
        print('Negativfälle: nicht erkannt / Einheit nicht freigegeben / Zwischenstand / drei Trigger mit Nebenwirkung -> Abbruch, nichts geblieben')

        # --- Gegenproben mit verfälschtem Paket (das Paket selbst ist die geprüfte Sache)
        # Fehlbild-Wert gleich der Lösung -> wird nicht als falsch bewertet -> Abbruch
        schlecht = einsp.replace('"wert": "1000"', '"wert": "1"', 1)
        assert schlecht != einsp
        pg.paket(schlecht, erwartet_fehler='BB1 ABBRUCH')
        nichts_geaendert('verfälschtes Paket (Fehlbild = Lösung)')
        i = einsp.index("('BB1-B1'")
        zeile_b1 = einsp[i:einsp.index('\n', i)]
        ao = '$bbj$' + json.dumps(p_b1['ao'], ensure_ascii=False) + '$bbj$::jsonb'
        assert zeile_b1.count(ao) >= 1
        schlecht = einsp.replace(zeile_b1, zeile_b1.replace(ao, '$bbj$' + json.dumps({'wert': 123456}) + '$bbj$::jsonb', 1), 1)   # alte Lösung im Paket verfälscht
        assert schlecht != einsp
        pg.paket(schlecht, erwartet_fehler='weder alte noch neue Aufgabe')
        nichts_geaendert('verfälschtes Paket (alte Lösung)')
        print('Gegenproben mit verfälschtem Paket: Abbruch, nichts geblieben')

        # --- Offener Verweis: Mischkarte auf die alte Aufgabe von BB1-B1 und eine laufende Testsitzung mit der alten Aufgabe von BB1-T01 -> beide zurückgestellt
        p_t1 = next(p for p in paare if p['bb'] == 'BB1-T01')
        p_t2 = next(p for p in paare if p['bb'] == 'BB1-T02')
        offen = (f"insert into schule.misch_ausgabe (lernender_id, aufgabe_id) values (2, {altid(p_b1)});\n"
                 f"insert into schule.testsitzung (lernender_id, art, einheit_id, aufgaben, status) values (2, 'nachtest', {p_t1['e']}, array[{altid(p_t1)}], 'laeuft');\n"
                 f"insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, anlauf) values (2, {altid(p_t2)}, 'offen1', '{{}}', false, 1);\n")
        pg.sql(offen)       # eigene Transaktion: die Schreib-Prüfung des Pakets darf fremde Zeilen derselben Transaktion nicht mitzählen
        vor.update({t: sig(pg, t) for t in ('versuch',)})
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        for bb, was in (('BB1-B1', 'offene Mischkarte'), ('BB1-T01', 'laufende Testsitzung'), ('BB1-T02', 'falscher 1. Anlauf')):
            assert bb in out and was in out, (bb, out[-1800:])
        assert '"neu_eingefuegt": 20' in out and '"alte_gesperrt": 20' in out, out[:1600]
        nichts_geaendert('Probelauf mit offenen Verweisen')
        # wirklich einspielen, mit den offenen Verweisen: 20 Paare, 3 bleiben unberührt (alte gültig, neue fehlt)
        vor2 = {t: sig(pg, t) for t in ('karte_stand', 'sterne', 'lerntag')}
        out = pg.paket(einsp)
        assert 'BB1 eingespielt' in out and '"neu_eingefuegt": 20' in out and '"alte_gesperrt": 20' in out, out[-1500:]
        for p in (p_b1, p_t1, p_t2):
            assert zahl(pg, f"select count(*) from schule.aufgabe where id = {altid(p)} and freigegeben") == 1, p['bb']
            assert zahl(pg, f"select count(*) from schule.aufgabe where einheit_id = {p['e']} and reihenfolge = {p['nr']}") == 0, p['bb']
        assert zahl(pg, 'select count(*) from schule.aufgabe where freigegeben and reihenfolge > 90000') == 20
        # zweiter Lauf mit noch offenen Verweisen: nichts zu tun außer weiter zurückstellen
        out = pg.paket(einsp)
        assert '"neu_eingefuegt": 0' in out and '"schon_berichtigt": 20' in out and 'BB1-B1' in out, out[-1500:]
        # Verweise erledigt (Mischkarte eingelöst, Test abgeschlossen, zweiter Versuch gemacht) -> Nachholen
        pg.sql("update schule.misch_ausgabe set eingeloest_am = now();\nupdate schule.testsitzung set status = 'abgeschlossen', abgeschlossen_am = now();\n"
               f"insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, anlauf) values (2, {altid(p_t2)}, 'offen2', '{{}}', false, 2);")
        out = pg.paket(einsp)
        assert '"neu_eingefuegt": 3' in out and '"alte_gesperrt": 3' in out and '"schon_berichtigt": 20' in out and '"zurueckgestellt": []' in out, out[-1500:]
        print('Offene Verweise: 3 Paare zurückgestellt (unberührt), 20 berichtigt; später nachgeholt (3), zweiter Lauf dazwischen ohne Änderung')
        # Der Versuch auf die alte Aufgabe von BB1-B1 und die Karte sind unverändert (nur die Versuche aus diesem Test kamen hinzu)
        assert zahl(pg, "select count(*) from schule.versuch where client_id = 'bb1-t1'") == 1

        # --- Frischer Lauf auf frischem Bestand: Einspielen in einem Zug, dann zweiter Lauf
        pg.ende()
        pg = T.PG(b)
        aufbauen(pg, paare)
        pg.sql(f"select schule.uebung_pruefen_wd(2, jsonb_build_object('aufgabe_id', {altid(p_b1)}, 'client_id', 'bb1-t1', 'antwort', jsonb_build_object('wert', '280'), 'anlauf', 2));")
        vor = {t: sig(pg, t) for t in tabellen}
        n_frei_vor = zahl(pg, 'select count(*) from schule.aufgabe where freigegeben')
        out = pg.paket(einsp)
        assert 'BB1 eingespielt' in out and '"neu_eingefuegt": 23' in out and '"alte_gesperrt": 23' in out and '"schon_berichtigt": 0' in out, out[-1500:]
        assert zahl(pg, 'select count(*) from schule.aufgabe where freigegeben') == n_frei_vor, 'freigegebene Aufgaben insgesamt: 23 neu, 23 gesperrt = gleich viele'
        assert zahl(pg, 'select count(*) from schule.aufgabe where not freigegeben') == N
        assert zahl(pg, 'select count(*) from schule.aufgabe where freigegeben and reihenfolge > 90000') == N
        assert zahl(pg, 'select count(*) from schule.aufgabe_regel') == n_reg + 14 and zahl(pg, 'select count(*) from schule.aufgabe_fehlbild') == n_fb + 69
        assert {t: sig(pg, t) for t in tabellen} == vor, 'Versuche/Karten/Sterne/Einheiten/Lernende nach dem Einspielen verändert'
        assert zahl(pg, "select count(*) from schule.einheit where status <> 'freigegeben'") == 0
        for p in paare:
            nid = f"(select id from schule.aufgabe where einheit_id = {p['e']} and reihenfolge = {p['nr']})"
            assert zahl(pg, f"select count(*) from schule.aufgabe_fehlbild where aufgabe_id = {nid}") == len(p['fb']), p['bb']
            assert zahl(pg, f"select count(*) from schule.aufgabe_regel where aufgabe_id = {nid}") == (1 if p['regel'] else 0), p['bb']
            assert zahl(pg, f"select count(*) from schule.aufgabe where id = {altid(p)} and not freigegeben") == 1, p['bb']
        # Die alte Aufgabe wird mit offenem Weg weiter bewertet (in-flight-Antwort), das Kind verliert nichts
        out = pg.sql(f"\\pset tuples_only on\nselect schule.uebung_pruefen_wd(2, jsonb_build_object('aufgabe_id', {altid(p_b1)}, 'client_id', 'bb1-t2', 'antwort', jsonb_build_object('wert', '" + str(p_b1['ao']['wert']) + "'), 'anlauf', 2))->>'richtig';")
        assert 'true' in out, out
        nach_einsp = {t: sig(pg, t) for t in ('aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild', 'einheit')}
        out = pg.paket(einsp)
        assert 'BB1 eingespielt' in out and '"neu_eingefuegt": 0' in out and '"alte_gesperrt": 0' in out and '"schon_berichtigt": 23' in out, out[-1500:]
        assert {t: sig(pg, t) for t in nach_einsp} == nach_einsp, 'zweiter Lauf hat etwas verändert'
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert '"schon_berichtigt": 23' in out
        print('Einspielen: 23 neu, 23 gesperrt, 14 Regeln, 69 Fehlbilder; Versuche/Karten/Sterne/Lernende/Einheiten byteidentisch; zweiter Lauf: 23 schon berichtigt, nichts geändert')
        print('Teil 2 (lokaler Nachbau) bestanden')
    finally:
        pg.ende()


def main():
    paare = teil1()
    teil2(paare)
    print('OK')


if __name__ == '__main__':
    main()
