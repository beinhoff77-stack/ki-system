"""Nachbau-Bausteine für die Tests von NF-S und der Bestands-Berichtigung 1 (lokale Postgres-Instanz, NICHT die echte Datenbank).
Die ALTEN Fassungen von schule.nachtest_auswahl (aus 20261124_nt_s_nachtest_menge.sql) und schule.nachtest_stand (Live-Funktionstext, tools/tests/nf_nachtest_stand_alt.prosrc.txt)
werden mit genau den Eigenschaften angelegt, die live gelten (STABLE, Invoker, nicht STRICT, search_path = ''); ihre Abhängigkeiten sind vereinfacht nachgebaut."""
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import nf_einspielen as NF  # noqa: E402


def nachtest_sql():
    mig = (WURZEL / 'supabase/migrations/20261124_nt_s_nachtest_menge.sql').read_text(encoding='utf-8')
    i = mig.index('create or replace function schule.nachtest_je_etappe(')
    je = mig[i:mig.index('$function$;', mig.index('as $function$', i)) + len('$function$;')]
    return f"""
create table if not exists schule.testsitzung (id bigserial primary key, lernender_id bigint, art text, einheit_id bigint, aufgaben bigint[], status text,
  ergebnis text, gestartet_am timestamptz default now(), abgeschlossen_am timestamptz);
create table if not exists schule.misch_ausgabe (id bigserial primary key, lernender_id bigint not null references schule.lernender(id), aufgabe_id bigint not null references schule.aufgabe(id),
  ausgegeben_am timestamptz not null default now(), eingeloest_am timestamptz, verfallen_am timestamptz);
create table if not exists schule.lernziel_stand (lernender_id bigint, einheit_id bigint, lernziel text, status text, pflicht boolean default true);
create or replace function schule.flug_ohne_test(p_l bigint, p_e bigint) returns boolean language sql stable set search_path to '' as $$ select false $$;
create or replace function schule.zusatz_eingeplant(p_l bigint, p_t bigint) returns boolean language sql stable set search_path to '' as $$ select false $$;
create or replace function schule.lerntage_seit(p_l bigint, p_t timestamptz) returns int language sql stable set search_path to '' as $$ select 30 $$;
{je}
create or replace function schule.nachtest_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
 returns bigint[] language sql stable set search_path to ''
as $function${NF.auswahl_alt()}$function$;
create or replace function schule.nachtest_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function${NF.stand_alt()}$function$;
-- die vier Karten-Funktionen wie in den Migrationen (karte_ziel: 20261116 sitzt_regel_6; typen: t1_punkteregel; schwer; anwenden: ft_s)
create or replace function schule.karte_ziel(p_einheit bigint, p_lz text) returns integer language sql stable set search_path to ''
as $function$ select least(6, greatest(2, count(*)))::int from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben; $function$;
create or replace function schule.karte_typen_noetig(p_einheit bigint, p_lz text) returns integer language sql stable set search_path to ''
as $function$ select least(2, count(distinct a.typ))::int from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and a.typ is not null; $function$;
create or replace function schule.karte_schwer_noetig(p_einheit bigint, p_lz text) returns boolean language sql stable set search_path to ''
as $function$ select exists (select 1 from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and a.stufe = 3); $function$;
create or replace function schule.karte_anwenden_noetig(p_einheit bigint, p_lz text) returns boolean language sql stable set search_path to ''
as $function$ select exists (select 1 from schule.aufgabe a where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and schule.aufgabe_zaehlt(a)
  and a.typ in ('einkleidung', 'transfer', 'pruefung')); $function$;
"""
