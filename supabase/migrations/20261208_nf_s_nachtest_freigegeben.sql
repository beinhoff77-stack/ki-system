-- NF-S (Einspielen): Nachtest nur mit freigegebenen Aufgaben. schule.nachtest_auswahl und schule.nachtest_stand lassen gesperrte Aufgaben (freigegeben = false) bisher
-- im Vorrat und in der Auswahl; beide werden per create or replace um genau diese eine Bedingung ergänzt – sonst NICHTS (Signatur, Rückgabe, Volatilität, Invoker,
-- search_path, nicht STRICT, Rechte, Kommentare bleiben). VOR der Bestands-Berichtigung 1 einspielen (die bricht ab, wenn NF-S fehlt).
-- Ein Aufruf, eine Transaktion, kein BEGIN/COMMIT. Je Funktion genau zwei zulässige Zustände des Funktionstexts (prosrc-md5): alt (Live-Stand) -> ersetzen, neu -> nichts tun,
-- alles andere -> Abbruch, nichts geändert. Vorher/nachher: Eigenschaften gleich; Ergebnis je Kind × Einheit (nachtest_stand) bzw. je Kind × Einheit/Lernziel × Menge
-- (nachtest_auswahl, deterministisch: Reihenfolge ist durch order by … id festgelegt) vorher = nachher, AUSSER in Einheiten, die schon gesperrte Sicherungs-Aufgaben haben
-- (dort ändert sich das Ergebnis zu Recht; solche Fälle werden gezählt und im Bericht ausgewiesen, kein Abbruch). Aufgaben, die an Sitzungen hängen (testsitzung.aufgaben), bleiben unberührt.
-- alt-md5 auswahl f25fab1c1599d980752c87b6849d557f (Länge 1109) -> neu ca0c30a1913c27b5de0a5505a76a53e5; alt-md5 stand e73af9b462d741de80d4932d8fa7a38a (Länge 3778) -> neu 971ea734cc6cf986e438a29995cb66cf.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $nf$
declare v_a constant regprocedure := to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)');
  v_s constant regprocedure := to_regprocedure('schule.nachtest_stand(bigint, bigint)');
  m_a_alt constant text := 'f25fab1c1599d980752c87b6849d557f'; m_a_neu constant text := 'ca0c30a1913c27b5de0a5505a76a53e5'; m_s_alt constant text := 'e73af9b462d741de80d4932d8fa7a38a'; m_s_neu constant text := '971ea734cc6cf986e438a29995cb66cf';
  e_soll constant text := 's|f|f|{"search_path=\"\""}';
  fehler text[] := '{}'; d text; st_a text; st_s text; ei_a text; ei_s text; ar_a text; ar_s text; ei_a2 text; ei_s2 text; ar_a2 text; ar_s2 text; r record; v text;
  n_a int := 0; n_s int := 0; n_diff int := 0; n_gesperrt int := 0; n_unerw int := 0; n_gesp_live int; v_bericht jsonb; k int;
begin
  if v_a is null or v_s is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.lernender') is null or to_regclass('schule.einheit') is null then
    raise exception 'NF-S ABBRUCH: nachtest_auswahl/nachtest_stand oder die Tabellen fehlen – nichts geändert'; end if;
  -- 1. Zustand je Funktion + Eigenschaften
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')),
         concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname) into d, ei_a, ar_a from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_a;
  st_a := case md5(d) when m_a_alt then 'alt' when m_a_neu then 'neu' else 'unbekannt' end;
  if st_a = 'unbekannt' then fehler := fehler || format('nachtest_auswahl weicht vom Repo-Stand ab (md5 %s, erwartet %s oder %s)', md5(d), m_a_alt, m_a_neu); end if;
  if ei_a <> e_soll then fehler := fehler || format('nachtest_auswahl: Eigenschaften %s, erwartet %s', ei_a, e_soll); end if;
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')),
         concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname) into d, ei_s, ar_s from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_s;
  st_s := case md5(d) when m_s_alt then 'alt' when m_s_neu then 'neu' else 'unbekannt' end;
  if st_s = 'unbekannt' then fehler := fehler || format('nachtest_stand weicht vom Repo-Stand ab (md5 %s, erwartet %s oder %s)', md5(d), m_s_alt, m_s_neu); end if;
  if ei_s <> e_soll then fehler := fehler || format('nachtest_stand: Eigenschaften %s, erwartet %s', ei_s, e_soll); end if;
  if array_length(fehler, 1) > 0 then raise exception 'NF-S ABBRUCH, Vorbedingung (% Befunde), nichts geändert: %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;
  select count(*) into n_gesp_live from schule.aufgabe a where a.pool = 'sicherung' and not a.freigegeben;
  -- 2. Vorher-Stand (nur wenn etwas zu ändern ist)
  create temp table nf_v (art text, l bigint, e bigint, lz text, n int, vor text, nach text) on commit drop;
  if st_a = 'alt' then
    insert into nf_v select 'auswahl', l.id, g.e, g.lz, m.n, schule.nachtest_auswahl(l.id, g.e, g.lz, m.n)::text
      from schule.lernender l cross join (select distinct a.einheit_id e, a.variante_gruppe lz from schule.aufgabe a where a.pool = 'sicherung') g
      cross join (values (1), (2), (3), (5)) m(n);
  end if;
  if st_s = 'alt' then
    for r in select l.id l, e.id e from schule.lernender l cross join schule.einheit e loop
      begin v := schule.nachtest_stand(r.l, r.e)::text; exception when others then v := 'FEHLER ' || sqlstate || ' ' || sqlerrm; end;
      insert into nf_v values ('stand', r.l, r.e, null, null, v);
    end loop;
  end if;
  -- 3. Ersetzen
  if st_a = 'alt' then
    execute $a$
