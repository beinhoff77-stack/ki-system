-- TEMPO-S1 (Bau-Auftrag Ladezeiten, ENTWURF – nicht eingespielt): schule_merkheft schneller, Ergebnis byte-gleich.
-- Analyse: inhalte/plan/ladezeiten.md. Einspielen NUR über das Paket tools/tests/aus/tempo_s1_einspielen.sql (eine Transaktion, prüft sich selbst:
-- vergleicht vorher/nachher je Kind und Einheit per md5 und bricht bei jeder Abweichung ab); Probe: tools/tests/aus/tempo_s1_probe.sql (rollt alles zurück).
--
-- Befund (live gemessen vom Projektleiter): api.schule_merkheft ruft je Einheit schule.etappen_stand auf, 95 Einheiten ≈ 3,7 s (≈ 39 ms je Einheit).
-- etappen_stand rechnet je Etappe (Lernziel) bis zu zehn Unterabfragen über schule.aufgabe und schule.versuch:
--   gesamt, geloest, karte_ziel (zweimal: ziel und folge_ziel), karte_typen_noetig, karte_schwer_noetig, karte_anwenden_pflicht → karte_anwenden_noetig,
--   karte_bearbeitungen, karte_sicher, dazu flug_nachtest(Kind, Einheit) – das ist je Einheit gleich, wurde aber je Etappe neu gerechnet.
--   Im Repo gibt es keinen Index auf schule.aufgabe(einheit_id …) und keinen auf schule.versuch(lernender_id, aufgabe_id) (live bekannt sind nur die
--   eindeutigen Indizes, supabase/tests/nachbau_live_constraints.sql). Ohne sie ist jede dieser Unterabfragen ein Lauf über die ganze Tabelle.
--
-- WAS:
--  1. Index schule.aufgabe (einheit_id, pool, variante_gruppe) – für alle Etappen-Hilfen (alle filtern einheit_id, pool, variante_gruppe).
--  2. Index schule.versuch (lernender_id, aufgabe_id) – für geloest und karte_bearbeitungen (Versuche eines Kindes zu Aufgaben einer Einheit).
--  3. schule.etappen_stand neu (create or replace), gleiches Ergebnis:
--     - flug_nachtest(Kind, Einheit) einmal je Aufruf statt je Etappe (Unterabfrage mit offset 0, damit der Planer sie nicht je Zeile einsetzt),
--     - karte_ziel einmal je Etappe (für ziel und folge_ziel),
--     - gesamt und geloest je Einheit in EINER gruppierten Abfrage statt je Etappe,
--     - alle übrigen Hilfsfunktionen unverändert dieselben (Regeln bleiben an einer Stelle).
--     Nur wenn die eingespielte Fassung genau die aus dem Repo ist (md5 des Funktionstexts, nachgerechnet aus den Migrationen 20261114 … 20261203);
--     sonst Abbruch ohne Änderung. Schon umgestellt (Marke TEMPO-S1) → nichts tun.
-- WAS NICHT: keine Tabelle, keine Spalte, kein Trigger, keine andere Funktion; kein DROP, kein DELETE, kein UPDATE; api.schule_merkheft bleibt, wie sie ist
--   (Antwort unverändert; Vorschlag für eine schlankere Antwort nur in der Analyse). Wiederholbar: ein zweiter Lauf ändert nichts.
-- Hinweis Index im selben Lauf: Postgres nutzt einen neuen Index in der anlegenden Transaktion u. U. noch nicht (indcheckxmin); die Laufzeit „nachher“
--   in Probe/Einspiel-Paket ist dann zu hoch. Maßgeblich ist die Messung danach (tools/tests/aus/tempo_s1_messen.sql, nur lesend).

select set_config('lock_timeout', '3s', true);

create index if not exists aufgabe_einheit_pool_lz_idx on schule.aufgabe (einheit_id, pool, variante_gruppe);
create index if not exists versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id);

