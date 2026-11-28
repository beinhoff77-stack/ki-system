"""Test für W1/W2 „Verstehen in Tests“ (tools/vtest_sql.py, tools/vtest_pruefen.py) mit den 6 Muster-Aufgaben in tools/tests/vtest_muster/
(erfundene Einheit muster.potenzen, id 9001, Lernziele potenz_sinn (V), rechnen (R), vorzeichen (V)).

Teil 1 (immer): Muster besteht W2; Vorschlag auswahl.json besteht (⌈n/2⌉, abwechselnd); Negativfälle der Prüfung (Lückenweg, zaehlt nein, 3er-Auswahl, Stufe 1,
  typ fehlt, typ direkt/erkennen, Etappe ohne Test-Aufgabe, Toleranz, falsche Fehlbild-Rechnung, Fehler-Detektiv als reine Zahl/3 Zeilen, ähnlich zur Übung,
  ersetzt_test fehlt, Lehrplan falsch, Hälfte verfehlt); alle Pakete unter tools/tests/aus byteidentisch zu origin/lernen-app (md5).
Teil 2 (nur mit lokalem Postgres; mit und ohne RB_PG_ICU=de-DE ausführen): NACHBAU (wie bestand_berichtigung1_test.py, NICHT die echte Datenbank) mit NF-S;
  Probelauf rollt zurück (Bericht am Anfang der Meldung); Negativfälle im SQL (NF-S fehlt, zusätzlicher Trigger, Einheit gesperrt, NULL-Feld, Etappe ohne
  Test-Aufgabe, Zwischenstand, Prüfbedingung auf reihenfolge); laufende Sitzung mit alter Aufgabe -> Gruppe zurückgestellt, Sitzung unberührt, später nachgeholt;
  Einspielen ersetzt die Test-Aufgabe; neuer Flugtest zieht genau eine Aufgabe je Lernziel (die neue); Korrektur zieht die erwartete Art; Nachtest-Auswahl
  wie geplant; Lernstände byteidentisch; Zweitlauf ändert nichts.
Aufruf: python3 -I tools/tests/vtest_sql_test.py   und   RB_PG_ICU=de-DE python3 -I tools/tests/vtest_sql_test.py   (enden mit OK)
"""
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import vtest_pruefen as P  # noqa: E402
import vtest_sql as W  # noqa: E402
import regelbezug_sql_test as T  # noqa: E402
import bestand_berichtigung1_test as BT  # noqa: E402
import nf_einspielen as NF  # noqa: E402

M = WURZEL / 'tools/tests/vtest_muster'
AUS = WURZEL / 'tools/tests/aus'
E = 9001
OPT = dict(runde='9', auswahl_datei=M / 'auswahl.json', plan_datei=M / 'plan.json', themen_dir=M / 'themen')


def k_muster():
    return P.kontext(**OPT)


def fehler_mit(aendern):
    k = k_muster()
    aendern(k)
    return P.runde_pruefen(k)[0]


def nach_kennung(k, kn):
    return next(x for _, x in k['eintraege'] if x['kennung'] == kn)


