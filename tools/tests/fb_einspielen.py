"""FB-S (Fehler-Bordkarten): falsch oder nicht selbst gelöste Übungsaufgaben kommen in Wiederholung und Mischkarte gezielt zurück (ohne Kennzeichnung).

Erzeugt die Migration supabase/migrations/20261210_fb_s_fehlerkarten.sql und die Pakete
  tools/tests/aus/fb_s_probe.sql       Probelauf: macht alles, vergleicht, endet IMMER mit „FB-S PROBELAUF bestanden … ALLES zurückgerollt“ (oder „FB-S ABBRUCH …“)
  tools/tests/aus/fb_s_einspielen.sql  dasselbe, bleibt bei Erfolg eingespielt (Hinweis „FB-S eingespielt …“)
Die Migration ist byteidentisch zur Einspiel-Datei (Einspielen nur über das selbstprüfende Paket). Regel, Fundstellen, Ablauf: inhalte/plan/fehlerkarten.md.

Geändert (je Funktion genau zwei zulässige Zustände des Funktionstexts, prosrc-md5: alt -> ersetzen, neu -> nichts, sonst Abbruch):
  schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)  eine Stelle: erster Sortierschlüssel „fällige Fehler-Bordkarte zuerst“
  schule.mischkarten(bigint, bigint, integer)               eine Stelle: „schon beantwortet“ zählt bei eingeschaltetem Schalter nur SEIT der Ausgabe
Neu (fehlt -> anlegen, neu -> nichts, sonst Abbruch): schule.fehlerkarte_regel, _an, _ab, _serie, _faellig.
Nur lesend geprüft (müssen dem Repo-Stand entsprechen, sonst Abbruch): wdh_sperre_ab, lern_datum, heute_tag, wdh_aufgabe_da(3), misch_gueltig.
Aufruf:  python3 -I tools/tests/fb_einspielen.py            -> schreibt Migration und Pakete, druckt Größe/md5
         python3 -I tools/tests/fb_einspielen.py --pruefen  -> schreibt nichts; Rückgabe 1, wenn eine Datei nicht dem Stand entspricht
"""
import hashlib
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
MIG = WURZEL / 'supabase/migrations'
AUS = WURZEL / 'tools/tests/aus'
MIGRATION = MIG / '20261210_fb_s_fehlerkarten.sql'


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


# ---------- Funktionstexte aus dem Repo nachrechnen (Grundfassung + dokumentierte Text-Patches, in Einspiel-Reihenfolge) ----------
def body(datei, anfang):
    s = (MIG / datei).read_text(encoding='utf-8')
    i = s.index(anfang)
    j = s.index('as $function$', i) + len('as $function$')
    return s[j:s.index('$function$', j)]


def rep(b, alt, neu, n=1):
    assert b.count(alt) == n, (alt[:80], b.count(alt))
    return b.replace(alt, neu)


def patches(datei, fn):
    """Paare (alt, neu) eines pg_temp.*_ersetzen('fn', 'merkmal', array[...], array[...])-Aufrufs."""
    s = (MIG / datei).read_text(encoding='utf-8')
    i = s.index(f"_ersetzen('{fn}'")
    seg = s[i:s.index(']);', s.index('array[', s.index('array[', i) + 1)) + 3]
    arr = re.findall(r'array\[(.*?)\]\s*[,)]', seg, re.S)
    alt, neu = (re.findall(r'\$a\$(.*?)\$a\$', a, re.S) for a in arr[:2])
    assert len(alt) == len(neu) > 0
    return list(zip(alt, neu))


def anwenden(b, paare):
    for a, n in paare:
        b = rep(b, a, n)
    return b


def ftsp(b):
    """FT-S-Patch (20261203_ft_s_form_takt.sql, Plan-Einträge wdh_aufgabe_waehlen / wdh_aufgabe_da): nur zählende Aufgaben."""
    return rep(b, 'where a.einheit_id = p_e and', 'where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and')


def waehlen_alt():
    return ftsp(body('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.wdh_aufgabe_waehlen('))


def mischkarten_alt():
    b = body('20261120_i4_misch_ausgabe_wieder.sql', 'create or replace function schule.mischkarten(')
    b = anwenden(b, patches('20261122_wd_s_wiederholungen.sql', 'schule.mischkarten(bigint, bigint, integer)'))
    return anwenden(b, patches('20261122_wd_s3_frische_aufgaben.sql', 'schule.mischkarten(bigint, bigint, integer)'))


def mischkarten_waehlen_alt():
    """Nur für den Nachbau (wird nicht geändert): Text aus w176_t3 (von I-2 umbenannt) + WD-3 + WD-S 3."""
    b = body('20261118_w176_t3_mischkarten.sql', 'create or replace function schule.mischkarten(')
    b = anwenden(b, patches('20261122_wd_s_wiederholungen.sql', 'schule.mischkarten_waehlen(bigint, bigint, integer)'))
    return anwenden(b, patches('20261122_wd_s3_frische_aufgaben.sql', 'schule.mischkarten_waehlen(bigint, bigint, integer)'))


