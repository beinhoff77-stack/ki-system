"""VTEST-S (Verstehen in Tests, Server): Test zieht in Verstehens-Etappen die Verstehens-Testaufgabe, Korrektur gleicher Art, Landung beim Üben erst mit
mindestens einer richtigen Verstehens-Aufgabe (nur nie gelandete Etappen, nur wenn die Etappe freigegebene Verstehens-Übungen hat). Plan und Fundstellen:
inhalte/plan/neuer-stil/server-schritt.md.

Erzeugt die Migration supabase/migrations/20261212_vtest_s.sql und die Pakete
  tools/tests/aus/vtest_s_probe.sql       Probelauf: macht alles, vergleicht, endet IMMER mit „VTEST-S KURZ {…} PROBELAUF bestanden …“ oder
                                         „VTEST-S PROBELAUF NICHT bestanden …“ (jeder Befund)
  tools/tests/aus/vtest_s_einspielen.sql  dasselbe, bleibt bei Erfolg eingespielt (Hinweis „VTEST-S eingespielt KURZ {…}“), sonst „VTEST-S ABBRUCH …“
Die Migration ist byteidentisch zur Einspiel-Datei (Einspielen nur über das selbstprüfende Paket).

Reihenfolge: NACH NF-S, TEMPO-S1 und FB-S (deren neue Funktionstexte sind Voraussetzung und werden per md5 geprüft).
Geändert (je Funktion genau zwei zulässige Zustände, prosrc-md5: alt -> ersetzen, neu -> nichts; alles andere und jeder Mischstand = Abbruch):
  schule.test_starten_intern(bigint, jsonb)    alt = NF-S neu; drei Zweige (Flugtest, Nachtragstest, Korrektur) je „if v_vt then <neu> else <bisher> end if“
  schule.etappen_stand(bigint, bigint)         alt = TEMPO-S1 neu; zwei Felder verstehen_noetig/verstehen_ok NUR bei eingeschaltetem Schalter
  schule.karte_landet(schule.karte_stand)      alt = LB-3 + FT-S Regel 6; eine Bedingung (Verstehens-Pflicht) angehängt
Der neue Text entsteht jeweils NUR durch Einfügen (kein Zeichen des alten Texts geändert oder entfernt) – geprüft in tools/tests/vtest_s_test.py.
Neu (fehlt -> anlegen, neu -> nichts): verstehen_regel, verstehen_an, aufgabe_verstehen, karte_verstehen_noetig, karte_verstehen_pflicht,
  karte_verstehen_ok, verstehen_korrektur_art. Schalter (schule.regel, 0 aus / 1 alle / 2 nur Testkind): verstehen_test_an, verstehen_landung_an.
Aufruf:  python3 -I tools/tests/vtest_s_einspielen.py            -> schreibt Migration und Pakete, druckt Größe/md5
         python3 -I tools/tests/vtest_s_einspielen.py --pruefen  -> schreibt nichts; Rückgabe 1, wenn eine Datei nicht dem Stand entspricht
"""
import hashlib
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import fb_einspielen as FB  # noqa: E402
import nf_einspielen as NF  # noqa: E402
import tempo_einspielen as TE  # noqa: E402

MIG = WURZEL / 'supabase/migrations'
AUS = WURZEL / 'tools/tests/aus'
MIGRATION = MIG / '20261212_vtest_s.sql'


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def body(datei, anfang):
    s = (MIG / datei).read_text(encoding='utf-8')
    i = s.index(anfang)
    j = s.index('as $function$', i) + len('as $function$')
    return s[j:s.index('$function$', j)]


def rep(b, alt, neu, n=1):
    assert b.count(alt) == n, (alt[:80], b.count(alt))
    return b.replace(alt, neu)


# ---------- alte Texte (Voraussetzung: NF-S, TEMPO-S1, FB-S eingespielt) ----------
TSI_ALT = ('7abcd2918f5042142d8720ae044b36c1', 6775)           # test_starten_intern nach NF-S
ES_ALT = ('3f49198f8dbf5c822a0be4650a5ebce5', None)            # etappen_stand nach TEMPO-S1
ES_VOR_TEMPO = 'bf3152e9a378a1d4e41c98965acf738e'
TSI_VOR_NF = NF.TSI_ALT_MD5
FB_W_NEU, FB_M_NEU = '79812f106f135beece303734f68fe351', 'b5674cbb53d0636617275c3b833596d9'


def tsi_alt():
    b = NF.tsi_neu()
    assert md5(b) == TSI_ALT[0] and len(b) == TSI_ALT[1]
    return b


def es_alt():
    b = TE.neuer_text()
    assert md5(b) == ES_ALT[0]
    return b


def kl_alt():
    """karte_landet: LB-3-Nachbesserung + FT-S Regel 6 (Text-Patch auf pg_get_functiondef, der Körper bleibt sonst wörtlich)."""
    b = body('20261120_lb3_nachbesserung.sql', 'create or replace function schule.karte_landet(')
    return rep(b, 'least(3, schule.karte_ziel(k.einheit_id, k.lernziel));', """least(3, schule.karte_ziel(k.einheit_id, k.lernziel))
     and (schule.karte_anwenden_ok(k) or not schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel)); -- FT-S Regel 6""")


def ft_body(name):
    return body('20261203_ft_s_form_takt.sql', f'create or replace function {name}(')


# Bezugsfunktionen: werden nicht geändert, die neue Regel stützt sich auf genau diese Fassung
def bezug():
    return [('schule.aufgabe_zaehlt(schule.aufgabe)', ft_body('schule.aufgabe_zaehlt')),
            ('schule.karte_anwenden_ok(schule.karte_stand)', ft_body('schule.karte_anwenden_ok')),
            ('schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text)', ft_body('schule.karte_anwenden_pflicht'))]


# ---------- Einfügungen (der neue Text = alter Text + genau diese Einfügungen an genau diesen Stellen) ----------
# (Anker im alten Text, Einfügung, 'vor' | 'nach')
UNGESEHEN = """not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
                       and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))"""
