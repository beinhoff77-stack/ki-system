"""Test für NF-S (Nachtest nur mit freigegebenen Aufgaben): tools/tests/nf_einspielen.py, Migration 20261208_nf_s_nachtest_freigegeben.sql, Pakete tools/tests/aus/nf_s_*.sql.

Gegenstand: nachtest_auswahl, nachtest_stand, test_starten_intern (erster Flugtest pool 'test', Korrektur-Zweig pool 'korrektur').
Teil 1 (immer): Pakete und Migration auf dem Stand (--pruefen), Migration = Einspiel-Datei byteidentisch, neue Funktionstexte unterscheiden sich vom alten Text
  nur um genau die eine Bedingung „and a.freigegeben“, Hash-Pins stimmen.
Teil 2 (nur mit lokalem Postgres, NACHBAU, NICHT die echte Datenbank): ALTE Funktionen mit den Live-Eigenschaften; Probelauf rollt zurück; Einspielen; zweiter Lauf („neu -> neu“);
  Verhalten: neu gestarteter Nachtest zieht nie eine gesperrte ID, die Vorratsanzeige zählt die Ersatzaufgabe genau einmal, eine bestehende Sitzung mit der alten ID bleibt unberührt;
  alle anderen Funktionen des Schemas unverändert; Gegenprobe (Reihenfolge der Auswahl verändert -> Abbruch); Negativfälle (abweichender Funktionstext, STRICT, VOLATILE, SECURITY DEFINER je Funktion).
Aufruf: python3 -I tools/tests/nf_s_test.py   (endet mit OK; Teil 2 wird übersprungen, wenn kein Postgres da ist)
"""
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import nf_einspielen as NF  # noqa: E402
import nf_nachbau as NB  # noqa: E402
import nf_probe2 as P2  # noqa: E402
import regelbezug_sql_test as T  # noqa: E402

AUS = WURZEL / 'tools/tests/aus'


def zahl(pg, sql):
    return int(pg.sql('\\pset tuples_only on\n' + sql).strip())


def text(pg, sql):
    return pg.sql('\\pset tuples_only on\n\\pset format unaligned\n' + sql).strip()


def teil1():
    p = subprocess.run([sys.executable, '-I', 'tools/tests/nf_einspielen.py', '--pruefen'], capture_output=True, text=True, cwd=str(WURZEL))
    assert p.returncode == 0, p.stderr
    probe = (AUS / 'nf_s_probe.sql').read_text(encoding='utf-8')
    einsp = (AUS / 'nf_s_einspielen.sql').read_text(encoding='utf-8')
    assert NF.MIGRATION.read_text(encoding='utf-8') == einsp
    p = subprocess.run([sys.executable, '-I', 'tools/tests/nf_probe2.py', '--pruefen'], capture_output=True, text=True, cwd=str(WURZEL))
    assert p.returncode == 0, p.stderr
    assert (AUS / 'nf_s_probe2.sql').read_text(encoding='utf-8').count('PROBELAUF2 bestanden') == 1
    assert 'PROBELAUF bestanden' in probe and 'PROBELAUF' not in einsp and 'NF-S eingespielt' in einsp
    assert not re.search(r'(?im)^\s*(begin|commit|rollback)\s*;', einsp + probe), 'kein BEGIN/COMMIT im Paket'
    a_alt, a_neu, s_alt, s_neu = NF.auswahl_alt(), NF.auswahl_neu(), NF.stand_alt(), NF.stand_neu()
    assert a_neu.replace(' and a.freigegeben)', ')') == a_alt and a_neu.count('a.freigegeben') == 1
    assert s_neu.replace(' and a.freigegeben\n', '\n') == s_alt and s_neu.count('a.freigegeben') == 1
    t_alt, t_neu = NF.tsi_alt(), NF.tsi_neu()
    assert t_neu.replace("'test' and a.freigegeben;", "'test';").replace("'korrektur' and a.freigegeben\n", "'korrektur'\n") == t_alt and t_neu.count('a.freigegeben') == 3, 'test_starten_intern: genau zwei Bedingungen ergänzt (plus die schon vorhandene)'
    assert NF.md5(t_alt) == 'b226ac94131e47a507462e9be303ef8f' and len(t_alt) == 6739 and NF.md5(t_neu) in einsp and NF.md5(t_neu) in probe
    assert NF.md5(a_alt) == 'f25fab1c1599d980752c87b6849d557f' and len(a_alt) == 1109 and NF.md5(s_alt) == 'e73af9b462d741de80d4932d8fa7a38a' and len(s_alt) == 3778
    for m in (NF.md5(a_neu), NF.md5(s_neu)):
        assert m in einsp and m in probe
    print('Teil 1 bestanden: Pakete auf dem Stand, Migration = Einspiel-Datei, je Funktion genau eine Bedingung ergänzt, alte md5/Längen wie live')
    return probe, einsp