def misch_gueltig_alt():
    b = body('20261120_i4_misch_ausgabe_wieder.sql', 'create or replace function schule.misch_gueltig(')
    b = anwenden(b, patches('20261122_fp_s2_nacharbeit_924.sql', 'schule.misch_gueltig(bigint, schule.aufgabe, jsonb)'))
    return anwenden(b, patches('20261122_wd_s4_nacharbeit_921.sql', 'schule.misch_gueltig(bigint, schule.aufgabe, jsonb)'))


def da_alt():
    return ftsp(body('20261122_wd_s4_nacharbeit_921.sql', 'create or replace function schule.wdh_aufgabe_da('))


def sperre_ab_alt():
    return body('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.wdh_sperre_ab(')


def lern_datum_alt():
    return body('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.lern_datum(')


def heute_tag_alt():
    return body('20261120_i2_lernregeln.sql', 'create or replace function schule.heute_tag(')


# Nachgerechnete Hashes (Projektleiter bestätigt sie lesend an der echten Datenbank: md5(prosrc), length(prosrc))
WAEHLEN_ALT = ('7a6d76c619d1edfb6cdd8ee4a4a5cb1f', 537)
MISCH_ALT = ('1d8a3466c1698cfe9d4d0dd00d5ca638', 5123)

# ---------- neue Texte ----------
W_ALT_STELLE = '   order by c.zuletzt nulls first, (c.stufe = 1), random() limit 1;'
W_NEU_STELLE = '   order by schule.fehlerkarte_faellig(p_l, c.id, c.zuletzt) desc, c.zuletzt nulls first, (c.stufe = 1), random() limit 1;'
M_ALT_STELLE = 'or exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = m.aufgabe_id) -- WD-S 3: schon beantwortet'
M_NEU_STELLE = ('or exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = m.aufgabe_id'
                ' and (not schule.fehlerkarte_an(p_lernender) or v.am >= m.ausgegeben_am))'
                ' -- WD-S 3: schon beantwortet; FB-S: bei eingeschalteten Fehler-Bordkarten nur seit der Ausgabe')


def waehlen_neu(variante=None):
    b = rep(waehlen_alt(), W_ALT_STELLE, W_NEU_STELLE)
    if variante: b = rep(b, W_NEU_STELLE, variante)          # nur für die Gegenprobe im Test
    return b


def mischkarten_neu():
    return rep(mischkarten_alt(), M_ALT_STELLE, M_NEU_STELLE)


# Neue Hilfsfunktionen: (Signatur, Kopf, Text, Kommentar). Kopf = alles zwischen „create or replace function …(…)“ und „as $function$“.
HILFEN = [
    ('schule.fehlerkarte_regel(text, integer)', 'schule.fehlerkarte_regel(p text, p_std integer)', "\n returns integer language sql stable set search_path to ''\n", """
  select coalesce((select case when length(r.wert #>> '{}') between 1 and 3 and ((r.wert #>> '{}') collate "C") !~ '[^0-9]' then (r.wert #>> '{}')::int end
                     from schule.regel r where r.schluessel = p), p_std);
""", 'FB-S: Einstellwert aus schule.regel wie wd_regel; ein ungültiger Wert (keine ganze Zahl 0–999) gilt als Vorgabe, bricht also nie die Wiederholung'),
    ('schule.fehlerkarte_an(bigint)', 'schule.fehlerkarte_an(p_l bigint)', "\n returns boolean language sql stable set search_path to ''\n", """
  select case schule.fehlerkarte_regel('fehlerkarten_an', 0)
           when 1 then true
           when 2 then coalesce((select l.ist_test from schule.lernender l where l.id = p_l), false)
           else false end;
""", 'FB-S: Schalter fehlerkarten_an (0 aus, 1 an, 2 nur Testkinder)'),
    ('schule.fehlerkarte_ab(bigint)', 'schule.fehlerkarte_ab(p_l bigint)', "\n returns date language sql stable set search_path to ''\n", """
  select coalesce((select min(q.datum) from (select t.datum from schule.lerntag t where t.lernender_id = p_l and t.fach = 'Mathematik' and t.datum < schule.heute_tag(p_l)
                                              order by t.datum desc limit greatest(schule.fehlerkarte_regel('fehlerkarten_pause_lerntage', 2), 0)) q), schule.heute_tag(p_l));
""", 'FB-S: Wartezeit wie wdh_sperre_ab – Fehler-Bordkarte erst, wenn die letzte Bearbeitung vor diesem Lerntag liegt (fehlerkarten_pause_lerntage Lerntage Pause dazwischen)'),
    ('schule.fehlerkarte_serie(bigint, bigint)', 'schule.fehlerkarte_serie(p_l bigint, p_a bigint)', "\n returns integer language sql stable set search_path to ''\n", """
  with x as (select v.id, v.am, coalesce(v.richtig, false) and coalesce(v.hilfe, 0) = 0 selbst from schule.versuch v
              where v.lernender_id = p_l and v.aufgabe_id = p_a and v.testsitzung_id is null and coalesce(v.anlauf, 1) <> 2),
  s as (select x.am, x.id from x where x.selbst order by x.am desc, x.id desc limit 1)
  select count(*)::int from x where not x.selbst and (not exists (select 1 from s) or (x.am, x.id) > (select s.am, s.id from s));
""", 'FB-S: Bearbeitungen (Versuch ohne Test, 2. Anlauf zählt zur Bearbeitung davor) dieser Aufgabe seit der letzten eigenen Lösung (richtig, 1. Anlauf, ohne Tipp); 0 = zuletzt selbst gelöst oder nie bearbeitet'),
    ('schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone)', 'schule.fehlerkarte_faellig(p_l bigint, p_a bigint, p_zuletzt timestamp with time zone)',
     "\n returns boolean language sql stable set search_path to ''\n", """
  select coalesce(case when p_zuletzt is null or not schule.fehlerkarte_an(p_l) then false               -- Schalter aus: sofort false (kein weiterer Zugriff)
                       when schule.lern_datum(p_l, p_zuletzt) >= schule.fehlerkarte_ab(p_l) then false    -- Wartezeit noch nicht vorbei
                       when exists (select 1 from schule.aufgabe a where a.id = p_a and a.form = 'lueckenweg') then false
                       else schule.fehlerkarte_serie(p_l, p_a) between 1 and schule.fehlerkarte_regel('fehlerkarten_max', 3) end, false);
""", 'FB-S: fällige Fehler-Bordkarte (Schalter an, Wartezeit vorbei, kein Lückenweg, 1 bis fehlerkarten_max Bearbeitungen ohne eigene Lösung in Folge)'),
]