create or replace function schule.nachtest_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
 returns bigint[] language sql stable set search_path to ''
as $function$
  with a as (
    select a.id, a.reihenfolge,
           exists (select 1 from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id)
             or exists (select 1 from schule.testsitzung x where x.lernender_id = p_l and a.id = any(x.aufgaben)) gestellt,
           greatest((select max(v.am) from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id),
                    (select max(x.gestartet_am) from schule.testsitzung x where x.lernender_id = p_l and a.id = any(x.aufgaben))) zuletzt
      from schule.aufgabe a
     where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'sicherung' and a.freigegeben)
  select case when not exists (select 1 from a where not a.gestellt) then '{}'::bigint[]          -- wie bisher: ohne ungestellte Aufgabe „Vorrat erschöpft“
              when (select count(*) from a) < greatest(p_anzahl, 1) then '{}'::bigint[]             -- NT-S 2 (D1): nie ein verkürzter Nachtest – genau die Menge oder keine
              else array(select a.id from a order by a.gestellt, a.zuletzt nulls first, a.reihenfolge, a.id limit greatest(p_anzahl, 1)) end;
$function$
$a$;
  end if;
  if st_s = 'alt' then
    execute $s$
create or replace function schule.nachtest_stand(p_lernender bigint, p_einheit bigint)
 returns jsonb language plpgsql stable set search_path to ''
