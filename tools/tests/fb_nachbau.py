"""Kleiner NACHBAU für den FB-S-Test (lokale, leere Postgres-Instanz – NICHT die echte Datenbank).

Funktionen mit Text aus dem Repo (Grundfassung + dokumentierte Patches, Kopf wie in den Migrationen = Live-Eigenschaften):
  wdh_aufgabe_waehlen (alt), mischkarten (alt), mischkarten_waehlen, misch_gueltig, wdh_aufgabe_da (beide Fassungen), wdh_sperre_ab, lern_datum, heute_tag,
  wd_regel, etappe_heute_beantwortet, karte_faellig, versuch_wertung, wdh_fehler, wdh_runde_groesse, wdh_runde_pruefen, wdh_runde_holen, aufgabe_zaehlt.
Vereinfacht: Tabellen nur mit den benutzten Spalten, aufgabe_anzeige (nur id), keine Trigger an versuch (Lerntage und Versuche legt der Test direkt an),
wdh_runde_holen ohne die WD-5-Sperre (wdh_runde_sperre) – für die Frage „Tagesrunde unverändert“ ohne Belang.
"""
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import fb_einspielen as FB  # noqa: E402

MIG = WURZEL / 'supabase/migrations'


def kopf(datei, anfang):
    s = (MIG / datei).read_text(encoding='utf-8')
    i = s.index(anfang)
    return s[i:s.index('as $function$', i)]


def stmt(datei, anfang, b=None, umbenennen=None):
    k = kopf(datei, anfang)
    if b is None: b = FB.body(datei, anfang)
    if umbenennen: k = k.replace(*umbenennen)
    return f'{k}as $function${b}$function$;\n'