# Soll-Eigenschaften: Argumente | Ergebnis | Sprache | Volatilität | Definer | STRICT | Menge | Parallelität | Kosten | Zeilen | leakproof | Einstellungen
SP = '{"search_path=\\"\\""}'
SOLL = {
    'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)': f'p_l bigint, p_e bigint, p_lz text, p_misch boolean|bigint|sql|v|f|f|f|u|100|0|f|{SP}',
    'schule.mischkarten(bigint, bigint, integer)': f'p_lernender bigint, p_einheit bigint, p_anzahl integer DEFAULT 8|jsonb|plpgsql|v|f|f|f|u|100|0|f|{SP}',
    'schule.fehlerkarte_regel(text, integer)': f'p text, p_std integer|integer|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.fehlerkarte_an(bigint)': f'p_l bigint|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.fehlerkarte_ab(bigint)': f'p_l bigint|date|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.fehlerkarte_serie(bigint, bigint)': f'p_l bigint, p_a bigint|integer|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.fehlerkarte_faellig(bigint, bigint, timestamp with time zone)': f'p_l bigint, p_a bigint, p_zuletzt timestamp with time zone|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.wdh_sperre_ab(bigint)': f'p_l bigint|date|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.lern_datum(bigint, timestamp with time zone)': f'p_l bigint, p_zeit timestamp with time zone|date|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.heute_tag(bigint)': f'p_l bigint|date|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.wdh_aufgabe_da(bigint, bigint, text)': f'p_l bigint, p_e bigint, p_lz text|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
    'schule.misch_gueltig(bigint, schule.aufgabe, jsonb)': f'p_lernender bigint, a schule.aufgabe, p jsonb|boolean|sql|s|f|f|f|u|100|0|f|{SP}',
}
BEZUG = [('schule.wdh_sperre_ab(bigint)', sperre_ab_alt), ('schule.lern_datum(bigint, timestamp with time zone)', lern_datum_alt),
         ('schule.heute_tag(bigint)', heute_tag_alt), ('schule.wdh_aufgabe_da(bigint, bigint, text)', da_alt),
         ('schule.misch_gueltig(bigint, schule.aufgabe, jsonb)', misch_gueltig_alt)]
REGELN = [('fehlerkarten_an', '0', 0, 2, 'FB-S: Fehler-Bordkarten in Wiederholung und Mischkarte bevorzugt (0 aus, 1 an, 2 nur Testkinder)'),
          ('fehlerkarten_pause_lerntage', '2', 0, 30, 'FB-S: so viele Lerntage Pause zwischen Fehler und Wiederkehr (die Sperre wdh_sperre_lerntage gilt zusätzlich)'),
          ('fehlerkarten_max', '3', 0, 20, 'FB-S: höchstens so oft hintereinander bevorzugt zurück (Bearbeitungen ohne eigene Lösung in Folge); danach normale Auswahl')]


def rang(b):
    """Probe-Variante eines Auswahltexts ohne Zufall: ganze Rangfolge zweimal (Gleichstand nach id auf- und absteigend) – gleiche Texte beider Läufe
    = gleiche Kandidatenmenge und gleiche Rangfolge einschließlich der Gleichstände (über die random() zieht)."""
    m = re.fullmatch(r'(.*\n)  select c\.id from c\n   where (.*)\n   order by (.*), random\(\) limit 1;\n', b, re.S)
    assert m, 'Auswahltext hat nicht die erwartete Form'
    vor, w, k = m.groups()
    return (f"{vor}  select array(select c.id from c where {w} order by {k}, c.id)::text || '|' || "
            f"array(select c.id from c where {w} order by {k}, c.id desc)::text;\n")