def teil1():
    k = k_muster()
    f, h, je, ein = P.runde_pruefen(k)
    assert not f, f
    gruppen = W.daten(k)
    assert [g['l'] for g in gruppen] == ['potenz_sinn', 'vorzeichen'] and all(len(g['items']) == 3 for g in gruppen)
    assert [i['nr'] for i in gruppen[0]['items']] == [100 + 80000 + 9000 + 1, -100000 + 9000 + 1, -100000 + 9000 + 2]
    rc = subprocess.run([sys.executable, '-I', 'tools/vtest_pruefen.py', '--nur-auswahl'], cwd=WURZEL, capture_output=True, text=True)
    assert rc.returncode == 0 and 'zusammen 65 Verstehens-Lernziele von 120' in rc.stdout, rc.stdout[-500:]
    # Negativfälle der Prüfung (jeder für sich auf einer Kopie)
    def setze(kn, fn):
        def a(k): fn(nach_kennung(k, kn))
        return a
    faelle = [
        ('Lückenweg', setze('VTM-001', lambda x: x.update(form='lueckenweg')), 'V1'),
        ('zaehlt nein', setze('VTM-002', lambda x: x.update(zaehlt='nein')), 'V2'),
        ('zaehlt leer', setze('VTM-002', lambda x: x.pop('zaehlt')), 'V2'),
        ('3er-Auswahl', setze('VTM-003', lambda x: (x['aufgabe']['a'].pop(), x['fehlbilder'].pop())), 'V7'),
        ('Stufe 1', setze('VTM-004', lambda x: (x.update(stufe=1), x['aufgabe'].update(s=1))), 'V3'),
        ('typ fehlt', setze('VTM-006', lambda x: x.pop('typ')), 'V4'),
        ('typ direkt', setze('VTM-006', lambda x: x.update(typ='direkt', form=None)), 'V4'),
        ('typ erkennen', setze('VTM-006', lambda x: x.update(typ='erkennen')), 'V4'),
        ('Etappe ohne Test-Aufgabe', lambda k: k['eintraege'].remove(next(e for e in k['eintraege'] if e[1]['kennung'] == 'VTM-004')), 'Test-Aufgaben, Soll genau 1'),
        ('Toleranz', setze('VTM-002', lambda x: x['aufgabe']['o'].update(toleranz=0.5)), 'V9'),
        ('Fehlbild-Rechnung falsch', setze('VTM-002', lambda x: x['fehlbilder'][0].update(rechnung='81 : 3')), 'V11'),
        ('Fehlbild ohne Rechnung', setze('VTM-006', lambda x: x['fehlbilder'][0].pop('rechnung')), 'V11'),
        ('Lösungsrechnung falsch', setze('VTM-006', lambda x: x['aufgabe'].update(c='−64 : 8')), 'V10'),
        ('Fehler-Detektiv als Zahl', setze('VTM-001', lambda x: x['aufgabe'].update(y='zahl', o={'wert': 32}, c='32', f={'text': x['aufgabe']['f']['text']})), 'V8'),
        ('Fehler-Detektiv-Auswahl mit 3 Zeilen', setze('VTM-005', lambda x: x['aufgabe']['f'].update(text=x['aufgabe']['f']['text'].replace(' Zeile 4: −81 − 9 = −90', ''))), 'V8'),
        ('Fehler-Detektiv-Auswahl ohne Begründung', setze('VTM-005', lambda x: x['aufgabe'].update(a=['In Zeile 2', 'In Zeile 1', 'In Zeile 3', 'In Zeile 4'])), 'V8'),
        ('ähnlich zur Übung', setze('VTM-002', lambda x: x['aufgabe']['f'].update(text='Berechne 3⁴.')), 'V15'),
        ('ersetzt_test fehlt', setze('VTM-004', lambda x: x.pop('ersetzt_test')), 'V17'),
        ('Lehrplan falsch', setze('VTM-004', lambda x: x.update(lehrplan='M6 1.2')), 'V13'),
        ('NULL in Lernkarte', setze('VTM-004', lambda x: x['aufgabe'].update(l=None)), 'aufgabe.l'),
        ('Hälfte verfehlt (nur 1 von 3)', lambda k: [k['eintraege'].remove(e) for e in list(k['eintraege']) if e[1]['lernkarte'] == 'vorzeichen'], 'Soll ⌈3/2⌉ = 2'),
    ]
    for was, fn, erwartet in faelle:
        f = fehler_mit(fn)
        assert any(erwartet in t for t in f), (was, f[:6])
    # W1 baut bei Fehlern kein Paket
    k = k_muster(); nach_kennung(k, 'VTM-002')['zaehlt'] = 'nein'
    try: W.daten(k); raise AssertionError('W1 hätte abbrechen müssen')
    except SystemExit as ex: assert 'V2' in str(ex)
    # bestehende Pakete byteidentisch zu origin/lernen-app
    namen = subprocess.run(['git', 'ls-tree', '--name-only', 'origin/lernen-app', 'tools/tests/aus/'], cwd=WURZEL, capture_output=True, text=True, check=True).stdout.split()
    assert len(namen) >= 40, namen
    for n in namen:
        if Path(n).name.startswith('advent_s_'):   # ADVENT-S: noch nicht eingespielt, nach Urteil 1215 direkt nachgebessert (Prüfung in advent_s_test.py)
            continue
        soll = hashlib.md5(subprocess.run(['git', 'show', f'origin/lernen-app:{n}'], cwd=WURZEL, capture_output=True, check=True).stdout).hexdigest()
        ist = hashlib.md5((WURZEL / n).read_bytes()).hexdigest()
        assert soll == ist, f'{n} ist nicht mehr byteidentisch'
    print(f'Teil 1: Muster besteht, Vorschlag 65/120 besteht, {len(faelle)} Negativfälle der Prüfung, W1 bricht ab; {len(namen)} Pakete unter tools/tests/aus byteidentisch zu origin/lernen-app')
    return gruppen


