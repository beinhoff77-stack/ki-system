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
--     Zulässig sind genau zwei Zustände des Funktionstexts: exakt alt (md5 bf3152e9…, nachgerechnet aus den Migrationen 20261114 … 20261203) → ersetzen;
--     exakt neu (md5 3f49198f…) → nichts tun. Alles andere (auch eine alte Fassung mit dem Wort TEMPO-S1) → Abbruch. Danach muss der neue md5 stehen;
--     Signatur, Rückgabetyp, Sprache, STABLE, SECURITY INVOKER und search_path werden vor und nach dem Ersetzen geprüft.
--  4. Nach dem Anlegen der Indizes: unter beiden Namen ein gültiger, bereiter, nicht eindeutiger B-Baum ohne Bedingung auf der richtigen Tabelle mit
--     genau diesen Spalten in dieser Reihenfolge – sonst Abbruch (create index if not exists nimmt einen gleichnamigen anderen Index sonst hin).
-- WAS NICHT: keine Tabelle, keine Spalte, kein Trigger, keine andere Funktion; kein DROP, kein DELETE, kein UPDATE; api.schule_merkheft bleibt, wie sie ist
--   (Antwort unverändert; Vorschlag für eine schlankere Antwort nur in der Analyse). Wiederholbar: ein zweiter Lauf ändert nichts.
-- Sperren: create index hält SHARE auf schule.aufgabe und schule.versuch bis zum Ende der Transaktion (Lesen geht, Schreiben wartet). Das Paket legt die
--   Indizes deshalb erst NACH dem Vergleich mit der neuen Funktion an und vergleicht danach nur noch einmal (Beweis im Endzustand); gemessen wird getrennt
--   (tools/tests/aus/tempo_s1_messen.sql, neue Transaktion, rollt zurück). Ausführungsvorschrift: inhalte/plan/ladezeiten.md, Abschnitt „Einspielen“.

select set_config('lock_timeout', '3s', true);

-- ==== TEMPO-S1 Teil 1: Funktion ====
-- 1. etappen_stand: genau zwei zulässige Zustände des Funktionstexts (prosrc): alt → ersetzen, neu → nichts tun; alles andere → Abbruch.
--    Signatur, Rückgabetyp, Sprache, STABLE, SECURITY INVOKER und search_path müssen vorher und nachher gleich (und wie erwartet) sein.
do $tempo$
declare v_f constant regprocedure := to_regprocedure('schule.etappen_stand(bigint, bigint)');
  v_alt constant text := 'bf3152e9a378a1d4e41c98965acf738e';   -- md5 des Funktionstexts nach 20261203_ft_s_form_takt.sql (tools/tests/tempo_einspielen.py)
  v_neu constant text := '3f49198f8dbf5c822a0be4650a5ebce5';   -- md5 des Funktionstexts unten (TEMPO-S1)
  v_art_soll constant text := 'p_lernender bigint, p_einheit bigint|jsonb|sql|s|f|{"search_path=\"\""}';
  d text; v_art_vor text; v_art_nach text;
begin
  if v_f is null then raise exception 'TEMPO-S1 ABBRUCH: schule.etappen_stand(bigint, bigint) fehlt – nichts geändert'; end if;
  select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname, p.provolatile, p.prosecdef, coalesce(p.proconfig::text, ''))
    into d, v_art_vor from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_f;
  if v_art_vor is distinct from v_art_soll then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: Eigenschaften von etappen_stand anders als erwartet (%, erwartet %) – nichts geändert', v_art_vor, v_art_soll;
  end if;
  if md5(d) = v_neu then raise notice 'TEMPO-S1: etappen_stand schon umgestellt (md5 %)', v_neu; return; end if;
  if md5(d) <> v_alt then
    raise exception 'TEMPO-S1 ABBRUCH, Vorbedingung: etappen_stand weicht vom Repo-Stand ab (md5 %, erwartet % oder %) – nichts geändert', md5(d), v_alt, v_neu;
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
  select p.prosrc, concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname, p.provolatile, p.prosecdef, coalesce(p.proconfig::text, ''))
    into d, v_art_nach from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_f;
  if md5(d) is distinct from v_neu then raise exception 'TEMPO-S1 ABBRUCH: neuer Funktionstext hat md5 %, erwartet %', md5(d), v_neu; end if;
  if v_art_nach is distinct from v_art_vor then raise exception 'TEMPO-S1 ABBRUCH: Eigenschaften von etappen_stand geändert (% → %)', v_art_vor, v_art_nach; end if;
end $tempo$;

-- ==== TEMPO-S1 Teil 2: Indizes ====
-- 2. Indizes; danach prüfen, dass unter den Zielnamen genau diese gültigen, bereiten B-Bäume liegen (ein gleichnamiger anderer Index → Abbruch)
create index if not exists aufgabe_einheit_pool_lz_idx on schule.aufgabe (einheit_id, pool, variante_gruppe);
create index if not exists versuch_kind_aufgabe_idx on schule.versuch (lernender_id, aufgabe_id);
do $tempoidx$
declare r record; v_ist text;
begin
  for r in select * from (values ('aufgabe_einheit_pool_lz_idx', 'aufgabe', 'einheit_id,pool,variante_gruppe'),
                                 ('versuch_kind_aufgabe_idx', 'versuch', 'lernender_id,aufgabe_id')) x(name, tabelle, spalten) loop
    select string_agg(a.attname, ',' order by k.nr) into v_ist
      from pg_class c join pg_namespace n on n.oid = c.relnamespace and n.nspname = 'schule'
      join pg_index i on i.indexrelid = c.oid join pg_class t on t.oid = i.indrelid and t.relname = r.tabelle and t.relnamespace = n.oid
      join pg_am am on am.oid = c.relam and am.amname = 'btree'
      cross join lateral unnest(i.indkey::int2[]) with ordinality k(att, nr) join pg_attribute a on a.attrelid = t.oid and a.attnum = k.att
     where c.relname = r.name and c.relkind = 'i' and i.indisvalid and i.indisready and i.indpred is null and i.indexprs is null
       and i.indnkeyatts = i.indnatts and not i.indisunique;
    if v_ist is distinct from r.spalten then
      raise exception 'TEMPO-S1 ABBRUCH: Index schule.% ist nicht der erwartete gültige B-Baum auf schule.% (%), gefunden: % – nichts geändert',
        r.name, r.tabelle, r.spalten, coalesce(v_ist, 'anderer/ungültiger Index');
    end if;
  end loop;
end $tempoidx$;