TSI_EIN = [
    ("v_je int; /* NT-S */", " v_vt boolean; v_ev boolean; v_g boolean; /* VTEST-S */", 'nach'),
    ("perform pg_advisory_xact_lock(hashtext('schule_test'), p_lernender::int);",
     "\n  v_vt := schule.verstehen_an(p_lernender, 'verstehen_test_an'); -- VTEST-S: Schalter verstehen_test_an (0 aus, 1 alle, 2 nur Testkind); aus = alles wie bisher", 'nach'),
    # Nachtragstest: in einer Verstehens-Etappe zuerst eine ungesehene Verstehens-Aufgabe (test, dann korrektur), sonst wie bisher (nie „Vorrat erschöpft“ wegen der Art)
    ("          select a.id into v_aid from schule.aufgabe a\n            where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool in ('test', 'korrektur')",
     """          if v_vt then -- VTEST-S (a): Verstehens-Etappe = hat eine freigegebene Verstehens-Testaufgabe
            v_ev := exists (select 1 from schule.aufgabe a where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'test' and a.freigegeben
                              and schule.aufgabe_verstehen(a));
            select a.id into v_aid from schule.aufgabe a
              where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool in ('test', 'korrektur') and a.freigegeben
                and not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
                and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))
              order by (v_ev and schule.aufgabe_verstehen(a)) desc, (a.pool = 'test') desc, a.reihenfolge, a.id limit 1;
          else
""", 'vor'),
    ("order by (a.pool = 'test') desc, a.reihenfolge limit 1;", "\n          end if; -- VTEST-S (a) Nachtragstest", 'nach'),
    # erster Flugtest: je Etappe mit freigegebener Verstehens-Testaufgabe genau EINE (die erste) statt der Rechen-Testaufgabe(n); andere Etappen wie bisher;
    # Reihenfolge nach Etappen (so wechseln Rechnen und Verstehen wie die Etappen), in der Etappe nach reihenfolge
    ("        select coalesce(array_agg(a.id order by a.reihenfolge), '{}') into v_ids from schule.aufgabe a where a.einheit_id = v_einheit and a.pool = 'test' and a.freigegeben;",
     """        if v_vt then -- VTEST-S (a): Verstehens-Etappe -> nur ihre erste Verstehens-Testaufgabe; sonst alle Test-Aufgaben der Etappe wie bisher
          select coalesce(array_agg(q.id order by q.nr, q.reihenfolge, q.id), '{}') into v_ids from (
            select a.id, a.reihenfolge, coalesce(et.nr, 2147483647) nr, schule.aufgabe_verstehen(a) ist_v,
                   bool_or(schule.aufgabe_verstehen(a)) over (partition by a.variante_gruppe) ev,
                   row_number() over (partition by a.variante_gruppe, schule.aufgabe_verstehen(a) order by a.reihenfolge, a.id) rn
              from schule.aufgabe a
              left join (select o.x->>'lernziel' lz, min(o.nr) nr from jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality o(x, nr) group by 1) et
                on et.lz = a.variante_gruppe
             where a.einheit_id = v_einheit and a.pool = 'test' and a.freigegeben) q
           where not q.ev or (q.ist_v and q.rn = 1);
        else
""", 'vor'),
    ("        select coalesce(array_agg(a.id order by a.reihenfolge), '{}') into v_ids from schule.aufgabe a where a.einheit_id = v_einheit and a.pool = 'test' and a.freigegeben;",
     "\n        end if; -- VTEST-S (a) Flugtest", 'nach'),
    # Korrektur: gleiche Art wie die falsche Aufgabe der letzten Testsitzung dieser Etappe (verstehen_korrektur_art); Rückfall siehe server-schritt.md
    ("        select a.id into v_aid from schule.aufgabe a\n          where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'korrektur'",
     f"""        if v_vt then -- VTEST-S (b): 1. ungesehen und gleiche Art, 2. nur bei Verstehen: schon gestellte Verstehens-Korrektur (am längsten her), 3. ungesehen andere Art
          v_g := schule.verstehen_korrektur_art(p_lernender, v_einheit, r.lernziel);
          select q.id into v_aid from (
            select a.id, a.reihenfolge, schule.aufgabe_verstehen(a) ist_v,
                   {UNGESEHEN} neu,
                   greatest((select max(v.am) from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id),
                            (select max(x.gestartet_am) from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))) zuletzt
              from schule.aufgabe a
             where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'korrektur' and a.freigegeben) q
           where q.neu or (v_g and q.ist_v)
           order by case when q.neu and (v_g is null or q.ist_v = v_g) then 0 when not q.neu then 1 else 2 end, q.zuletzt nulls first, q.reihenfolge, q.id limit 1;
        else
""", 'vor'),
    ("          order by a.reihenfolge limit 1;", "\n        end if; -- VTEST-S (b) Korrektur", 'nach'),
]
ES_EIN = [
    ("'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb))",
     "\n           || case when vs.an then jsonb_build_object('verstehen_noetig', schule.karte_verstehen_pflicht(k, p_lernender, p_einheit, z.lz),"
     " 'verstehen_ok', coalesce(schule.karte_verstehen_ok(k), false)) else '{}'::jsonb end /* VTEST-S */", 'nach'),
    ("  cross join (select schule.flug_nachtest(p_lernender, p_einheit) v offset 0) fn",
     "\n  cross join (select schule.verstehen_an(p_lernender, 'verstehen_landung_an') an offset 0) vs -- VTEST-S: Schalter einmal je Aufruf", 'nach'),
]
KL_EIN = [
    ("(schule.karte_anwenden_ok(k) or not schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel))",
     "\n     and (schule.karte_verstehen_ok(k) or not schule.karte_verstehen_pflicht(k, k.lernender_id, k.einheit_id, k.lernziel)) /* VTEST-S */", 'nach'),
]