def aufbauen():
    b = T.pg_bin()
    pg = T.PG(b)
    pg.sql(T.nachbau_sql() + NB.nachtest_sql())
    return pg


def daten(pg):
    """Zwei Einheiten, drei Lernziele, je 6/6/4 Sicherungsaufgaben (alle freigegeben); Kind 2 hat einige gestellt (Versuch bzw. Testsitzung)."""
    e1, e2 = (int(x) for x in text(pg, 'select string_agg(id::text, \' \' order by id) from (select id from schule.einheit order by id limit 2) z;').split())
    sql = []
    for e, lz, n in ((e1, 'nfA', 6), (e1, 'nfB', 6), (e2, 'nfC', 4)):
        for i in range(1, n + 1):
            sql.append(f"insert into schule.aufgabe (einheit_id, variante_gruppe, antworttyp, frage, loesung, reihenfolge, pool, typ) values ({e}, '{lz}', 'zahl', '{{\"text\": \"{lz} {i}\"}}', '{{\"wert\": {i}}}', {100 + i}, 'sicherung', 'einkleidung');")
    sql.append("insert into schule.lernender (ist_test) values (false), (false);")        # Kind 3 (Korrektur-Fälle), Kind 4 (laufender Flugtest)
    for e, lz, pool, n, ab in ((e1, 'nfA', 'test', 3, 201), (e1, 'nfB', 'test', 2, 201), (e2, 'nfC', 'test', 2, 201), (e1, 'nfA', 'korrektur', 3, 301), (e1, 'nfB', 'korrektur', 2, 301), (e2, 'nfC', 'korrektur', 1, 301)):
        for i in range(n):
            sql.append(f"insert into schule.aufgabe (einheit_id, variante_gruppe, antworttyp, frage, loesung, reihenfolge, pool, typ) values ({e}, '{lz}', 'zahl', '{{\"text\": \"{pool} {lz} {i}\"}}', '{{\"wert\": {i}}}', {ab + i}, '{pool}', 'einkleidung');")
    sql.append(f"insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, status) values (3, {e1}, 'nfA', 'fehler'), (3, {e1}, 'nfB', 'nachgewiesen');")
    for l in (1, 2):
        for e, lz, st in ((e1, 'nfA', 'gesichert'), (e1, 'nfB', 'wacklig'), (e2, 'nfC', 'wacklig')):
            sql.append(f"insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, status) values ({l}, {e}, '{lz}', '{st}');")
    sql.append(f"insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, anlauf, am) select 2, id, 'nf-' || id, '{{}}', true, 1, now() - (id || ' hours')::interval "
               f"from schule.aufgabe where pool = 'sicherung' and reihenfolge in (101, 103) and einheit_id = {e1};")
    sql.append(f"insert into schule.testsitzung (lernender_id, art, einheit_id, aufgaben, status) select 2, 'nachtest', {e1}, array_agg(id), 'laeuft' from schule.aufgabe "
               f"where pool = 'sicherung' and reihenfolge = 105 and einheit_id = {e1} and variante_gruppe = 'nfB';")
    pg.sql('\n'.join(sql))
    return e1, e2