def sq(s):
    return "'" + s.replace("'", "''") + "'"


def paket(probe, waehlen_variante=None):
    w_alt, w_neu, m_alt, m_neu = waehlen_alt(), waehlen_neu(waehlen_variante), mischkarten_alt(), mischkarten_neu()
    assert (md5(w_alt), len(w_alt)) == WAEHLEN_ALT and (md5(m_alt), len(m_alt)) == MISCH_ALT, 'Repo-Stand passt nicht zu den eingetragenen Alt-Hashes'
    for t in [w_neu, m_neu] + [h[3] for h in HILFEN]:
        assert '$' not in t
    r_alt, r_neu = rang(w_alt), rang(w_neu)
    helfer_decl = '\n'.join(f"    ({sq(s)}, {sq(md5(t))})," for s, _, _, t, _ in HILFEN).rstrip(',')
    bezug_decl = ',\n'.join(f"    ({sq(s)}, {sq(md5(f()))})" for s, f in BEZUG)
    soll_decl = ',\n'.join(f"    ({sq(s)}, {sq(v)})" for s, v in SOLL.items())
    regel_decl = ',\n'.join(f"    ({sq(k)}, {sq(w)}::jsonb, {lo}, {hi}, {sq(h)})" for k, w, lo, hi, h in REGELN)
    anlegen = '\n'.join(f"""    execute $fbx$
create or replace function {kopf}{art}as $function${t}$function$
$fbx$;
    execute $fbx$revoke all on function {s} from public$fbx$;
    if exists (select 1 from pg_roles where rolname = 'anon') then execute $fbx$revoke all on function {s} from anon$fbx$; end if;
    if exists (select 1 from pg_roles where rolname = 'authenticated') then execute $fbx$revoke all on function {s} from authenticated$fbx$; end if;
    execute $fbx$comment on function {s} is {sq(c)}$fbx$;""" for s, kopf, art, t, c in HILFEN)
    titel = 'Probelauf – rollt am Ende ALLES zurück' if probe else 'Einspielen'
    if probe:
        ende = ("  raise exception 'FB-S PROBELAUF bestanden – % – ALLES zurückgerollt (nichts eingespielt). Details: %', v_kurz, v_bericht::text;\n")
    else:
        ende = ("  drop function pg_temp.fb_rang_alt(bigint, bigint, text, boolean);\n  drop function pg_temp.fb_rang_neu(bigint, bigint, text, boolean);\n"
                "  raise notice 'FB-S eingespielt – % – Details: %', v_kurz, v_bericht::text;\n")
    s = f"""-- FB-S Fehler-Bordkarten ({titel}). Erzeugt von tools/tests/fb_einspielen.py – nicht von Hand ändern. Regel und Ablauf: inhalte/plan/fehlerkarten.md.
-- Was: Eine Übungsaufgabe, deren jüngste Bearbeitung das Kind nicht selbst gelöst hat (falsch, mit Tipp oder erst im 2. Anlauf), kommt in Wiederholung und
-- Mischkarte zuerst – nach fehlerkarten_pause_lerntage Lerntagen Pause (die Sperre der letzten 3 Lerntage gilt weiter), höchstens fehlerkarten_max-mal in Folge,
-- erledigt nach einer eigenen Lösung. Ohne Kennzeichnung (die App bleibt unverändert). Schalter fehlerkarten_an: 0 aus (beim Einspielen), 1 an, 2 nur Testkinder.
-- Geändert: schule.wdh_aufgabe_waehlen (eine Stelle: erster Sortierschlüssel), schule.mischkarten (eine Stelle: „schon beantwortet“ bei eingeschaltetem
-- Schalter nur seit der Ausgabe – sonst verfiele eine ausgegebene Fehler-Bordkarte beim nächsten Laden). Neu: schule.fehlerkarte_regel/_an/_ab/_serie/_faellig.
-- Schutz: je Funktion genau zwei zulässige Zustände (alt -> ersetzen, neu -> nichts; neue Hilfen: fehlt -> anlegen, neu -> nichts); alles andere, auch ein
-- Zwischenzustand, = Abbruch. Alle Katalogeigenschaften vorher/nachher gegen festes Soll; Rechte der ersetzten Funktionen unverändert. Bezugsfunktionen nur lesend.
-- Vergleich mit Schalter AUS: Kandidatenmenge und Rangfolge (ohne Zufall, Gleichstände nach id auf- und absteigend) alt gegen neu für alle Karten aller
-- Kinder × (Wiederholung, Mischkarte) in EINER Anweisung (ein Schnappschuss – laufende Antworten stören nicht); jede Abweichung = Abbruch.
-- Danach innerhalb der Transaktion Schalter AN: nur Zahlen (keine Lerndaten), Schalter wird auf den vorherigen Wert zurückgesetzt.
-- alt-md5 wdh_aufgabe_waehlen {md5(w_alt)} (Länge {len(w_alt)}) -> neu {md5(w_neu)} (Länge {len(w_neu)});
-- alt-md5 mischkarten {md5(m_alt)} (Länge {len(m_alt)}) -> neu {md5(m_neu)} (Länge {len(m_neu)}).
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT, keine Untertransaktion. Keine Lernpause nötig (keine Tabellen-DDL, nur Funktionen und drei Regel-Zeilen).
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $fb$
declare
  m_w_alt constant text := '{md5(w_alt)}'; m_w_neu constant text := '{md5(w_neu)}';
  m_m_alt constant text := '{md5(m_alt)}'; m_m_neu constant text := '{md5(m_neu)}';
  v_w constant text := 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)'; v_m constant text := 'schule.mischkarten(bigint, bigint, integer)';
  fehler text[] := '{{}}'; r record; d text; st jsonb := '{{}}'; ei_vor jsonb := '{{}}'; acl_vor jsonb := '{{}}'; n_alt int := 0; n_neu int := 0; n_sonst int := 0;
  v_an_vorher jsonb; n_k int; n_e int; n_v int; n_abw int; n_da int; n_kinder int; t0 timestamptz; ms_aus numeric; ms_an numeric; zz jsonb; v_bericht jsonb; v_kurz text;
begin
  if to_regclass('schule.aufgabe') is null or to_regclass('schule.versuch') is null or to_regclass('schule.karte_stand') is null or to_regclass('schule.lernender') is null
     or to_regclass('schule.lerntag') is null or to_regclass('schule.regel') is null or to_regclass('schule.misch_ausgabe') is null or to_regclass('schule.einheit') is null then
    raise exception 'FB-S ABBRUCH, Vorbedingung: eine der Tabellen aufgabe/versuch/karte_stand/lernender/lerntag/regel/misch_ausgabe/einheit fehlt – nichts geändert'; end if;
  for r in select * from (values ('versuch', 'lernender_id'), ('versuch', 'aufgabe_id'), ('versuch', 'am'), ('versuch', 'richtig'), ('versuch', 'hilfe'), ('versuch', 'anlauf'),
                                 ('versuch', 'testsitzung_id'), ('versuch', 'id'), ('aufgabe', 'form'), ('aufgabe', 'zaehlt'), ('aufgabe', 'stufe'), ('lernender', 'ist_test'),
                                 ('lernender', 'zeitzone'), ('misch_ausgabe', 'ausgegeben_am'), ('regel', 'wert')) x(t, s) loop
    if not exists (select 1 from information_schema.columns c where c.table_schema = 'schule' and c.table_name = r.t and c.column_name = r.s) then
      fehler := fehler || format('Spalte fehlt: schule.%s.%s', r.t, r.s); end if;
  end loop;
  -- 1. Zustand und Eigenschaften je Funktion gegen festes Soll
  create temp table if not exists fb_soll (f text primary key, ei text) on commit drop;
  truncate fb_soll;
  insert into fb_soll values
{soll_decl};
  create temp table if not exists fb_neu (f text primary key, m text) on commit drop;
  truncate fb_neu;
  insert into fb_neu values
{helfer_decl};
  for r in select s.f, s.ei, to_regprocedure(s.f) o from fb_soll s order by s.f collate "C" loop
    if r.o is null then
      if r.f in (select f from fb_neu) then st := st || jsonb_build_object(r.f, 'fehlt'); n_alt := n_alt + 1;
      else fehler := fehler || format('Funktion fehlt: %s', r.f); end if;
      continue;
    end if;
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    ei_vor := ei_vor || jsonb_build_object(r.f, v_kurz);
    acl_vor := acl_vor || jsonb_build_object(r.f, (select coalesce(p.proacl::text, '') from pg_proc p where p.oid = r.o));
    if v_kurz is distinct from r.ei then fehler := fehler || format('%s: Eigenschaften %s, erwartet %s', r.f, v_kurz, r.ei); end if;
    if r.f = v_w then
      if md5(d) = m_w_alt then st := st || jsonb_build_object(r.f, 'alt'); n_alt := n_alt + 1;
      elsif md5(d) = m_w_neu then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      else fehler := fehler || format('%s weicht ab (md5 %s, Länge %s; erwartet %s oder %s)', r.f, md5(d), length(d), m_w_alt, m_w_neu); n_sonst := n_sonst + 1; end if;
    elsif r.f = v_m then
      if md5(d) = m_m_alt then st := st || jsonb_build_object(r.f, 'alt'); n_alt := n_alt + 1;
      elsif md5(d) = m_m_neu then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      else fehler := fehler || format('%s weicht ab (md5 %s, Länge %s; erwartet %s oder %s)', r.f, md5(d), length(d), m_m_alt, m_m_neu); n_sonst := n_sonst + 1; end if;
    elsif r.f in (select f from fb_neu) then
      if md5(d) = (select m from fb_neu where f = r.f) then st := st || jsonb_build_object(r.f, 'neu'); n_neu := n_neu + 1;
      else fehler := fehler || format('%s ist vorhanden, aber nicht im neuen Stand (md5 %s)', r.f, md5(d)); n_sonst := n_sonst + 1; end if;
    end if;
  end loop;
  -- Bezugsfunktionen (werden nicht geändert; die Regel stützt sich auf genau diese Fassung)
  for r in select * from (values
{bezug_decl}) x(f, m) loop
    if to_regprocedure(r.f) is null then fehler := fehler || format('Bezugsfunktion fehlt: %s', r.f); continue; end if;
    select md5(p.prosrc) into d from pg_proc p where p.oid = to_regprocedure(r.f);
    if d is distinct from r.m then fehler := fehler || format('Bezugsfunktion %s weicht vom Repo-Stand ab (md5 %s, erwartet %s)', r.f, d, r.m); end if;
  end loop;
  if n_sonst = 0 and n_alt > 0 and n_neu > 0 then
    fehler := fehler || format('Zwischenzustand (%s Funktionen alt/fehlend, %s neu): %s', n_alt, n_neu, st::text); end if;
  -- Regeln: fehlen oder gültig
  create temp table if not exists fb_regel (k text primary key, w jsonb, lo int, hi int, h text) on commit drop;
  truncate fb_regel;
  insert into fb_regel values
{regel_decl};
  for r in select g.k, g.lo, g.hi, x.wert from fb_regel g join schule.regel x on x.schluessel = g.k loop
    if jsonb_typeof(r.wert) is distinct from 'number' or (r.wert #>> '{{}}')::numeric not between r.lo and r.hi or (r.wert #>> '{{}}')::numeric <> trunc((r.wert #>> '{{}}')::numeric) then
      fehler := fehler || format('Regel %s hat einen ungültigen Wert %s (erlaubt ganze Zahl %s–%s)', r.k, r.wert, r.lo, r.hi); end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'FB-S ABBRUCH, Vorbedingung (% Befunde), nichts geändert: %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 2. Regeln anlegen (ein vorhandener Wert bleibt), Funktionen ersetzen/anlegen (nur im Zustand alt)
  insert into schule.regel (schluessel, wert, hinweis) select g.k, g.w, g.h from fb_regel g order by g.k on conflict (schluessel) do nothing;
  if n_alt > 0 then
{anlegen}
    execute $fbx$
create or replace function schule.wdh_aufgabe_waehlen(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns bigint language sql volatile set search_path to ''
as $function${w_neu}$function$
$fbx$;
    execute $fbx$
create or replace function schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl integer default 8)
 returns jsonb language plpgsql set search_path to ''
as $function${m_neu}$function$
$fbx$;
  end if;

  -- 3. Nachher: alle im neuen Stand, Eigenschaften = Soll, Rechte der ersetzten Funktionen unverändert, neue Hilfen nicht für public/anon/authenticated
  for r in select s.f, s.ei, to_regprocedure(s.f) o from fb_soll s order by s.f collate "C" loop
    if r.o is null then fehler := fehler || format('nachher fehlt: %s', r.f); continue; end if;
    select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), pg_get_function_result(p.oid), l.lanname, p.provolatile, p.prosecdef, p.proisstrict, p.proretset,
                     p.proparallel, p.procost, p.prorows, p.proleakproof, coalesce(p.proconfig::text, ''))
      into d, v_kurz from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    if v_kurz is distinct from r.ei then fehler := fehler || format('nachher %s: Eigenschaften %s, erwartet %s', r.f, v_kurz, r.ei); end if;
    if r.f = v_w and md5(d) <> m_w_neu then fehler := fehler || format('nachher %s: md5 %s statt %s', r.f, md5(d), m_w_neu); end if;
    if r.f = v_m and md5(d) <> m_m_neu then fehler := fehler || format('nachher %s: md5 %s statt %s', r.f, md5(d), m_m_neu); end if;
    if r.f in (select f from fb_neu) then
      if md5(d) <> (select m from fb_neu where f = r.f) then fehler := fehler || format('nachher %s: md5 %s', r.f, md5(d)); end if;
      if (select coalesce(p.proacl::text, '') from pg_proc p where p.oid = r.o) ~ '(^|[{{,])=' then fehler := fehler || format('nachher %s: für public ausführbar', r.f); end if;
      if exists (select 1 from pg_roles where rolname in ('anon', 'authenticated') and has_function_privilege(rolname, r.o, 'execute')) then
        fehler := fehler || format('nachher %s: für anon/authenticated ausführbar', r.f); end if;
    elsif ei_vor ? r.f and (select coalesce(p.proacl::text, '') from pg_proc p where p.oid = r.o) is distinct from acl_vor->>r.f then
      fehler := fehler || format('nachher %s: Rechte geändert', r.f);
    end if;
  end loop;
  if array_length(fehler, 1) > 0 then raise exception 'FB-S ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;

  -- 4. Vergleich mit Schalter AUS: alte gegen neue Auswahl ohne Zufall (Probe-Kopien im temporären Schema, aus den geprüften Texten)
  execute $fbx$
create or replace function pg_temp.fb_rang_alt(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns text language sql stable set search_path to ''
as $function${r_alt}$function$
$fbx$;
  execute $fbx$
create or replace function pg_temp.fb_rang_neu(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns text language sql stable set search_path to ''
as $function${r_neu}$function$
$fbx$;
  select x.wert into v_an_vorher from schule.regel x where x.schluessel = 'fehlerkarten_an';
  update schule.regel set wert = '0'::jsonb where schluessel = 'fehlerkarten_an';
  create temp table if not exists fb_v (l bigint, e bigint, lz text, misch boolean, sitzt boolean, faellig boolean, alt text, neu text, da boolean, ok_e boolean) on commit drop;
  truncate fb_v;
  insert into fb_v   -- EINE Anweisung = ein Schnappschuss für alt und neu
  select k.lernender_id, k.einheit_id, k.lernziel, m.misch, coalesce(k.sitzt, false), coalesce(schule.karte_faellig(k), false),
         pg_temp.fb_rang_alt(k.lernender_id, k.einheit_id, k.lernziel, m.misch), pg_temp.fb_rang_neu(k.lernender_id, k.einheit_id, k.lernziel, m.misch),
         case when not m.misch then schule.wdh_aufgabe_da(k.lernender_id, k.einheit_id, k.lernziel) end,
         exists (select 1 from schule.einheit e where e.id = k.einheit_id and e.status in ('geprueft', 'freigegeben'))
    from schule.karte_stand k cross join (values (false), (true)) m(misch);
  select count(distinct l), count(distinct (l, e, lz)), count(*), count(*) filter (where alt is distinct from neu),
         count(*) filter (where not misch and da is distinct from (ok_e and neu not like '{{}}|%'))
    into n_kinder, n_e, n_v, n_abw, n_da from fb_v;
  if n_abw > 0 then
    raise exception 'FB-S ABBRUCH, alles zurückgerollt: mit Schalter AUS weicht die Auswahl in % von % Fällen ab (z. B. %)', n_abw, n_v,
      (select string_agg(format('Kind %s Einheit %s %s %s', l, e, lz, case when misch then 'Mischkarte' else 'Wiederholung' end), '; ')
         from (select * from fb_v where alt is distinct from neu order by l, e, lz collate "C", misch limit 5) z); end if;
  t0 := clock_timestamp();
  perform count(schule.wdh_aufgabe_waehlen(k.lernender_id, k.einheit_id, k.lernziel, false)) from schule.karte_stand k where k.sitzt;
  ms_aus := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);

  -- 5. Schalter AN (nur in dieser Transaktion): nur Zahlen
  update schule.regel set wert = '1'::jsonb where schluessel = 'fehlerkarten_an';
  create temp table if not exists fb_a (l bigint, e bigint, lz text, sitzt boolean, faellig boolean, r0 text, r1 text, da boolean) on commit drop;
  truncate fb_a;
  insert into fb_a
  select k.lernender_id, k.einheit_id, k.lernziel, coalesce(k.sitzt, false), coalesce(schule.karte_faellig(k), false),
         pg_temp.fb_rang_neu(k.lernender_id, k.einheit_id, k.lernziel, false), pg_temp.fb_rang_neu(k.lernender_id, k.einheit_id, k.lernziel, true),
         schule.wdh_aufgabe_da(k.lernender_id, k.einheit_id, k.lernziel)
    from schule.karte_stand k;
  if exists (select 1 from fb_a a join fb_v v on v.l = a.l and v.e = a.e and v.lz = a.lz and not v.misch where a.da is distinct from v.da) then
    raise exception 'FB-S ABBRUCH, alles zurückgerollt: wdh_aufgabe_da ändert sich mit dem Schalter'; end if;
  if exists (select 1 from fb_a a join fb_v v on v.l = a.l and v.e = a.e and v.lz = a.lz and not v.misch
              where (a.r0 like '{{}}|%') is distinct from (v.neu like '{{}}|%')) then
    raise exception 'FB-S ABBRUCH, alles zurückgerollt: mit Schalter AN hat eine Etappe eine andere Kandidatenmenge (leer/nicht leer)'; end if;
  with t as (select a.*, (string_to_array(trim(both '{{}}' from split_part(a.r0, '|', 1)), ','))[1]::bigint t0, (string_to_array(trim(both '{{}}' from split_part(a.r1, '|', 1)), ','))[1]::bigint t1 from fb_a a),
  f as (select t.*, t.t0 is not null and schule.fehlerkarte_faellig(t.l, t.t0, (select max(v.am) from schule.versuch v where v.lernender_id = t.l and v.aufgabe_id = t.t0)) fb0,
               t.t1 is not null and schule.fehlerkarte_faellig(t.l, t.t1, (select max(v.am) from schule.versuch v where v.lernender_id = t.l and v.aufgabe_id = t.t1)) fb1 from t)
  select jsonb_build_object(
      'etappen_mit_faelliger_fehlerkarte_je_kind', coalesce((select jsonb_object_agg(q.l::text, q.n) from (select l, count(*) n from f where sitzt and fb0 group by l) q), '{{}}'::jsonb),
      'davon_heute_in_der_wiederholung_faellig_je_kind', coalesce((select jsonb_object_agg(q.l::text, q.n) from (select l, count(*) n from f where sitzt and faellig and fb0 group by l) q), '{{}}'::jsonb),
      'mischkarten_etappen_mit_fehlerkarte', (select count(*) from f where sitzt and fb1))
    into zz;
  zz := zz || (with p as (
      select v.lernender_id l, v.aufgabe_id a, max(v.am) zuletzt from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
       where a.pool = 'uebung' and a.freigegeben and schule.aufgabe_zaehlt(a) and v.testsitzung_id is null group by v.lernender_id, v.aufgabe_id),
    s as (select p.*, schule.fehlerkarte_serie(p.l, p.a) serie, (select a.form = 'lueckenweg' from schule.aufgabe a where a.id = p.a) lw,
                 (select coalesce(a.stufe, 2) from schule.aufgabe a where a.id = p.a) stufe from p)
    select jsonb_build_object(
      'fehler_aufgaben_offen', count(*) filter (where serie between 1 and schule.fehlerkarte_regel('fehlerkarten_max', 3) and lw is not true),
      'fehler_aufgaben_heute_faellig', count(*) filter (where schule.fehlerkarte_faellig(l, a, zuletzt) and schule.lern_datum(l, zuletzt) < schule.wdh_sperre_ab(l)),
      'davon_stufe_1_nur_wiederholung', count(*) filter (where stufe = 1 and schule.fehlerkarte_faellig(l, a, zuletzt) and schule.lern_datum(l, zuletzt) < schule.wdh_sperre_ab(l)),
      'ueber_obergrenze_normal', count(*) filter (where serie > schule.fehlerkarte_regel('fehlerkarten_max', 3) and lw is not true),
      'lueckenwege_ausgenommen', count(*) filter (where serie >= 1 and lw is true),
      'kinder_mit_fehler_aufgaben', count(distinct l) filter (where serie >= 1 and lw is not true)) from s);
  t0 := clock_timestamp();
  perform count(schule.wdh_aufgabe_waehlen(k.lernender_id, k.einheit_id, k.lernziel, false)) from schule.karte_stand k where k.sitzt;
  ms_an := round(extract(epoch from clock_timestamp() - t0) * 1000, 1);
  zz := zz || jsonb_build_object('misch_offen_vorher_beantwortet', (select count(*) from schule.misch_ausgabe m where m.eingeloest_am is null and m.verfallen_am is null
                                   and exists (select 1 from schule.versuch v where v.lernender_id = m.lernender_id and v.aufgabe_id = m.aufgabe_id and v.am < m.ausgegeben_am)));
  update schule.regel set wert = v_an_vorher where schluessel = 'fehlerkarten_an';   -- Schalter zurück (beim ersten Lauf: 0)
  if (select x.wert from schule.regel x where x.schluessel = 'fehlerkarten_an') is distinct from v_an_vorher then raise exception 'FB-S ABBRUCH: Schalter nicht zurückgesetzt'; end if;

  v_kurz := format('Kinder %s, Etappen %s, Vergleiche %s, Abweichungen AUS %s | AN heute: Etappen mit fälliger Fehler-Bordkarte je Kind %s (davon heute fällig %s), Mischkarten-Etappen %s, Fehler-Aufgaben offen %s (heute fällig %s) | Laufzeit %s ms aus / %s ms an (Index versuch_kind_aufgabe_idx: %s) | %s',
    n_kinder, n_e, n_v, n_abw, zz->'etappen_mit_faelliger_fehlerkarte_je_kind', zz->'davon_heute_in_der_wiederholung_faellig_je_kind', zz->'mischkarten_etappen_mit_fehlerkarte',
    zz->'fehler_aufgaben_offen', zz->'fehler_aufgaben_heute_faellig', ms_aus, ms_an,
    case when to_regclass('schule.versuch_kind_aufgabe_idx') is null then 'nein' else 'ja' end,
    case when n_alt > 0 then 'alt -> neu' else 'neu -> neu (schon eingespielt, nichts geändert)' end);
  v_bericht := zz || jsonb_build_object('zustand_vorher', st, 'md5_wdh_aufgabe_waehlen_neu', m_w_neu, 'md5_mischkarten_neu', m_m_neu,
    'kinder', n_kinder, 'etappen', n_e, 'vergleiche', n_v, 'abweichungen_aus', n_abw, 'da_ungleich_auswahl_info', n_da,
    'schalter', (select x.wert from schule.regel x where x.schluessel = 'fehlerkarten_an'),
    'regeln', (select jsonb_object_agg(x.schluessel, x.wert) from schule.regel x where x.schluessel in (select k from fb_regel)),
    'ms_auswahl_aus', ms_aus, 'ms_auswahl_an', ms_an, 'eigenschaften_gleich', true, 'fehler', 0);
{ende}end $fb$;
"""
    return s


def dateien():
    p, e = paket(True), paket(False)
    return [('fb_s_probe.sql', p), ('fb_s_einspielen.sql', e)], e


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
    w, m = waehlen_neu(), mischkarten_neu()
    print('wdh_aufgabe_waehlen', WAEHLEN_ALT, '->', md5(w), len(w), '| mischkarten', MISCH_ALT, '->', md5(m), len(m))
    for s, f in BEZUG:
        print('Bezug', s, md5(f()), len(f()))
    for s, _, _, t, _ in HILFEN:
        print('neu', s, md5(t), len(t))


if __name__ == '__main__':
    main()