def zahl(pg, sql):
    return int(pg.sql('\\pset tuples_only on\n' + sql).split()[0])


def wert(pg, sql):
    return pg.sql('\\pset tuples_only on\n' + sql).strip()


def aufbauen(pg):
    BT.aufbauen(pg, [])
    th = json.loads((M / 'themen/muster.potenzen.json').read_text(encoding='utf-8'))
    rows = []
    for i, a in enumerate(th['aufgaben'], 1):
        r = {f: a[f] for f in P.FELDER if a.get(f) is not None}
        r['r'] = i
        rows.append(r)
    pg.sql(f"insert into schule.thema values ({E}, 'muster.potenzen') on conflict do nothing;\n"
           f"insert into schule.einheit (id, thema_id, status) values ({E}, {E}, 'freigegeben');\n"
           f"select schule.aufgaben_einfuegen({E}, $j${json.dumps(rows, ensure_ascii=False)}$j$::jsonb);")
    assert zahl(pg, f"select count(*) from schule.aufgabe where einheit_id = {E}") == len(rows)


def aid(frage_text, pool):
    return f"(select id from schule.aufgabe where einheit_id = {E} and pool = '{pool}' and frage->>'text' = $t${frage_text}$t$)"


def neu_id(g, kn):
    it = next(i for i in g['items'] if i['k'] == kn)
    return f"(select id from schule.aufgabe where einheit_id = {E} and reihenfolge = {it['nr']})"


def sig(pg, tabellen):
    return {t: BT.sig(pg, t) for t in tabellen}