as $function$
declare v_abst jsonb := coalesce((select wert from schule.regel where schluessel = 'nachtest_abstaende_lerntage'), '[10,25,60]');
  v_wdh int := coalesce((select (wert #>> '{}')::int from schule.regel where schluessel = 'nachtest_wiederholung_lerntage'), 3);
  v_best int; v_letzt schule.testsitzung; v_anker timestamptz; v_soll int; v_seit int; v_offen int; v_fehler int; v_alle int; v_ges int; v_art text; v_vorrat int; v_je int; /* NT-S */
begin
  if schule.flug_ohne_test(p_lernender, p_einheit) then return jsonb_build_object('faellig', false, 'grund',
    case when schule.zusatz_eingeplant(p_lernender, (select e.thema_id from schule.einheit e where e.id = p_einheit)) then 'zusatz' else 'gesetzt' end); end if; -- LB-3, ZP-S
  select count(*) filter (where s.status = 'offen'), count(*) filter (where s.status = 'fehler'), count(*), count(*) filter (where s.status = 'gesichert')
    into v_offen, v_fehler, v_alle, v_ges from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.pflicht;
  if v_alle = 0 or v_offen > 0 then return jsonb_build_object('faellig', false, 'grund', 'einheit_offen'); end if;
  if v_fehler > 0 then return jsonb_build_object('faellig', false, 'grund', 'erst_korrektur'); end if;
  if v_ges = v_alle then return jsonb_build_object('faellig', false, 'grund', 'gesichert'); end if;
  select count(*) into v_best from schule.testsitzung t where t.lernender_id = p_lernender and t.einheit_id = p_einheit and t.art = 'nachtest' and t.ergebnis = 'bestanden';
  select * into v_letzt from schule.testsitzung t where t.lernender_id = p_lernender and t.einheit_id = p_einheit and t.art = 'nachtest' and t.status = 'abgeschlossen'
    order by t.abgeschlossen_am desc, t.id desc limit 1;
  if v_letzt.id is not null and v_letzt.ergebnis in ('wiederholen','rueckreise') then
    select max(t.abgeschlossen_am) into v_anker from schule.testsitzung t where t.lernender_id = p_lernender and t.einheit_id = p_einheit
      and t.art = 'korrektur' and t.status = 'abgeschlossen' and t.abgeschlossen_am >= v_letzt.abgeschlossen_am;
    v_anker := coalesce(v_anker, v_letzt.abgeschlossen_am); v_soll := v_wdh; v_art := 'wiederholung';
  elsif v_letzt.id is not null then
    v_anker := v_letzt.abgeschlossen_am; v_soll := (v_abst->>least(v_best, jsonb_array_length(v_abst) - 1))::int; v_art := 'runde';
  else
    select max(t.abgeschlossen_am) into v_anker from schule.testsitzung t where t.lernender_id = p_lernender and t.einheit_id = p_einheit
      and t.art in ('blocktest','korrektur') and t.status = 'abgeschlossen';
    v_soll := (v_abst->>0)::int; v_art := 'runde';
  end if;
  v_seit := schule.lerntage_seit(p_lernender, coalesce(v_anker, now()));
  v_je := schule.nachtest_je_etappe(v_alle); -- NT-S
  select coalesce(min(n), 0) into v_vorrat from (
    select s.lernziel, count(a.id) / greatest(v_je, 1) n from schule.lernziel_stand s
    left join schule.aufgabe a on a.einheit_id = p_einheit and a.variante_gruppe = s.lernziel and a.pool = 'sicherung' and a.freigegeben
      and not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
      and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))
    where s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.pflicht group by s.lernziel) q;
  return jsonb_build_object('faellig', v_seit >= v_soll, 'grund', case when v_seit >= v_soll then 'faellig' else 'noch_nicht_faellig' end,
    'art', v_art, 'runde', least(v_best + 1, 3), 'folgerunde', v_best >= 3, 'bestandene_runden', v_best, 'lerntage_seit', v_seit, 'lerntage_noetig', v_soll, 'anker', v_anker,
    'aufgaben_je_etappe', v_je, 'vorrat_runden', v_vorrat, 'nachschub_noetig', v_vorrat <= 1);
end $function$
$s$;
  end if;
  -- 4. Nachher: Zustand, Eigenschaften unverändert
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')), concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname)
    into d, ei_a2, ar_a2 from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_a;
  if md5(d) <> m_a_neu then fehler := fehler || format('nachtest_auswahl: neuer Funktionstext hat md5 %s, erwartet %s', md5(d), m_a_neu); end if;
  select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, '')), concat_ws('|', pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname)
    into d, ei_s2, ar_s2 from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = v_s;
  if md5(d) <> m_s_neu then fehler := fehler || format('nachtest_stand: neuer Funktionstext hat md5 %s, erwartet %s', md5(d), m_s_neu); end if;
  if (ei_a2, ar_a2, ei_s2, ar_s2) is distinct from (ei_a, ar_a, ei_s, ar_s) then fehler := fehler || 'Eigenschaften (Volatilität, Definer/Invoker, STRICT, search_path, Signatur, Rückgabetyp, Sprache) haben sich geändert'; end if;
  if array_length(fehler, 1) > 0 then raise exception 'NF-S ABBRUCH, alles zurückgerollt (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;
  -- 5. Nachher-Ergebnisse, Vergleich
  if st_a = 'alt' then
    update nf_v x set nach = schule.nachtest_auswahl(x.l, x.e, x.lz, x.n)::text where x.art = 'auswahl';
  end if;
  if st_s = 'alt' then
    for r in select * from nf_v x where x.art = 'stand' loop
      begin v := schule.nachtest_stand(r.l, r.e)::text; exception when others then v := 'FEHLER ' || sqlstate || ' ' || sqlerrm; end;
      update nf_v set nach = v where art = 'stand' and l = r.l and e = r.e;
    end loop;
  end if;
  select count(*) filter (where art = 'auswahl'), count(*) filter (where art = 'stand'), count(*) filter (where vor is distinct from nach),
         count(*) filter (where vor is distinct from nach and exists (select 1 from schule.aufgabe a where a.einheit_id = nf_v.e and a.pool = 'sicherung' and not a.freigegeben)),
         count(*) filter (where vor is distinct from nach and not exists (select 1 from schule.aufgabe a where a.einheit_id = nf_v.e and a.pool = 'sicherung' and not a.freigegeben))
    into n_a, n_s, n_diff, n_gesperrt, n_unerw from nf_v;
  if n_unerw > 0 then
    raise exception 'NF-S ABBRUCH, alles zurückgerollt: % Fälle ändern sich, obwohl in der Einheit keine Sicherungs-Aufgabe gesperrt ist (z. B. %)', n_unerw,
      (select string_agg(format('%s Kind %s Einheit %s %s', art, l, e, coalesce(lz, '')), '; ') from (select * from nf_v where vor is distinct from nach
        and not exists (select 1 from schule.aufgabe a where a.einheit_id = nf_v.e and a.pool = 'sicherung' and not a.freigegeben) limit 5) z); end if;
  v_bericht := jsonb_build_object('nachtest_auswahl', st_a || ' -> neu', 'nachtest_stand', st_s || ' -> neu', 'md5_auswahl_neu', m_a_neu, 'md5_stand_neu', m_s_neu,
    'verglichen_auswahl', n_a, 'verglichen_stand', n_s, 'abweichend_gesamt', n_diff, 'abweichend_wegen_gesperrter_sicherungsaufgaben', n_gesperrt, 'abweichend_unerwartet', n_unerw,
    'gesperrte_sicherungsaufgaben_live', n_gesp_live, 'eigenschaften_gleich', true, 'fehler', 0);
  raise notice 'NF-S eingespielt: %', v_bericht::text;
end $nf$;