def sperren(pg, e, lz, nr, pool='sicherung'):
    pg.sql("alter table schule.aufgabe disable trigger aufgabe_schutz;\n"
           f"update schule.aufgabe set freigegeben = false where einheit_id = {e} and variante_gruppe = '{lz}' and pool = '{pool}' and reihenfolge = {nr};\n"
           "alter table schule.aufgabe enable trigger aufgabe_schutz;")
    return int(text(pg, f"select id from schule.aufgabe where einheit_id = {e} and variante_gruppe = '{lz}' and pool = '{pool}' and reihenfolge = {nr};"))


def starten(pg, l, e, art, behalten=False):
    """Startet über test_starten_intern; ohne behalten wird die Transaktion zurückgerollt. Rückgabe (grund, ids|None)."""
    out = pg.sql("\\pset tuples_only on\n\\pset format unaligned\n"
                 f"select 'GRUND=' || coalesce((schule.test_starten_intern({l}, jsonb_build_object('einheit_id', {e}, 'art', '{art}')))->>'grund', 'ok');\n"
                 f"select 'IDS=' || coalesce((select aufgaben::text from schule.testsitzung where lernender_id = {l} and einheit_id = {e} and art = '{art}' order by id desc limit 1), 'keine');"
                 + ('' if behalten else "\nrollback;"))
    g = re.search(r'GRUND=(\w+)', out).group(1)
    i = re.search(r'IDS=(\{[\d,]*\}|keine)', out).group(1)
    return g, (None if i == 'keine' else [int(x) for x in i.strip('{}').split(',') if x])


def zustand(pg):
    """prosrc-md5 + Eigenschaften der beiden Funktionen und md5 über ALLE anderen Funktionen des Schemas schule (Text + Eigenschaften)."""
    z = text(pg, "select concat(p.proname, ' ', md5(p.prosrc), ' ', p.provolatile, p.prosecdef::text, p.proisstrict::text, coalesce(p.proconfig::text, '')) from pg_proc p join pg_namespace n on n.oid = p.pronamespace "
                 "where n.nspname = 'schule' and p.proname in ('nachtest_auswahl', 'nachtest_stand', 'test_starten_intern') order by 1;")
    rest = text(pg, "select md5(string_agg(concat(p.oid::regprocedure::text, md5(p.prosrc), p.provolatile, p.prosecdef::text, p.proisstrict::text, coalesce(p.proconfig::text, ''), coalesce(p.proacl::text, '')), '|' order by p.oid::regprocedure::text)) "
                    "from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule' and p.proname not in ('nachtest_auswahl', 'nachtest_stand', 'test_starten_intern');")
    return z, rest