def nachbau_sql():
    t = []
    t.append(r"""
create role anon nologin;
create role authenticated nologin;
create schema schule;
create schema pruef;
create table schule.lernender (id bigint primary key, ist_test boolean not null default false, aktiv boolean not null default true, zeitzone text, klasse int);
create table schule.block (id bigint primary key, stadt text, kontinent_id bigint);
create table schule.einheit (id bigint primary key, thema_id bigint, status text not null default 'freigegeben', inhalt jsonb default '{}', block_id bigint references schule.block(id));
create table schule.aufgabe (id bigint primary key, einheit_id bigint references schule.einheit(id), variante_gruppe text, pool text not null default 'uebung',
  freigegeben boolean not null default true, stufe smallint, form text, zaehlt text, typ text, antworttyp text default 'zahl', frage jsonb default '{}', tipp text);
create table schule.versuch (id bigserial primary key, lernender_id bigint not null references schule.lernender(id), aufgabe_id bigint not null references schule.aufgabe(id),
  client_id text, antwort jsonb, richtig boolean not null, hilfe smallint, versuch_nr int, anlauf smallint, testsitzung_id bigint, misch boolean not null default false,
  am timestamptz not null default now(), wertung_fest text, wertung_offen boolean);
create table schule.lerntag (lernender_id bigint, fach text, datum date, zeitzone text, primary key (lernender_id, fach, datum));
create table schule.regel (schluessel text primary key, wert jsonb not null, hinweis text);
create table schule.karte_stand (lernender_id bigint not null references schule.lernender(id), einheit_id bigint not null references schule.einheit(id), lernziel text not null,
  richtig int not null default 0, falsch int not null default 0, sitzt boolean not null default false, sitzt_am timestamptz, wdh_stufe smallint not null default 0,
  faellig_am timestamptz, zuletzt timestamptz, wdh_fehler smallint not null default 0, wdh_ab timestamptz, wdh_lerntage smallint, primary key (lernender_id, einheit_id, lernziel));
create table schule.misch_ausgabe (id bigint generated always as identity primary key, lernender_id bigint not null references schule.lernender(id),
  aufgabe_id bigint not null references schule.aufgabe(id), ausgegeben_am timestamptz not null default now(), eingeloest_am timestamptz,
  einheit_id bigint references schule.einheit(id), lernziel text, verfallen_am timestamptz);
create unique index misch_ausgabe_offen_eindeutig on schule.misch_ausgabe (lernender_id, aufgabe_id) where eingeloest_am is null;
create table schule.wdh_runde (lernender_id bigint not null references schule.lernender(id), tag date not null, ziel integer not null default 0, faellig integer not null default 0,
  angelegt_am timestamptz not null default now(), fertig_am timestamptz, primary key (lernender_id, tag));
create table schule.wdh_runde_etappe (lernender_id bigint not null, tag date not null, nr integer not null, einheit_id bigint not null, lernziel text not null,
  bearbeitet_am timestamptz, primary key (lernender_id, tag, einheit_id, lernziel), foreign key (lernender_id, tag) references schule.wdh_runde (lernender_id, tag));
create or replace function schule.aufgabe_zaehlt(a schule.aufgabe)
 returns boolean language sql immutable set search_path to ''
as $function$
  select a.zaehlt is distinct from 'nein';
$function$;
create or replace function schule.aufgabe_anzeige(a schule.aufgabe, p_mit_tipp boolean) returns jsonb language sql stable set search_path to '' as $$ select jsonb_build_object('id', a.id) $$;
""")
    t.append(stmt('20261122_wd_s_wiederholungen.sql', 'create or replace function schule.wd_regel('))
    t.append(stmt('20261120_i2_lernregeln.sql', 'create or replace function schule.heute_tag('))
    t.append(stmt('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.wdh_sperre_ab('))
    t.append(stmt('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.lern_datum('))
    t.append(stmt('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.etappe_heute_beantwortet('))
    t.append(stmt('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.wdh_aufgabe_waehlen(', FB.waehlen_alt()))
    t.append(stmt('20261122_wd_s4_nacharbeit_921.sql', 'create or replace function schule.wdh_aufgabe_da(', FB.da_alt()))
    t.append(stmt('20261122_wd_s_wiederholungen.sql', 'create or replace function schule.wdh_aufgabe_da(', FB.ftsp(FB.body('20261122_wd_s_wiederholungen.sql', 'create or replace function schule.wdh_aufgabe_da('))))
    t.append(stmt('20261116_w150_r3_wiederholung_lerntage.sql', 'create or replace function schule.karte_faellig('))
    t.append(stmt('20261120_i3_lernregeln_nachpruefung.sql', 'create or replace function schule.versuch_wertung('))
    t.append(stmt('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.wdh_fehler('))
    t.append(stmt('20261122_wd_s_wiederholungen.sql', 'create or replace function schule.wdh_runde_groesse('))
    t.append(stmt('20261122_wd_s4_nacharbeit_921.sql', 'create or replace function schule.wdh_runde_pruefen('))
    t.append(stmt('20261122_wd_s3_frische_aufgaben.sql', 'create or replace function schule.wdh_runde_holen('))
    t.append(stmt('20261118_w176_t3_mischkarten.sql', 'create or replace function schule.mischkarten(', FB.mischkarten_waehlen_alt(),
                  ('function schule.mischkarten(', 'function schule.mischkarten_waehlen(')))
    t.append(stmt('20261120_i4_misch_ausgabe_wieder.sql', 'create or replace function schule.mischkarten(', FB.mischkarten_alt()))
    t.append(stmt('20261120_i4_misch_ausgabe_wieder.sql', 'create or replace function schule.misch_gueltig(', FB.misch_gueltig_alt()))
    t.append("""
insert into schule.regel values ('wdh_sperre_lerntage', '3', 'WD-S 3'), ('wdh_nur_selbst', 'true', 'WD-S 3');
revoke all on function schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean) from public;
""")
    return '\n'.join(t)


def rang_sql():
    """Test-Hilfen (Schema pruef): Rangfolge ohne Zufall wie im Paket, alt und neu."""
    return (f"create or replace function pruef.rang_alt(p_l bigint, p_e bigint, p_lz text, p_misch boolean) returns text language sql stable set search_path to '' "
            f"as $function${FB.rang(FB.waehlen_alt())}$function$;\n"
            f"create or replace function pruef.rang_neu(p_l bigint, p_e bigint, p_lz text, p_misch boolean) returns text language sql stable set search_path to '' "
            f"as $function${FB.rang(FB.waehlen_neu())}$function$;\n")
