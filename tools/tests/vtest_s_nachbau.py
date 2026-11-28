"""Nachbau für den Test von VTEST-S (lokale Postgres-Instanz, NICHT die echte Datenbank, erfundene Daten).
Grundlage: Schema und Hilfsfunktionen aus tools/tests/tempo_nachbau.sql (ohne dessen Daten), dazu die Funktionen im Stand NACH NF-S, TEMPO-S1 und FB-S
mit genau den Funktionstexten, die das Paket per md5 verlangt (test_starten_intern = NF-S neu, etappen_stand = TEMPO-S1 neu, karte_landet = LB-3 + FT-S,
wdh_aufgabe_waehlen/mischkarten = FB-S neu – die beiden nur als Text, sie werden hier nicht aufgerufen). karte_buchen: Fassung H-Muss (19.11.) mit dem FT-S-Filter
und der Landeregel-Stelle der LB-3-Nachbesserung (vereinfacht: ohne gesetzte Etappen, ohne landung_speichern); Trigger bucht jede Übungsantwort."""
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
import fb_einspielen as FB  # noqa: E402
import nf_einspielen as NF  # noqa: E402
import vtest_s_einspielen as VS  # noqa: E402

MIG = WURZEL / 'supabase/migrations'


def auszug(datei, anfang, ende='end $function$;'):
    s = (MIG / datei).read_text(encoding='utf-8')
    i = s.index(anfang)
    return s[i:s.index(ende, i) + len(ende)]


def karte_buchen():
    kb = auszug('20261119_w176_h_muss.sql', 'create or replace function schule.karte_buchen(')
    kb = VS.rep(kb, "if a.id is null or a.pool <> 'uebung' then return; end if;",
                "if a.id is null or a.pool <> 'uebung' or not schule.aufgabe_zaehlt(a) then return; end if;")                      # FT-S
    kb = VS.rep(kb, 'v_eigen boolean; v_neu boolean;', 'v_eigen boolean; v_neu boolean; v_war_gelandet boolean;')
    kb = VS.rep(kb, '  if not k.sitzt then\n    if v_eigen then', '  v_war_gelandet := k.sitzt;\n  if not k.sitzt then\n    if v_eigen then')
    kb = VS.rep(kb, ('    if k.eigene_loesungen >= v_ziel\n       and coalesce(array_length(k.typen, 1), 0) >= schule.karte_typen_noetig(a.einheit_id, a.variante_gruppe)\n'
                     '       and (k.schwer_ok or not schule.karte_schwer_noetig(a.einheit_id, a.variante_gruppe))\n       and k.folge >= least(3, v_ziel) then'),
                '    ' + VS.KARTE_BUCHEN_STELLE + ' -- gemeinsame Landeregel (LB-3)')
    return kb


def sql():
    t = (WURZEL / 'tools/tests/tempo_nachbau.sql').read_text(encoding='utf-8')
    t = t[:t.index('-- ---------- erfundene Daten ----------')]
    nt = (MIG / '20261124_nt_s_nachtest_menge.sql').read_text(encoding='utf-8')
    i = nt.index('create or replace function schule.nachtest_je_etappe(')
    je = nt[i:nt.index('$function$;', nt.index('as $function$', i)) + len('$function$;')]
    return t + f"""
-- ---------- VTEST-S: Ergänzungen ----------
alter table schule.regel add column hinweis text;
alter table schule.aufgabe add column form text, add column antworttyp text not null default 'zahl';
alter table schule.testsitzung add column aufgaben bigint[] not null default '{{}}', add column status text, add column gestartet_am timestamptz default now(),
  add column block_id bigint, add column thema_id bigint, add column nachtest_runde smallint, add column punkte_max int, add column regel_version int;
insert into schule.regel (schluessel, wert) values ('anwenden_pflicht', '0');
create function schule.lernziele_anlegen(p_l bigint, p_e bigint) returns void language sql set search_path to '' as $$ select null::void $$;
create function schule.offene_entscheiden(p_l bigint) returns void language sql set search_path to '' as $$ select null::void $$;
create function schule.lerntage_seit(p_l bigint, p_t timestamptz) returns int language sql stable set search_path to '' as $$ select 30 $$;
create function schule.aufgabe_anzeige(a schule.aufgabe, p_mit_tipp boolean) returns jsonb language sql stable set search_path to '' as $$
  select jsonb_build_object('id', a.id, 'typ', a.typ, 'form', a.form) $$;
{je}
create function schule.nachtest_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
 returns bigint[] language sql stable set search_path to ''
as $function${NF.auswahl_neu()}$function$;
create function schule.nachtest_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function${NF.stand_neu()}$function$;
create function schule.test_starten_intern(p_lernender bigint, p_daten jsonb)
 returns jsonb language plpgsql set search_path to ''
as $function${VS.tsi_alt()}$function$;
create function schule.etappen_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language sql stable set search_path to ''
as $function${VS.es_alt()}$function$;
create function schule.karte_landet(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function${VS.kl_alt()}$function$;
set check_function_bodies = off;
create function schule.wdh_aufgabe_waehlen(p_l bigint, p_e bigint, p_lz text, p_misch boolean)
 returns bigint language sql volatile set search_path to ''
as $function${FB.waehlen_neu()}$function$;
create function schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl integer default 8)
 returns jsonb language plpgsql volatile set search_path to ''
as $function${FB.mischkarten_neu()}$function$;
reset check_function_bodies;
{karte_buchen()}
create function schule.versuch_karte() returns trigger language plpgsql set search_path to '' as $$
begin
  if new.testsitzung_id is null then perform schule.karte_buchen(new.lernender_id, new.aufgabe_id, new.richtig, coalesce(new.hilfe, 0)::smallint, new.am); end if;
  return new;
end $$;
create trigger versuch_karte after insert on schule.versuch for each row execute function schule.versuch_karte();
revoke all on function schule.test_starten_intern(bigint, jsonb), schule.etappen_stand(bigint, bigint), schule.karte_landet(schule.karte_stand) from public;
grant execute on function schule.etappen_stand(bigint, bigint) to authenticated;
"""