def teil2(probe, einsp):
    if not T.pg_bin():
        print('Teil 2 übersprungen (kein Postgres)'); return
    pg = aufbauen()
    try:
        e1, e2 = daten(pg)
        z0, rest0 = zustand(pg)
        assert f"nachtest_auswahl {NF.AUSWAHL_ALT_MD5} s" in z0 and f"nachtest_stand {NF.STAND_ALT_MD5} s" in z0 and f"test_starten_intern {NF.TSI_ALT_MD5} vfalsefalse" in z0, z0      # Nachbau = Live-Texte, STABLE/Invoker/nicht STRICT/search_path
        # --- Ausgangslage OHNE gesperrte Sicherungsaufgaben: Vergleich vorher = nachher überall
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert '"nachtest_auswahl": "alt -> neu"' in out and '"nachtest_stand": "alt -> neu"' in out and '"abweichend_gesamt": 0' in out and '"abweichend_unerwartet": 0' in out, out[-1500:]
        assert '"gesperrte_sicherungsaufgaben_live": 0' in out and '"eigenschaften_gleich": true' in out, out[-1500:]
        assert zustand(pg) == (z0, rest0), 'Probelauf hat etwas zurückgelassen'
        pg.sql(probe, erwartet_fehler='PROBELAUF bestanden')     # auch direkt (psql)
        assert zustand(pg) == (z0, rest0)
        print('Probelauf (ohne gesperrte Aufgaben): bestanden, zurückgerollt, alle Fälle vorher = nachher')

        # --- Mit einer gesperrten Sicherungsaufgabe je Lernziel nfA (Kind 2 hat sie nicht gestellt) und einer in nfB (die in der laufenden Sitzung steckt)
        l_a = sperren(pg, e1, 'nfA', 102)
        l_b = sperren(pg, e1, 'nfB', 105)
        l_c = sperren(pg, e2, 'nfC', 101)
        t_a = sperren(pg, e1, 'nfA', 202, 'test')                                    # ein Test-Auftrag in e1 gesperrt -> Flugtest wird kürzer
        for r_ in (201, 202): sperren(pg, e2, 'nfC', r_, 'test')                      # ALLE Test-Aufgaben von e2 gesperrt -> nichts_zu_testen
        k_a = sperren(pg, e1, 'nfA', 301, 'korrektur')                                # erste Korrektur-Aufgabe von nfA gesperrt
        k_c = sperren(pg, e2, 'nfC', 301, 'korrektur')                                # einziges Korrektur-Aufgabe von nfC gesperrt
        # ALT (Mangel): gesperrte IDs werden gezogen; Kind 4 bekommt eine laufende Sitzung mit der gesperrten ID
        g, ids = starten(pg, 1, e1, 'blocktest'); assert g == 'ok' and t_a in ids and len(ids) == 5, (g, ids)
        g, ids = starten(pg, 1, e2, 'blocktest'); assert g == 'ok' and len(ids) == 2, (g, ids)
        g, ids = starten(pg, 3, e1, 'korrektur'); assert g == 'ok' and ids == [k_a], (g, ids, k_a)
        g, sitz_alt = starten(pg, 4, e1, 'blocktest', behalten=True); assert t_a in sitz_alt
        ersatz = pg.sql(f"insert into schule.aufgabe (einheit_id, variante_gruppe, antworttyp, frage, loesung, reihenfolge, pool, typ) values ({e2}, 'nfC', 'zahl', '{{\"text\": \"Ersatz\"}}', '{{\"wert\": 1}}', 90101, 'sicherung', 'einkleidung');")
        # Vorher (ALT): gesperrte Aufgaben sind im Vorrat und werden gezogen -> der Mangel
        def ziehen(l, e, lz, n): return [int(x) for x in text(pg, f"select unnest(schule.nachtest_auswahl({l}, {e}, '{lz}', {n}));").split()]
        gezogen_alt = {n: ziehen(1, e1, 'nfA', n) for n in range(1, 7)}
        assert any(l_a in v for v in gezogen_alt.values()), 'Ausgangslage: die gesperrte ID wird im alten Stand gezogen'
        vorrat_alt = text(pg, f"select schule.nachtest_stand(1, {e2})->>'vorrat_runden';")
        je2 = zahl(pg, f"select schule.nachtest_je_etappe(count(*)::int) from schule.lernziel_stand where lernender_id = 1 and einheit_id = {e2};")
        assert vorrat_alt == str(5 // max(je2, 1)), (vorrat_alt, je2)       # alt: 4 alte (davon 1 gesperrt) + 1 Ersatz = 5 gezählt
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert f'"flugtest_einheiten_nichts_zu_testen_ids": [{e2}]' in out and '"flugtest_einheiten_nichts_zu_testen": 1' in out and '"flugtest_einheiten_gekuerzt": 1' in out, out[:2500]
        assert '"korrektur_faelle_andere_aufgabe_neu": 1' in out and '"korrektur_faelle_vorrat_leer_neu": 0' in out and '"korrektur_lernziele_ohne_freigegebene_aufgabe_durch_sperre": 1' in out, out[:2500]
        assert '"davon_neu_durch_sperre": 1' in out and '"test_starten_intern": "alt -> neu"' in out, out[:2500]
        assert '"abweichend_unerwartet": 0' in out and '"gesperrte_sicherungsaufgaben_live": 3' in out and '"abweichend_wegen_gesperrter_sicherungsaufgaben": 0' not in out, out[-1500:]
        assert zustand(pg) == (z0, rest0)
        print('Probelauf (3 gesperrte Aufgaben): bestanden; Abweichungen nur in Einheiten mit gesperrter Sicherungsaufgabe (gezählt, kein Abbruch)')

        # --- Probe 2 (Härtung, zusätzliche Datei): im Zustand ALT; Zahlen merken
        probe2 = (AUS / 'nf_s_probe2.sql').read_text(encoding='utf-8')
        out = pg.paket(probe2, erwartet_fehler='PROBELAUF2 bestanden')
        assert '"zustand": {"stand": "alt", "auswahl": "alt", "test_starten_intern": "alt"}' in out and '"unerwartet": 0' in out and '"fehler": 0' in out, out[-900:]
        erlaubt_alt = re.search(r'"erlaubt_wegen_gesperrter_sicherungsaufgaben": (\d+)', out).group(1)
        assert int(erlaubt_alt) > 0
        assert zustand(pg) == (z0, rest0)
        # Fehler werden getrennt gezählt und brechen ab (hier: Tabelle versuch fehlt in der Transaktion)
        pg.sql("alter table schule.versuch rename to versuch_x;\n" + f"do $nfx$ begin execute $nfxinhalt${probe2}$nfxinhalt$; end $nfx$;", erwartet_fehler='NF-S PROBE2 ABBRUCH: ')
        # --- Gegenprobe: Reihenfolge der Auswahl verändert -> unerwartete Abweichung in einer Einheit OHNE gesperrte Aufgabe -> Abbruch, alles zurück
        pg2 = aufbauen()
        try:
            daten(pg2)
            z2, r2 = zustand(pg2)
            bad = NF.paket(False, auswahl_variante='order by a.gestellt desc, a.zuletzt desc nulls last')
            out = pg2.paket(bad, erwartet_fehler='NF-S ABBRUCH, alles zurückgerollt')
            assert 'ändern sich, obwohl in der Einheit keine Sicherungs-Aufgabe gesperrt ist' in out
            assert zustand(pg2) == (z2, r2)
        finally:
            pg2.ende()
        print('Gegenprobe mit verändertem Auswahltext: Abbruch, nichts geblieben')

        # --- Einspielen
        out = pg.paket(einsp)
        assert 'NF-S eingespielt' in out and '"nachtest_auswahl": "alt -> neu"' in out and '"abweichend_unerwartet": 0' in out, out[-1500:]
        z1, rest1 = zustand(pg)
        assert z1.count(' s') >= 0 and NF.md5(NF.auswahl_neu()) in z1 and NF.md5(NF.stand_neu()) in z1
        assert re.findall(r'(nachtest_\w+) \w{32} (\S+)', z1) == re.findall(r'(nachtest_\w+) \w{32} (\S+)', z0), 'Eigenschaften verändert'
        assert rest1 == rest0, 'andere Funktionen des Schemas verändert'
        # Probe 2 im Zustand NEU: vergleicht trotzdem (alte Kopie gegen lebende Funktion) – gleiche erlaubte Abweichungen wie vorher
        out = pg.paket(probe2, erwartet_fehler='PROBELAUF2 bestanden')
        assert '"zustand": {"stand": "neu", "auswahl": "neu", "test_starten_intern": "neu"}' in out and '"unerwartet": 0' in out, out[-900:]
        assert re.search(r'"erlaubt_wegen_gesperrter_sicherungsaufgaben": (\d+)', out).group(1) == erlaubt_alt
        # eine veränderte lebende Funktion (Reihenfolge der Auswahl) -> Probe 2 bricht ab (Text weder alt noch neu)
        pg.sql("create or replace function schule.nachtest_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int) returns bigint[] language sql stable set search_path to '' as $f$"
               + NF.auswahl_neu('order by a.gestellt desc, a.zuletzt desc nulls last') + "$f$;\n" + f"do $nfx$ begin execute $nfxinhalt${probe2}$nfxinhalt$; end $nfx$;", erwartet_fehler='weder alt noch neu')
        # zweiter Lauf: neu -> neu, nichts zu tun
        out = pg.paket(einsp)
        assert '"nachtest_auswahl": "neu -> neu"' in out and '"nachtest_stand": "neu -> neu"' in out and '"verglichen_auswahl": 0' in out, out[-1200:]
        assert zustand(pg) == (z1, rest1)
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert 'neu -> neu' in out
        print('Probe 2 (zusätzliche Datei): im Zustand alt und neu gleiche erlaubte Abweichungen; Fehler getrennt gezählt (Abbruch); veränderte Funktion -> Abbruch')
        print('Einspielen: beide Funktionen neu, Eigenschaften gleich, andere Funktionen unverändert; zweiter Lauf neu -> neu ohne Änderung')

        # --- Verhalten NEU
        for l in (1, 2):
            for lz, e in (('nfA', e1), ('nfB', e1), ('nfC', e2)):
                for n in range(1, 7):
                    z = ziehen(l, e, lz, n)
                    assert not (set(z) & {l_a, l_b, l_c}), (l, lz, n, z)
        assert ziehen(1, e1, 'nfA', 5) and len(ziehen(1, e1, 'nfA', 5)) == 5 and ziehen(1, e1, 'nfA', 6) == [], 'nfA: 5 freigegebene -> 5 ja, 6 nein (nie verkürzt)'
        # Vorrat: Einheit 2 hat 3 alte freigegebene + 1 gesperrte + 1 Ersatz -> gezählt werden 4 (die Ersatzaufgabe genau einmal, die gesperrte gar nicht)
        vorrat_neu = text(pg, f"select schule.nachtest_stand(1, {e2})->>'vorrat_runden';")
        assert vorrat_neu == str(4 // max(je2, 1)), (vorrat_neu, je2)
        assert vorrat_neu != vorrat_alt or je2 > 1, 'Zählung hat sich nicht geändert'
        # laufende Sitzung mit der gesperrten ID aus nfB: bleibt unberührt, die ID gilt für Kind 2 weiter als gestellt (nicht im Vorrat, nicht in der Auswahl)
        assert zahl(pg, f"select count(*) from schule.testsitzung where {l_b} = any(aufgaben) and status = 'laeuft'") == 1
        assert zahl(pg, f"select count(*) from schule.aufgabe where id = {l_b} and not freigegeben") == 1
        assert zahl(pg, f"select count(*) from schule.aufgabe a where a.pool = 'sicherung' and a.freigegeben and a.id in ({l_a}, {l_b}, {l_c})") == 0
        # test_starten_intern: neue Sitzungen ziehen keine gesperrte ID; alles gesperrt -> nichts_zu_testen; laufende Sitzung bleibt
        g, ids = starten(pg, 1, e1, 'blocktest'); assert g == 'ok' and t_a not in ids and len(ids) == 4, (g, ids)
        g, ids = starten(pg, 1, e2, 'blocktest'); assert g == 'nichts_zu_testen' and ids is None, (g, ids)
        g, ids = starten(pg, 3, e1, 'korrektur'); assert g == 'ok' and ids and k_a not in ids and len(ids) == 1, (g, ids)
        g, ids = starten(pg, 3, e1, 'korrektur'); assert ids == starten(pg, 3, e1, 'korrektur')[1]
        g, sitz_neu = starten(pg, 4, e1, 'blocktest'); assert sitz_neu == sitz_alt and t_a in sitz_neu, (sitz_alt, sitz_neu)
        assert zahl(pg, "select count(*) from schule.testsitzung where lernender_id = 4 and art = 'blocktest'") == 1
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden'); assert '"test_starten_intern": "neu -> neu"' in out
        print('Flugtest/Korrektur: neue Sitzungen ziehen nie eine gesperrte ID (Flugtest 5 -> 4 Aufgaben), alles gesperrt -> nichts_zu_testen, laufende Sitzung mit gesperrter ID unverändert')
        print('Verhalten: neue Nachtests ziehen nie eine gesperrte ID (Kinder 1/2 × 3 Lernziele × Mengen 1-6); Vorrat zählt die Ersatzaufgabe genau einmal; laufende Sitzung mit alter ID unberührt')
    finally:
        pg.ende()

    # --- Negativfälle: jeweils frischer Nachbau, Änderung + Paket in EINER Transaktion; Abbruch rollt auch die Änderung zurück
    pg = aufbauen()
    try:
        daten(pg)
        z0, rest0 = zustand(pg)
        faelle = []
        for fn, sig_ in (('nachtest_auswahl', 'bigint, bigint, text, integer'), ('nachtest_stand', 'bigint, bigint')):
            faelle += [(fn, f'alter function schule.{fn}({sig_}) strict;', 'Eigenschaften'),
                       (fn, f'alter function schule.{fn}({sig_}) volatile;', 'Eigenschaften'),
                       (fn, f'alter function schule.{fn}({sig_}) security definer;', 'Eigenschaften')]
        faelle += [('test_starten_intern', 'alter function schule.test_starten_intern(bigint, jsonb) strict;', 'Eigenschaften'),
                   ('test_starten_intern', 'alter function schule.test_starten_intern(bigint, jsonb) stable;', 'Eigenschaften'),
                   ('test_starten_intern', 'alter function schule.test_starten_intern(bigint, jsonb) security definer;', 'Eigenschaften'),
                   ('test_starten_intern', "create or replace function schule.test_starten_intern(p_lernender bigint, p_daten jsonb) returns jsonb language plpgsql set search_path to '' as $f$"
                    + NF.tsi_alt().replace('begin', 'begin /* abweichend */', 1) + "$f$;", 'weicht vom Repo-Stand ab')]
        # abweichender Funktionstext (je Funktion): alte Fassung mit zusätzlichem Kommentar
        pg.sql("create table pg_temp.dummy(x int);")
        for fn, rueck, kopf, body in (('nachtest_auswahl', 'bigint[]', 'p_l bigint, p_e bigint, p_lz text, p_anzahl int', NF.auswahl_alt() + ' -- abweichend\n'),
                                      ('nachtest_stand', 'jsonb', 'p_lernender bigint, p_einheit bigint', NF.stand_alt().replace('begin', 'begin /* abweichend */', 1))):
            sprache = 'sql' if fn == 'nachtest_auswahl' else 'plpgsql'
            faelle.append((fn, f"create or replace function schule.{fn}({kopf}) returns {rueck} language {sprache} stable set search_path to '' as $f$ {body} $f$;", 'weicht vom Repo-Stand ab'))
        for fn, aenderung, erwartet in faelle:
            out = pg.sql(aenderung + '\n' + f"do $nfx$ begin execute $nfxinhalt${einsp}$nfxinhalt$; end $nfx$;", erwartet_fehler='NF-S ABBRUCH')
            assert fn in out and erwartet in out, (fn, aenderung[:60], out[-800:])
            assert zustand(pg) == (z0, rest0), f'{fn}: nichts darf geblieben sein'
        # die Funktion fehlt ganz
        for fn_, sg_ in (('nachtest_stand', 'bigint, bigint'), ('test_starten_intern', 'bigint, jsonb')):
            pg.sql(f"drop function schule.{fn_}({sg_});\n" + f"do $nfx$ begin execute $nfxinhalt${einsp}$nfxinhalt$; end $nfx$;", erwartet_fehler='NF-S ABBRUCH')
        print(f'Negativfälle: {len(faelle) + 2} (abweichender Text / STRICT / VOLATILE bzw. STABLE / SECURITY DEFINER je Funktion, Funktion fehlt) -> Abbruch, nichts geblieben')
        # nur EINE Funktion schon neu, die andere alt: wird nachgezogen (zulässiger Zwischenzustand)
        pg.sql(f"create or replace function schule.nachtest_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int) returns bigint[] language sql stable set search_path to '' as $f${NF.auswahl_neu()}$f$;")
        out = pg.paket(einsp)
        assert '"nachtest_auswahl": "neu -> neu"' in out and '"nachtest_stand": "alt -> neu"' in out and '"test_starten_intern": "alt -> neu"' in out, out[-1200:]
        print('Zwischenzustand (eine Funktion schon neu): zweite wird nachgezogen')
    finally:
        pg.ende()
    print('Teil 2 (lokaler Nachbau) bestanden')


def main():
    probe, einsp = teil1()
    teil2(probe, einsp)
    print('OK')


if __name__ == '__main__':
    main()