def teil2(gruppen):
    b = T.pg_bin()
    if not b:
        print('Teil 2 übersprungen (kein Postgres)'); return
    k = k_muster()
    probe, einsp = W.paket(k, gruppen, True), W.paket(k, gruppen, False)
    lern = ('versuch', 'karte_stand', 'sterne', 'lerntag', 'lernender', 'lernziel_stand', 'testsitzung', 'misch_ausgabe')
    alt_a, alt_b, alt_c = aid('Berechne 4³.', 'test'), aid('Berechne 6².', 'test'), aid('Berechne (−3)².', 'test')
    pg = T.PG(b)
    try:
        aufbauen(pg)
        alles = ('aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild', 'einheit') + lern
        vor = sig(pg, alles)

        def nichts(was):
            assert sig(pg, alles) == vor, f'{was}: etwas ist geblieben'

        # --- Probelauf: Bericht am Anfang, alles zurück
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        i = out.index('VTM BERICHT:')
        assert i < out.index('PROBELAUF bestanden') and 'Lernziele 2 (neu 2, schon fertig 0, zurückgestellt 0) | Aufgaben neu 6 (test 2, korrektur 2, sicherung 2) | alte Test-Aufgaben gesperrt 2 | Regeln 6, Fehlbilder 15' in out, out[-1500:]
        assert '"sollantworten_richtig": 6' in out and '"fehlantworten_gueltig_und_falsch": 15' in out and '"fehler": 0' in out, out[-1500:]
        nichts('Probelauf')
        pg.sql(probe, erwartet_fehler='PROBELAUF bestanden')      # auch direkt mit psql
        nichts('Probelauf direkt')
        print('Probelauf: bestanden, Bericht am Anfang der Meldung, alles zurückgerollt')

        # --- Negativfälle im SQL (jeweils mit der Änderung in EINER Transaktion; der Abbruch rollt beides zurück)
        def neg(vor_sql, erwartet, paket=einsp):
            pg.sql(vor_sql + f"\ndo $rbpaket$ begin execute $rbpaketinhalt${paket}$rbpaketinhalt$; end $rbpaket$;", erwartet_fehler=erwartet)
            nichts(erwartet)
        offen, zu = f"update schule.einheit set status = 'geprueft' where id = {E};\n", f"\nupdate schule.einheit set status = 'freigegeben' where id = {E};"
        alt_t = f"create or replace function schule.test_starten_intern(p_lernender bigint, p_daten jsonb) returns jsonb language plpgsql set search_path to '' as $f${NF.tsi_alt()}$f$;"
        alt_s = f"create or replace function schule.nachtest_stand(p_lernender bigint, p_einheit bigint) returns jsonb language plpgsql stable set search_path to '' as $f${NF.stand_alt()}$f$;"
        n_neg = 0
        for was, sql_, erw in (
                ('NF-S fehlt (test_starten_intern alt)', alt_t, 'erst NF-S einspielen'),
                ('NF-S fehlt (nachtest_stand alt)', alt_s, 'erst NF-S einspielen'),
                ('zusätzlicher Trigger', "create function schule.t_x() returns trigger language plpgsql as $$ begin return new; end $$;\n"
                                         "create trigger t_x before update on schule.aufgabe for each row execute function schule.t_x();", 'festen Soll-Liste'),
                ('fehlender Trigger', 'drop trigger einheit_schutz on schule.einheit;', 'festen Soll-Liste'),
                ('Trigger schreibt', "create or replace function schule.einheit_schutz() returns trigger language plpgsql as $$ begin insert into schule.sterne (lernender_id, menge, grund, bezug) values (1, 1, 'x', 'y'); return coalesce(new, old); end $$;", 'schreibt oder meldet'),
                ('Einheit gesperrt', f"update schule.einheit set status = 'geprueft' where id = {E};", 'ist nicht freigegeben'),
                ('NULL-Feld (Lernkarte der alten Test-Aufgabe NULL)', offen + f"update schule.aufgabe set variante_gruppe = null where id = {alt_a};" + zu, 'alte Test-Aufgabe 0-mal gefunden'),
                ('NULL-Feld (Lösung der alten Test-Aufgabe NULL)', offen + f"alter table schule.aufgabe disable trigger aufgabe_schutz; update schule.aufgabe set loesung = null where id = {alt_c}; alter table schule.aufgabe enable trigger aufgabe_schutz;" + zu, 'alte Test-Aufgabe 0-mal gefunden'),
                ('Etappe ohne Test-Aufgabe (alte schon gesperrt, neue fehlen)', offen + f"update schule.aufgabe set freigegeben = false where id = {alt_a};" + zu, 'Etappe ohne Test-Aufgabe'),
                ('zweite freigegebene Test-Aufgabe im Lernziel', f"select schule.aufgaben_einfuegen({E}, '[{{\"l\": \"potenz_sinn\", \"t\": \"begriff\", \"p\": \"test\", \"s\": 2, \"y\": \"zahl\", \"f\": {{\"text\": \"Zusatz\"}}, \"o\": {{\"wert\": 1}}, \"r\": 999}}]'::jsonb);", 'freigegebene Test-Aufgaben (erwartet genau die alte)'),
                ('Zwischenstand (eine neue schon da)', f"select schule.aufgaben_einfuegen({E}, $j${json.dumps([gruppen[0]['items'][1]['row']], ensure_ascii=False)}$j$::jsonb);", 'Zwischenstand'),
                ('Platz belegt', f"select schule.aufgaben_einfuegen({E}, '[{{\"l\": \"rechnen\", \"t\": \"berechnen\", \"p\": \"uebung\", \"s\": 2, \"y\": \"zahl\", \"f\": {{\"text\": \"Platzhalter\"}}, \"o\": {{\"wert\": 1}}, \"r\": {gruppen[1]['items'][2]['nr']}}}]'::jsonb);", 'schon belegt'),
                ('Prüfbedingung reihenfolge > 0', 'alter table schule.aufgabe add constraint r_pos check (reihenfolge > -1000000);', 'Prüfbedingung auf schule.aufgabe.reihenfolge')):
            neg(sql_, erw); n_neg += 1
            if 'NF-S' in was: neg(sql_, erw, probe); n_neg += 1
        # verfälschtes Paket: Fehlbild gleich der Lösung -> Antwortprobe bricht ab
        schlecht = einsp.replace('"wert": "-8"', '"wert": "-32"', 1)
        assert schlecht != einsp
        pg.paket(schlecht, erwartet_fehler='VTM ABBRUCH'); nichts('Fehlbild = Lösung'); n_neg += 1
        print(f'Negativfälle im SQL: {n_neg} Abbrüche, jedes Mal nichts geblieben')

        # --- laufende Sitzung mit der ALTEN Test-Aufgabe von potenz_sinn + offene Korrektur bei vorzeichen -> beide zurückgestellt (unberührt)
        pg.sql(f"insert into schule.testsitzung (lernender_id, art, einheit_id, aufgaben, status) values (2, 'blocktest', {E}, array[{alt_a}, {alt_b}, {alt_c}], 'laeuft');\n"
               f"insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, status) values (2, {E}, 'vorzeichen', 'fehler');")
        ts_vor = wert(pg, "select md5(string_agg(x::text, '|' order by id)) from schule.testsitzung x")
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert 'zurückgestellt 2' in out and 'laufende Testsitzung' in out and 'offene Korrektur' in out, out[-1500:]
        out = pg.paket(einsp)
        assert 'Lernziele 2 (neu 0, schon fertig 0, zurückgestellt 2) | Aufgaben neu 0' in out, out[-800:]
        assert wert(pg, "select md5(string_agg(x::text, '|' order by id)) from schule.testsitzung x") == ts_vor
        assert zahl(pg, f"select count(*) from schule.aufgabe where id in ({alt_a}, {alt_c}) and freigegeben") == 2
        assert zahl(pg, f"select count(*) from schule.aufgabe where einheit_id = {E} and reihenfolge < 0 or reihenfolge > 80000 and einheit_id = {E}") == 0
        # Sitzung abgeschlossen, Korrektur erledigt -> Nachholen
        pg.sql("update schule.testsitzung set status = 'abgeschlossen', abgeschlossen_am = now();\nupdate schule.lernziel_stand set status = 'nachgewiesen';")
        lern_vor = sig(pg, lern)
        out = pg.paket(einsp)
        assert 'Lernziele 2 (neu 2, schon fertig 0, zurückgestellt 0) | Aufgaben neu 6 (test 2, korrektur 2, sicherung 2) | alte Test-Aufgaben gesperrt 2' in out, out[-800:]
        assert sig(pg, lern) == lern_vor, 'Lernstände verändert'
        print('Laufende Sitzung / offene Korrektur: Gruppen zurückgestellt (Sitzung byteidentisch, alte Aufgaben gültig), später nachgeholt; Lernstände byteidentisch')

        # --- Wirkung: Test-Aufgaben je Lernziel, Flugtest, Korrektur, Nachtest
        g_a, g_c = gruppen
        assert zahl(pg, f"select count(*) from schule.aufgabe where id in ({alt_a}, {alt_c}) and not freigegeben") == 2
        assert zahl(pg, f"select count(*) from schule.aufgabe where id = {alt_b} and freigegeben") == 1
        for l in ('potenz_sinn', 'rechnen', 'vorzeichen'):
            assert zahl(pg, f"select count(*) from schule.aufgabe where einheit_id = {E} and pool = 'test' and variante_gruppe = '{l}' and freigegeben") == 1, l
        # Kind 1 (frisch): erster Flugtest
        out = wert(pg, f"select schule.test_starten_intern(1, '{{\"einheit_id\": {E}, \"art\": \"blocktest\"}}')")
        st = json.loads(out)
        ids = [a['id'] for a in st['aufgaben']]
        soll = [zahl(pg, f"select {alt_b}"), zahl(pg, f"select {neu_id(g_a, 'VTM-001')}"), zahl(pg, f"select {neu_id(g_c, 'VTM-004')}")]
        assert ids == soll, (ids, soll)     # genau eine je Lernziel; Rechen-Aufgabe zuerst, dann die Verstehens-Aufgaben
        # Korrektur: alle drei falsch -> potenz_sinn/vorzeichen bekommen die neue Verstehens-Korrektur, rechnen die erste alte Rechen-Korrektur
        pg.sql(f"update schule.testsitzung set status = 'abgeschlossen', abgeschlossen_am = now() where lernender_id = 1;\n"
               f"insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, status) values (1, {E}, 'potenz_sinn', 'fehler'), (1, {E}, 'rechnen', 'fehler'), (1, {E}, 'vorzeichen', 'fehler');")
        st = json.loads(wert(pg, f"select schule.test_starten_intern(1, '{{\"einheit_id\": {E}, \"art\": \"korrektur\"}}')"))
        ids = sorted(a['id'] for a in st['aufgaben'])
        soll = sorted([zahl(pg, f"select {neu_id(g_a, 'VTM-002')}"), zahl(pg, f"select {aid('Berechne 3³.', 'korrektur')}"), zahl(pg, f"select {neu_id(g_c, 'VTM-005')}")])
        assert ids == soll, (ids, soll)
        # zweite Korrektur (die erste falsch): Vorrat Verstehen verbraucht (Muster: 1 je Lernziel) -> Rückfall auf die alte Rechen-Korrektur (Grenze, plan.md)
        pg.sql("update schule.testsitzung set status = 'abgeschlossen', abgeschlossen_am = now() where lernender_id = 1;")
        st = json.loads(wert(pg, f"select schule.test_starten_intern(1, '{{\"einheit_id\": {E}, \"art\": \"korrektur\"}}')"))
        ids = sorted(a['id'] for a in st['aufgaben'])
        soll = sorted([zahl(pg, f"select {aid('Berechne 7².', 'korrektur')}"), zahl(pg, f"select {aid('Berechne 9².', 'korrektur')}"), zahl(pg, f"select {aid('Berechne (−1)⁵.', 'korrektur')}")])
        assert ids == soll, (ids, soll)
        # Nachtest-Auswahl (1 je Etappe): Verstehens-Lernziele zuerst die neue Sicherung, danach Rechen-Bestand; Rechen-Lernziel unverändert
        def na(l): return wert(pg, f"select schule.nachtest_auswahl(2, {E}, '{l}', 1)")
        assert na('potenz_sinn') == '{' + str(zahl(pg, f"select {neu_id(g_a, 'VTM-003')}")) + '}'
        assert na('vorzeichen') == '{' + str(zahl(pg, f"select {neu_id(g_c, 'VTM-006')}")) + '}'
        assert na('rechnen') == '{' + str(zahl(pg, f"select {aid('Berechne 11².', 'sicherung')}")) + '}'
        pg.sql(f"insert into schule.versuch (lernender_id, aufgabe_id, client_id, antwort, richtig, anlauf, testsitzung_id) values (2, {neu_id(g_a, 'VTM-003')}, 'vt-n1', '{{}}', true, 1, 1);")
        assert na('potenz_sinn') == '{' + str(zahl(pg, f"select {aid('Berechne 5³.', 'sicherung')}")) + '}'
        print('Wirkung: je Lernziel genau eine freigegebene Test-Aufgabe; Flugtest = [alte Rechen-Aufgabe, neue V, neue V]; Korrektur 1 = V/V/R wie das Lernziel, '
              'Korrektur 2 nach Verbrauch = Rechen-Bestand; Nachtest: V zuerst, dann Rechen-Bestand')

        # --- Zweitlauf ändert nichts
        nach = sig(pg, ('aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild', 'einheit'))
        pg.sql("update schule.lernziel_stand set status = 'nachgewiesen';")
        out = pg.paket(einsp)
        assert 'Lernziele 2 (neu 0, schon fertig 2, zurückgestellt 0) | Aufgaben neu 0' in out and 'gesperrt 0' in out, out[-800:]
        assert sig(pg, ('aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild', 'einheit')) == nach
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        assert 'schon fertig 2' in out
        # fertig, aber eine neue Aufgabe verändert (Tipp gesetzt / Form NULL) -> Abbruch, nichts geblieben
        for satz in ("tipp = 'x'", 'form = null', "zaehlt = null"):
            pg.sql(offen + f"alter table schule.aufgabe disable trigger aufgabe_schutz; update schule.aufgabe set {satz} where id = {neu_id(g_a, 'VTM-001')}; alter table schule.aufgabe enable trigger aufgabe_schutz;" + zu
                   + f"\ndo $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;", erwartet_fehler='weicht aber vom Soll ab')
            assert sig(pg, ('aufgabe', 'aufgabe_regel', 'aufgabe_fehlbild', 'einheit')) == nach, satz
        print('Zweitlauf: 2 schon fertig, nichts geändert; abweichender fertiger Stand (Tipp, Form NULL, zählt NULL) -> Abbruch')
        print('Teil 2 (lokaler Nachbau) bestanden' + (' [ICU]' if __import__('os').environ.get('RB_PG_ICU') else ' [C]'))
    finally:
        pg.ende()


def main():
    gruppen = teil1()
    teil2(gruppen)
    print('OK')


if __name__ == '__main__':
    main()