def einfuegen(b, liste):
    for anker, ein, wo in liste:
        assert b.count(anker) == 1, anker[:80]
        assert ein not in b
        b = b.replace(anker, ein + anker if wo == 'vor' else anker + ein)
    return b


def tsi_neu():
    return einfuegen(tsi_alt(), TSI_EIN)


def es_neu():
    return einfuegen(es_alt(), ES_EIN)


def kl_neu():
    return einfuegen(kl_alt(), KL_EIN)


V_TYPEN = ('begruenden', 'fehler', 'darstellung', 'parameter', 'umkehr', 'rueckwaerts', 'transfer')          # = tools/vtest_pruefen.py V_TYPEN
V_FORMEN = ('fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'bruecke', 'umkehren', 'viele_antworten')   # = tools/vtest_pruefen.py V_FORMEN
SP = '{"search_path=\\"\\""}'

# Neue Hilfsfunktionen: (Signatur, Kopf, Rückgabe-Zeile, Text, Kommentar)
HILFEN = [
    ('schule.verstehen_regel(text, integer)', 'schule.verstehen_regel(p text, p_std integer)', "\n returns integer language sql stable set search_path to ''\n", """
  select coalesce((select case when length(r.wert #>> '{}') between 1 and 3 and ((r.wert #>> '{}') collate "C") !~ '[^0-9]' then (r.wert #>> '{}')::int end
                     from schule.regel r where r.schluessel = p), p_std);
""", 'VTEST-S: Einstellwert aus schule.regel (wie fehlerkarte_regel); ein ungültiger Wert gilt als Vorgabe'),
    ('schule.verstehen_an(bigint, text)', 'schule.verstehen_an(p_l bigint, p_schalter text)', "\n returns boolean language sql stable set search_path to ''\n", """
  select case schule.verstehen_regel(p_schalter, 0)
           when 1 then true
           when 2 then coalesce((select l.ist_test from schule.lernender l where l.id = p_l), false)
           else false end;
""", 'VTEST-S: Schalter verstehen_test_an / verstehen_landung_an für dieses Kind (0 aus, 1 alle, 2 nur Testkinder)'),
    ('schule.aufgabe_verstehen(schule.aufgabe)', 'schule.aufgabe_verstehen(a schule.aufgabe)', "\n returns boolean language sql immutable set search_path to ''\n", f"""
  select (coalesce((a.typ collate "C") in ({', '.join(f"'{t}'" for t in V_TYPEN)}), false)
       or coalesce((a.form collate "C") in ({', '.join(f"'{t}'" for t in V_FORMEN)}), false))
     and a.form is distinct from 'lueckenweg';
""", 'VTEST-S: Verstehens-Aufgabe (Klasse V aus inhalte/plan/neuer-stil/didaktik.md Abschnitt 2 = tools/vtest_pruefen.py); Lückenweg nie; ohne typ/form = Rechnen'),
    ('schule.karte_verstehen_noetig(bigint, text)', 'schule.karte_verstehen_noetig(p_einheit bigint, p_lz text)', "\n returns boolean language sql stable set search_path to ''\n", """
  select exists (select 1 from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and schule.aufgabe_zaehlt(a) and schule.aufgabe_verstehen(a));
""", 'VTEST-S: die Lernkarte hat eine freigegebene, zählende Verstehens-Übung'),
    ('schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text)',
     'schule.karte_verstehen_pflicht(k schule.karte_stand, p_l bigint, p_einheit bigint, p_lz text)', "\n returns boolean language sql stable set search_path to ''\n", """
  select schule.verstehen_an(p_l, 'verstehen_landung_an')
     and k.sitzt_am is null and not coalesce(k.sitzt, false) and schule.karte_verstehen_noetig(p_einheit, p_lz);
""", 'VTEST-S: Verstehens-Aufgabe zum Landen nötig – nur bei Schalter verstehen_landung_an, nur nie gelandete Karten, nur mit freigegebener zählender Verstehens-Übung'),
    ('schule.karte_verstehen_ok(schule.karte_stand)', 'schule.karte_verstehen_ok(k schule.karte_stand)', "\n returns boolean language sql stable set search_path to ''\n", """
  select exists (select 1 from jsonb_object_keys(coalesce(k.gezaehlt, '{}'::jsonb)) x join schule.aufgabe a on a.id = x::bigint
                  where schule.aufgabe_verstehen(a) and schule.aufgabe_zaehlt(a));
""", 'VTEST-S: unter den gezählten Aufgaben (eigene Lösung) der Karte ist eine Verstehens-Aufgabe'),
    ('schule.verstehen_korrektur_art(bigint, bigint, text)', 'schule.verstehen_korrektur_art(p_l bigint, p_e bigint, p_lz text)', "\n returns boolean language sql stable set search_path to ''\n", """
  with s as (select t.id, t.aufgaben from schule.testsitzung t
              where t.lernender_id = p_l and t.einheit_id = p_e and t.status = 'abgeschlossen'
                and exists (select 1 from schule.aufgabe a where a.id = any(t.aufgaben) and a.variante_gruppe = p_lz)
              order by t.abgeschlossen_am desc nulls last, t.id desc limit 1)
  select case when bool_or(schule.aufgabe_verstehen(a)) then true when count(*) > 0 then false end
    from s join schule.aufgabe a on a.id = any(s.aufgaben) and a.variante_gruppe = p_lz
   where not exists (select 1 from schule.versuch v where v.testsitzung_id = s.id and v.aufgabe_id = a.id and v.richtig);
""", 'VTEST-S: Art der falschen (oder unbeantworteten) Aufgabe(n) dieser Etappe in der letzten abgeschlossenen Testsitzung: true Verstehen (auch wenn beide Arten falsch), false Rechnen, null unbekannt'),
]

SOLL = {
    'schule.test_starten_intern(bigint, jsonb)': f'p_lernender bigint, p_daten jsonb|jsonb|plpgsql|v|f|f|f|u|100|0|f|{SP}',
    'schule.etappen_stand(bigint, bigint)': f'p_lernender bigint, p_einheit bigint|jsonb|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.karte_landet(schule.karte_stand)': f'k schule.karte_stand|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.verstehen_regel(text, integer)': f'p text, p_std integer|integer|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.verstehen_an(bigint, text)': f'p_l bigint, p_schalter text|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.aufgabe_verstehen(schule.aufgabe)': f'a schule.aufgabe|boolean|sql|i|f|f|f|u|100|0|f|{SP}',
    'schule.karte_verstehen_noetig(bigint, text)': f'p_einheit bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.karte_verstehen_pflicht(schule.karte_stand, bigint, bigint, text)': f'k schule.karte_stand, p_l bigint, p_einheit bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.karte_verstehen_ok(schule.karte_stand)': f'k schule.karte_stand|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.verstehen_korrektur_art(bigint, bigint, text)': f'p_l bigint, p_e bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
}
GEAENDERT = [('schule.test_starten_intern(bigint, jsonb)', 'schule.test_starten_intern(p_lernender bigint, p_daten jsonb)',
              "\n returns jsonb language plpgsql set search_path to ''\n", tsi_alt, tsi_neu),
             ('schule.etappen_stand(bigint, bigint)', 'schule.etappen_stand(p_lernender bigint, p_einheit bigint)',
              "\n returns jsonb language sql stable set search_path to ''\n", es_alt, es_neu),
             ('schule.karte_landet(schule.karte_stand)', 'schule.karte_landet(k schule.karte_stand)',
              "\n returns boolean language sql stable set search_path to ''\n", kl_alt, kl_neu)]
# Voraussetzungen anderer Schritte: Funktion -> (md5 Voraussetzung erfüllt, md5 „noch nicht eingespielt“, Name des Schritts)
VORAUS = [('schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)', FB_W_NEU, FB.WAEHLEN_ALT[0], 'FB-S'),
          ('schule.mischkarten(bigint, bigint, integer)', FB_M_NEU, FB.MISCH_ALT[0], 'FB-S')]
REGELN = [('verstehen_test_an', 'VTEST-S: Tests – Verstehens-Etappe zieht die Verstehens-Testaufgabe, Korrektur gleicher Art (0 aus, 1 alle, 2 nur Testkinder)'),
          ('verstehen_landung_an', 'VTEST-S: Üben – nie gelandete Etappe landet erst mit einer richtigen Verstehens-Aufgabe (0 aus, 1 alle, 2 nur Testkinder; erst mit App)')]
KARTE_BUCHEN_STELLE = 'if not v_war_gelandet and schule.karte_landet(k) then'


def sq(s):
    return "'" + s.replace("'", "''") + "'"


def create(kopf, rueck, text):
    assert '$function$' not in text and '$vsx$' not in text
    return f"create or replace function {kopf}{rueck}as $function${text}$function$"


def paket(probe, varianten=None):
    """probe: Probelauf (endet immer mit raise exception). varianten {Signatur: Text}: nur für die Gegenprobe im Test (verdorbene neue Fassung)."""
    varianten = varianten or {}
    neu = {s: varianten.get(s) or f() for s, _, _, _, f in GEAENDERT}
    alt = {s: f() for s, _, _, f, _ in GEAENDERT}
    P = 'VTEST-S PROBELAUF NICHT bestanden' if probe else 'VTEST-S ABBRUCH'
    titel = 'Probelauf – rollt am Ende ALLES zurück' if probe else 'Einspielen'
    hilfen_neu = '\n'.join(f"    ({sq(s)}, '{md5(t)}')," for s, _, _, t, _ in HILFEN).rstrip(',')
    soll = '\n'.join(f"    ({sq(s)}, {sq(e)})," for s, e in SOLL.items()).rstrip(',')
    geaendert = '\n'.join(f"    ({sq(s)}, '{md5(alt[s])}', '{md5(neu[s])}')," for s, _, _, _, _ in GEAENDERT).rstrip(',')
    bez = '\n'.join(f"    ({sq(s)}, '{md5(t)}')," for s, t in bezug()).rstrip(',')
    vor = '\n'.join(f"    ({sq(s)}, '{m}', '{a}', '{n}')," for s, m, a, n in VORAUS).rstrip(',')
    regeln = '\n'.join(f"    ({sq(k)}, '0'::jsonb, {sq(h)})," for k, h in REGELN).rstrip(',')
    anlegen = []
    for s, kopf, rueck, t, kom in HILFEN:
        anlegen.append(f"    execute $vsx${create(kopf, rueck, t)}$vsx$;\n"
                       f"    execute $vsx$revoke all on function {s} from public$vsx$;\n"
                       f"    if exists (select 1 from pg_roles where rolname = 'anon') then execute $vsx$revoke all on function {s} from anon$vsx$; end if;\n"
                       f"    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $vsx$revoke all on function {s} from authenticated$vsx$; end if;\n"
                       f"    execute $vsx$comment on function {s} is {sq(kom)}$vsx$;")
    for s, kopf, rueck, _, _ in GEAENDERT:
        anlegen.append(f"    execute $vsx${create(kopf, rueck, neu[s])}$vsx$;")
    anlegen = '\n'.join(anlegen)
    kopien = (f"  execute $vsx${create('pg_temp.vs_es_alt(p_lernender bigint, p_einheit bigint)', GEAENDERT[1][2], alt['schule.etappen_stand(bigint, bigint)'])}$vsx$;\n"
              f"  execute $vsx${create('pg_temp.vs_kl_alt(k schule.karte_stand)', GEAENDERT[2][2], alt['schule.karte_landet(schule.karte_stand)'])}$vsx$;")
    if probe:
        ende = ("  raise exception 'VTEST-S KURZ % PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt). VOLL %', v_kurz::text, v_bericht::text;\n")
    else:
        ende = ("  drop function pg_temp.vs_es_alt(bigint, bigint);\n  drop function pg_temp.vs_kl_alt(schule.karte_stand);\n"
                "  raise notice 'VTEST-S eingespielt KURZ % VOLL %', v_kurz::text, v_bericht::text;\n")
    return f"""-- VTEST-S Verstehen in Tests, Server ({titel}). Erzeugt von tools/tests/vtest_s_einspielen.py – nicht von Hand ändern.
-- Plan, Fundstellen, Ablauf: inhalte/plan/neuer-stil/server-schritt.md. Einspielen NACH NF-S, TEMPO-S1 und FB-S (deren neue Funktionstexte werden per md5 verlangt).
-- Was (nur bei eingeschaltetem Schalter; Schalter 0 = beim Einspielen = genau das bisherige Verhalten):
--   verstehen_test_an:    erster Flugtest – je Etappe mit freigegebener Verstehens-Testaufgabe genau diese eine statt der Rechen-Testaufgabe(n), Reihenfolge nach Etappen;
--                         Nachtragstest – Verstehens-Etappe zuerst Verstehen; Korrektur – gleiche Art wie die falsche Aufgabe der letzten Testsitzung der Etappe
--                         (Rückfall bei leerem Verstehens-Vorrat: schon gestellte Verstehens-Korrektur, am längsten her; dann wie bisher).
--   verstehen_landung_an: eine nie gelandete Etappe mit freigegebener zählender Verstehens-Übung landet erst, wenn eine Verstehens-Übung selbst gelöst (gezählt) ist;
--                         etappen_stand liefert dann je Etappe verstehen_noetig und verstehen_ok. Gelandete, wieder geöffnete, gesetzte Etappen: unverändert.
-- Geändert: test_starten_intern, etappen_stand, karte_landet (neuer Text = alter Text + Einfügungen). Neu: 7 Hilfsfunktionen, 2 Regeln (Wert 0; ein vorhandener Wert bleibt).
-- Schutz: je Funktion genau zwei Zustände (alt -> ersetzen, neu -> nichts; Hilfen fehlt -> anlegen), jeder Mischstand = Abbruch; Eigenschaften gegen festes Soll;
-- Rechte der ersetzten Funktionen unverändert. Vergleich mit Schalter AUS in je EINER Anweisung: etappen_stand (alle Kinder × Einheiten) und karte_landet (alle Karten,
-- dazu jede Karte als „nie gelandet“) alt gegen neu – jede Abweichung = Abbruch. Danach Schalter AN nur in dieser Transaktion: nur Zahlen, Schalter zurück.
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT, keine Untertransaktion. Keine Tabellen-DDL (nur Funktionen und zwei Regel-Zeilen) – keine Lernpause nötig.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $vs$
declare
  fehler text[] := '{{}}'; r record; d text; v_kurz text; st jsonb := '{{}}'; acl_vor jsonb := '{{}}'; n_alt int := 0; n_neu int := 0;
  v_t_vor jsonb; v_l_vor jsonb; n_e int; n_k int; n_abw_es int; n_abw_kl int; n_abw_kl_offen int; n_kinder int; n_einh int; zz jsonb; v_bericht jsonb; t0 timestamptz; ms_aus numeric; ms_an numeric;
begin
  if to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null or to_regclass('schule.karte_stand') is null or to_regclass('schule.lernender') is null
     or to_regclass('schule.testsitzung') is null or to_regclass('schule.regel') is null or to_regclass('schule.einheit') is null or to_regclass('schule.lernziel_stand') is null then
    raise exception '{P}, Vorbedingung: eine der Tabellen aufgabe/versuch/karte_stand/lernender/testsitzung/regel/einheit/lernziel_stand fehlt – nichts geändert'; end if;
  for r in select * from (values ('aufgabe', 'typ'), ('aufgabe', 'form'), ('aufgabe', 'zaehlt'), ('aufgabe', 'pool'), ('aufgabe', 'freigegeben'), ('aufgabe', 'variante_gruppe'),
                                 ('aufgabe', 'reihenfolge'), ('versuch', 'testsitzung_id'), ('versuch', 'richtig'), ('versuch', 'am'), ('testsitzung', 'aufgaben'),
                                 ('testsitzung', 'status'), ('testsitzung', 'abgeschlossen_am'), ('testsitzung', 'gestartet_am'), ('karte_stand', 'gezaehlt'),
                                 ('karte_stand', 'sitzt_am'), ('lernender', 'ist_test'), ('einheit', 'inhalt'), ('regel', 'wert'), ('regel', 'hinweis')) x(t, s) loop
    if not exists (select 1 from information_schema.columns c where c.table_schema = 'schule' and c.table_name = r.t and c.column_name = r.s) then
      fehler := fehler || format('Spalte fehlt: schule.%s.%s', r.t, r.s); end if;
  end loop;
  -- 1. Zustand und Eigenschaften
  create temp table if not exists vs_soll (f text primary key, ei text) on commit drop;
  truncate vs_soll;
  insert into vs_soll values
{soll};
  create temp table if not exists vs_hilfe (f text primary key, m text) on commit drop;
  truncate vs_hilfe;
  insert into vs_hilfe values
{hilfen_neu};
  create temp table if not exists vs_geaendert (f text primary key, m_alt text, m_neu text) on commit drop;
  truncate vs_geaendert;
  insert into vs_geaendert values
{geaendert};
  for r in select s.f, s.ei, to_regprocedure(s.f) o from vs_soll s order by s.f collate "C" loop
    if r.o is null then
      if r.f in (select f from vs_hilfe) then st := st || jsonb_build_object(r.f, 'fehlt'); n_alt := n_alt + 1;
      else fehler := fehler || format('Funktion fehlt: %s', r.f); end if;
      continue;
    end if;
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    acl_vor := acl_vor || jsonb_build_object(r.f, (select concat_ws('|', p.proowner::regrole::text, coalesce(p.proacl::text, '')) from pg_proc p where p.oid = r.o));
    if v_kurz is distinct from r.ei then fehler := fehler || format('%s: Eigenschaften %s, erwartet %s', r.f, v_kurz, r.ei); end if;
    if r.f in (select f from vs_geaendert) then
      if md5(d) = (select m_alt from vs_geaendert where f = r.f) then st := st || jsonb_build_object(r.f, 'alt'); n_alt := n_alt + 1;
      elsif md5(d) = (select m_neu from vs_geaendert where f = r.f) then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      elsif r.f = 'schule.test_starten_intern(bigint, jsonb)' and md5(d) = '{TSI_VOR_NF}' then fehler := fehler || 'test_starten_intern: NF-S ist noch nicht eingespielt – erst NF-S';
      elsif r.f = 'schule.etappen_stand(bigint, bigint)' and md5(d) = '{ES_VOR_TEMPO}' then fehler := fehler || 'etappen_stand: TEMPO-S1 ist noch nicht eingespielt – erst TEMPO-S1';
      else fehler := fehler || format('%s weicht ab (md5 %s, Länge %s; erwartet %s oder %s)', r.f, md5(d), length(d),
                                      (select m_alt from vs_geaendert where f = r.f), (select m_neu from vs_geaendert where f = r.f)); end if;
    elsif md5(d) = (select m from vs_hilfe where f = r.f) then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
    else fehler := fehler || format('%s ist vorhanden, aber nicht im neuen Stand (md5 %s)', r.f, md5(d)); end if;
  end loop;
  if n_alt > 0 and n_neu > 0 then fehler := fehler || format('Mischstand (%s Funktionen alt/fehlend, %s neu) – kein Wiederanlauf auf einem Mischstand: %s', n_alt, n_neu, st::text); end if;
  -- Bezugsfunktionen (unverändert; die Regel stützt sich auf genau diese Fassung)
  for r in select * from (values
{bez}) x(f, m) loop
    if to_regprocedure(r.f) is null then fehler := fehler || format('Bezugsfunktion fehlt: %s', r.f); continue; end if;
    if (select md5(p.prosrc) from pg_proc p where p.oid = to_regprocedure(r.f)) is distinct from r.m then
      fehler := fehler || format('Bezugsfunktion %s weicht vom Repo-Stand ab (md5 %s, erwartet %s)', r.f, (select md5(p.prosrc) from pg_proc p where p.oid = to_regprocedure(r.f)), r.m); end if;
  end loop;
  -- Voraussetzungen anderer Schritte (FB-S): deren neuer Stand muss stehen
  for r in select * from (values
{vor}) x(f, m, m_vor, schritt) loop
    if to_regprocedure(r.f) is null then fehler := fehler || format('Voraussetzung fehlt: %s', r.f); continue; end if;
    select md5(p.prosrc) into d from pg_proc p where p.oid = to_regprocedure(r.f);
    if d = r.m_vor then fehler := fehler || format('%s: %s ist noch nicht eingespielt – erst %s', r.f, r.schritt, r.schritt);
    elsif d is distinct from r.m then fehler := fehler || format('Voraussetzung %s (%s) weicht ab (md5 %s, erwartet %s)', r.f, r.schritt, d, r.m); end if;
  end loop;
  -- karte_buchen muss die Landeregel genau an dieser Stelle rufen (sonst wirkt die Pflicht nicht)
  if to_regprocedure('schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)') is null then fehler := fehler || 'karte_buchen fehlt';
  elsif (select (length(p.prosrc) - length(replace(p.prosrc, {sq(KARTE_BUCHEN_STELLE)}, ''))) / length({sq(KARTE_BUCHEN_STELLE)}) from pg_proc p
          where p.oid = 'schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)'::regprocedure) <> 1 then
    fehler := fehler || 'karte_buchen: Stelle „{KARTE_BUCHEN_STELLE}“ nicht genau einmal'; end if;
  -- Regeln: fehlen oder gültig (ganze Zahl 0–2)
  create temp table if not exists vs_regel (k text primary key, w jsonb, h text) on commit drop;
  truncate vs_regel;
  insert into vs_regel values
{regeln};
  for r in select g.k, x.wert from vs_regel g join schule.regel x on x.schluessel = g.k loop
    if jsonb_typeof(r.wert) is distinct from 'number' or (r.wert #>> '{{}}')::numeric not in (0, 1, 2) then
      fehler := fehler || format('Regel %s hat einen ungültigen Wert %s (erlaubt 0, 1, 2)', r.k, r.wert); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception '{P}, Vorbedingung (% Befunde), nichts geändert: %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 2. Regeln anlegen (ein vorhandener Wert bleibt); für den Vergleich in dieser Transaktion AUS, danach zurück
  insert into schule.regel (schluessel, wert, hinweis) select g.k, g.w, g.h from vs_regel g order by g.k on conflict (schluessel) do nothing;
  select x.wert into v_t_vor from schule.regel x where x.schluessel = 'verstehen_test_an';
  select x.wert into v_l_vor from schule.regel x where x.schluessel = 'verstehen_landung_an';
  update schule.regel set wert = '0'::jsonb where schluessel in ('verstehen_test_an', 'verstehen_landung_an');
  -- alte Fassungen als Kopie in pg_temp (für den Vergleich in EINER Anweisung)
{kopien}

  -- 3. Anlegen / ersetzen (nur im Zustand alt)
  if n_alt > 0 then
{anlegen}
  end if;
  -- 4. Nachher: Zustand, Eigenschaften, Besitzer/Rechte
  for r in select s.f, s.ei from vs_soll s order by s.f collate "C" loop
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = to_regprocedure(r.f);
    if v_kurz is distinct from r.ei then fehler := fehler || format('%s: Eigenschaften nachher %s', r.f, v_kurz); end if;
    if md5(d) is distinct from coalesce((select m_neu from vs_geaendert where f = r.f), (select m from vs_hilfe where f = r.f)) then
      fehler := fehler || format('%s: Funktionstext nachher md5 %s', r.f, md5(d)); end if;
    if r.f in (select f from vs_geaendert) and acl_vor->>r.f is distinct from (select concat_ws('|', p.proowner::regrole::text, coalesce(p.proacl::text, '')) from pg_proc p where p.oid = to_regprocedure(r.f)) then
      fehler := fehler || format('%s: Besitzer/Rechte geändert', r.f); end if;
    if r.f in (select f from vs_hilfe) and exists (select 1 from pg_proc p, aclexplode(coalesce(p.proacl, acldefault('f', p.proowner))) a
                                                    where p.oid = to_regprocedure(r.f) and a.grantee = 0) then
      fehler := fehler || format('%s: für alle (public) ausführbar', r.f); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception '{P}, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 5. Vergleich mit Schalter AUS (je eine Anweisung = ein Schnappschuss)
  t0 := clock_timestamp();
  select count(*), count(*) filter (where pg_temp.vs_es_alt(l.id, e.id) is distinct from schule.etappen_stand(l.id, e.id)), count(distinct l.id), count(distinct e.id)
    into n_e, n_abw_es, n_kinder, n_einh from schule.lernender l cross join schule.einheit e;
  ms_aus := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  select count(*), count(*) filter (where pg_temp.vs_kl_alt(k) is distinct from schule.karte_landet(k)),
         count(*) filter (where pg_temp.vs_kl_alt(jsonb_populate_record(k, '{{"sitzt": false, "sitzt_am": null}}')) is distinct from schule.karte_landet(jsonb_populate_record(k, '{{"sitzt": false, "sitzt_am": null}}')))
    into n_k, n_abw_kl, n_abw_kl_offen from schule.karte_stand k;
  if n_abw_es > 0 or n_abw_kl > 0 or n_abw_kl_offen > 0 then
    raise exception '{P}, alles zurückgerollt: mit Schalter AUS weicht ab – etappen_stand % von % (z. B. %), karte_landet % von %, karte_landet als nie gelandet % von %',
      n_abw_es, n_e, (select string_agg(format('Kind %s Einheit %s', q.l, q.e), '; ') from (select l.id l, e.id e from schule.lernender l cross join schule.einheit e
        where pg_temp.vs_es_alt(l.id, e.id) is distinct from schule.etappen_stand(l.id, e.id) order by 1, 2 limit 5) q),
      n_abw_kl, n_k, n_abw_kl_offen, n_k; end if;

  -- 6. Schalter AN (nur in dieser Transaktion): nur Zahlen
  update schule.regel set wert = '1'::jsonb where schluessel in ('verstehen_test_an', 'verstehen_landung_an');
  t0 := clock_timestamp();
  with s as (select l.id l, j.key lz, j.value v from schule.lernender l cross join schule.einheit e cross join lateral jsonb_each(schule.etappen_stand(l.id, e.id)) j)
  select jsonb_build_object(
      'etappen_mit_feldern', count(*) filter (where s.v ? 'verstehen_noetig' and s.v ? 'verstehen_ok'),
      'etappen_ohne_felder', count(*) filter (where not (s.v ? 'verstehen_noetig' and s.v ? 'verstehen_ok')),
      'etappen_verstehen_fehlt_je_kind', coalesce((select jsonb_object_agg(q.l::text, q.n) from (select s2.l, count(*) n from s s2
         where (s2.v->>'verstehen_noetig')::boolean and not (s2.v->>'verstehen_ok')::boolean group by s2.l) q), '{{}}'::jsonb)) into zz from s;
  ms_an := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  zz := zz || (select jsonb_build_object(
      'karten_nie_gelandet', count(*) filter (where k.sitzt_am is null and not k.sitzt),
      'davon_mit_verstehens_uebung', count(*) filter (where k.sitzt_am is null and not k.sitzt and schule.karte_verstehen_noetig(k.einheit_id, k.lernziel)),
      'davon_verstehen_schon_ok', count(*) filter (where k.sitzt_am is null and not k.sitzt and schule.karte_verstehen_noetig(k.einheit_id, k.lernziel) and schule.karte_verstehen_ok(k)),
      'landebereit_bis_auf_verstehen', count(*) filter (where k.sitzt_am is null and not k.sitzt and pg_temp.vs_kl_alt(k) and not schule.karte_landet(k)),
      'gelandete_unveraendert', count(*) filter (where (k.sitzt or k.sitzt_am is not null) and pg_temp.vs_kl_alt(k) is not distinct from schule.karte_landet(k)),
      'gelandete_geaendert', count(*) filter (where (k.sitzt or k.sitzt_am is not null) and pg_temp.vs_kl_alt(k) is distinct from schule.karte_landet(k)))
    from schule.karte_stand k);
  zz := zz || (select jsonb_build_object(
      'lernkarten_uebung', count(*), 'lernkarten_ohne_verstehens_uebung', count(*) filter (where not q.v))
    from (select a.einheit_id, a.variante_gruppe, bool_or(schule.aufgabe_zaehlt(a) and schule.aufgabe_verstehen(a)) v from schule.aufgabe a
           where a.pool = 'uebung' and a.freigegeben group by 1, 2) q);
  zz := zz || (select jsonb_build_object(
      'test_etappen', count(*), 'test_etappen_verstehen', count(*) filter (where q.nv > 0), 'test_etappen_verstehen_und_rechnen', count(*) filter (where q.nv > 0 and q.nr > 0),
      'flugtest_aufgaben_bisher', coalesce(sum(q.nv + q.nr), 0), 'flugtest_aufgaben_neu', coalesce(sum(case when q.nv > 0 then 1 else q.nr end), 0))
    from (select a.einheit_id, a.variante_gruppe, count(*) filter (where schule.aufgabe_verstehen(a)) nv, count(*) filter (where not schule.aufgabe_verstehen(a)) nr
            from schule.aufgabe a where a.pool = 'test' and a.freigegeben group by 1, 2) q);
  zz := zz || (with f as (select s.lernender_id l, s.einheit_id e, s.lernziel lz, schule.verstehen_korrektur_art(s.lernender_id, s.einheit_id, s.lernziel) g
                            from schule.lernziel_stand s where s.status = 'fehler'),
    v as (select f.*, (select count(*) filter (where schule.aufgabe_verstehen(a)) from schule.aufgabe a where a.einheit_id = f.e and a.variante_gruppe = f.lz and a.pool = 'korrektur' and a.freigegeben
                         and not exists (select 1 from schule.versuch x where x.lernender_id = f.l and x.aufgabe_id = a.id)
                         and not exists (select 1 from schule.testsitzung x where x.lernender_id = f.l and a.id = any(x.aufgaben))) neu_v,
                      (select count(*) filter (where not schule.aufgabe_verstehen(a)) from schule.aufgabe a where a.einheit_id = f.e and a.variante_gruppe = f.lz and a.pool = 'korrektur' and a.freigegeben
                         and not exists (select 1 from schule.versuch x where x.lernender_id = f.l and x.aufgabe_id = a.id)
                         and not exists (select 1 from schule.testsitzung x where x.lernender_id = f.l and a.id = any(x.aufgaben))) neu_r,
                      (select count(*) filter (where schule.aufgabe_verstehen(a)) from schule.aufgabe a where a.einheit_id = f.e and a.variante_gruppe = f.lz and a.pool = 'korrektur' and a.freigegeben) alle_v
            from f)
    select jsonb_build_object('korrektur_offen', count(*), 'korrektur_art_verstehen', count(*) filter (where g), 'korrektur_art_rechnen', count(*) filter (where not g),
      'korrektur_art_unbekannt', count(*) filter (where g is null),
      'verstehen_neue_da', count(*) filter (where g and neu_v > 0), 'verstehen_wiederholung', count(*) filter (where g and neu_v = 0 and alle_v > 0),
      'verstehen_rueckfall_rechnen', count(*) filter (where g and alle_v = 0 and neu_r > 0), 'rechnen_neue_da', count(*) filter (where not g and neu_r > 0),
      'rechnen_rueckfall_verstehen', count(*) filter (where not g and neu_r = 0 and neu_v > 0)) from v);
  update schule.regel set wert = v_t_vor where schluessel = 'verstehen_test_an';
  update schule.regel set wert = v_l_vor where schluessel = 'verstehen_landung_an';
  if (select x.wert from schule.regel x where x.schluessel = 'verstehen_test_an') is distinct from v_t_vor
     or (select x.wert from schule.regel x where x.schluessel = 'verstehen_landung_an') is distinct from v_l_vor then raise exception '{P}: Schalter nicht zurückgesetzt'; end if;

  v_kurz := jsonb_build_object('zustand', case when n_alt > 0 then 'alt -> neu' else 'neu -> neu (schon eingespielt, nichts geändert)' end,
    'kinder', n_kinder, 'einheiten', n_einh, 'etappen_stand_verglichen', n_e, 'karten_verglichen', n_k, 'abweichungen_aus', n_abw_es + n_abw_kl + n_abw_kl_offen,
    'schalter', jsonb_build_object('verstehen_test_an', v_t_vor, 'verstehen_landung_an', v_l_vor),
    'flugtest_aufgaben_bisher_neu', jsonb_build_array(zz->'flugtest_aufgaben_bisher', zz->'flugtest_aufgaben_neu'), 'test_etappen_verstehen', zz->'test_etappen_verstehen',
    'korrektur_offen_v_r_unbekannt', jsonb_build_array(zz->'korrektur_offen', zz->'korrektur_art_verstehen', zz->'korrektur_art_rechnen', zz->'korrektur_art_unbekannt'),
    'landebereit_bis_auf_verstehen', zz->'landebereit_bis_auf_verstehen', 'lernkarten_ohne_verstehens_uebung', zz->'lernkarten_ohne_verstehens_uebung',
    'ms_aus_an', jsonb_build_array(ms_aus, ms_an))::text;
  v_bericht := zz || jsonb_build_object('zustand_vorher', st, 'md5_neu', (select jsonb_object_agg(f, m_neu) from vs_geaendert), 'fehler', 0);
  if (zz->>'etappen_ohne_felder')::int > 0 or (zz->>'gelandete_geaendert')::int > 0 then
    raise exception '{P}, alles zurückgerollt: mit Schalter AN fehlen Felder (%) oder eine gelandete Karte ändert ihre Landeregel (%)', zz->>'etappen_ohne_felder', zz->>'gelandete_geaendert'; end if;
{ende}end $vs$;
"""


def dateien():
    p, e = paket(True), paket(False)
    return [('vtest_s_probe.sql', p), ('vtest_s_einspielen.sql', e)], e


def main():
    out, einsp = dateien()
    ziele = [(AUS / n, t) for n, t in out] + [(MIGRATION, einsp)]
    for _, t in ziele:
        assert len(t.encode('utf-8')) < 1_500_000 and '\n\\' not in t
    if '--pruefen' in sys.argv:
        alt = [str(p.relative_to(WURZEL)) for p, t in ziele if not p.exists() or p.read_text(encoding='utf-8') != t]
        if alt: print('nicht auf dem Stand:', ', '.join(alt), file=sys.stderr); sys.exit(1)
        print('OK'); return
    print('| Datei | Bytes | md5 |\n|---|---|---|')
    for p, t in ziele:
        p.write_text(t, encoding='utf-8')
        print(f'| `{p.relative_to(WURZEL)}` | {len(t.encode("utf-8"))} | `{md5(t)}` |')
    for s, _, _, a, n in GEAENDERT:
        print(s, md5(a()), len(a()), '->', md5(n()), len(n()))
    for s, t in bezug():
        print('Bezug', s, md5(t), len(t))
    for s, _, _, t, _ in HILFEN:
        print('neu', s, md5(t), len(t))


if __name__ == '__main__':
    main()