do $tempo$
declare d text := (select p.prosrc from pg_proc p where p.oid = to_regprocedure('schule.etappen_stand(bigint, bigint)'));
  v_soll constant text := 'bf3152e9a378a1d4e41c98965acf738e';   -- md5 des Funktionstexts nach 20261203_ft_s_form_takt.sql (tools/tests/tempo_einspielen.py)
begin
  if d is null then raise exception 'TEMPO-S1: schule.etappen_stand(bigint, bigint) fehlt'; end if;
  if position('TEMPO-S1' in d) > 0 then raise notice 'TEMPO-S1: etappen_stand schon umgestellt'; return; end if;
  if md5(d) <> v_soll then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: etappen_stand weicht vom Repo-Stand ab (md5 %, erwartet %) – nichts geändert', md5(d), v_soll;
  end if;
  execute $neu$
create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language sql stable set search_path to ''
as $function$
  -- TEMPO-S1: gleiches Ergebnis wie die Fassung nach FT-S; je Einheit einmal: flug_nachtest, gesamt/geloest (gruppiert); je Etappe einmal: karte_ziel
  select coalesce(jsonb_object_agg(z.lz, jsonb_build_object('geloest', z.geloest, 'gesamt', z.gesamt,
           'serie', coalesce(k.serie, 0), 'ziel', z.ziel, 'sitzt', coalesce(k.sitzt, false), 'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig', schule.karte_schwer_noetig(p_einheit, z.lz),
           'faellig', coalesce(schule.karte_faellig(k), false), 'wdh_stufe', coalesce(k.wdh_stufe, 0),
           'eigene_loesungen', coalesce(k.eigene_loesungen, 0), 'folge', coalesce(k.folge, 0), 'folge_ziel', least(3, z.ziel),
           'typen_anzahl', coalesce(array_length(k.typen, 1), 0), 'typen_noetig', schule.karte_typen_noetig(p_einheit, z.lz),
           'fehler_folge', coalesce(k.fehler_folge, 0), 'stufe_senkung', coalesce(k.stufe_senkung, 0), 'sicher', coalesce(schule.karte_sicher(k), false), 'misch_ok', k.misch_ok_am is not null and k.misch_ok_am >= coalesce(k.sitzt_am, k.misch_ok_am), 'flug_nachtest', fn.v,
           'fertig', schule.etappe_fertig(k, s.status), 'test_nachgewiesen', coalesce(s.status in ('nachgewiesen','korrigiert','gesichert'), false), 'wieder_offen', not coalesce(k.sitzt, false) and k.sitzt_am is not null, 'gezaehlt', coalesce((select jsonb_agg(x::bigint) from jsonb_object_keys(k.gezaehlt) x), '[]'::jsonb))), '{}'::jsonb)
  from (select y.lz, coalesce(g.gesamt, 0) gesamt, coalesce(v.geloest, 0) geloest, schule.karte_ziel(p_einheit, y.lz) ziel
          from (select e->>'lernziel' lz, o.nr
                  from schule.einheit x, jsonb_array_elements(coalesce(x.inhalt->'etappen', '[]'::jsonb)) with ordinality o(e, nr) where x.id = p_einheit) y
          left join (select a.variante_gruppe lz, count(*) gesamt from schule.aufgabe a
                      where a.einheit_id = p_einheit and a.pool = 'uebung' and a.freigegeben group by a.variante_gruppe) g on g.lz = y.lz
          left join (select a.variante_gruppe lz, count(distinct v.aufgabe_id) geloest from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
                      where v.lernender_id = p_lernender and v.richtig and v.testsitzung_id is null and a.einheit_id = p_einheit and a.pool = 'uebung'
                      group by a.variante_gruppe) v on v.lz = y.lz
         order by y.nr) z
  cross join (select schule.flug_nachtest(p_lernender, p_einheit) v offset 0) fn
  left join schule.lernziel_stand s on s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.lernziel = z.lz
  left join schule.karte_stand k on k.lernender_id = p_lernender and k.einheit_id = p_einheit and k.lernziel = z.lz;
$function$
$neu$;
end $tempo$;
