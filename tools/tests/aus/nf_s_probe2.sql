-- NF-S Probe 2 (rein lesend, rollt am Ende ALLES zurück). Zusatz zur ersten Probe; funktioniert in jedem Zustand (alt/neu/gemischt).
-- Die alten (Live-Stand) und die neuen Funktionstexte werden als temporäre Funktionen pg_temp.nf_alt_*/nf_neu_* angelegt: Wirkung = alt gegen neu; zusätzlich muss die lebende Funktion das Ergebnis ihres eigenen Zustands liefern:
-- Fehler getrennt zählen (Abbruch), Abweichung nur mit gesperrter Sicherungsaufgabe am konkreten Lernziel (auswahl) bzw. an einem Pflicht-Lernziel des Kindes (stand),
-- bei nachtest_stand nur in vorrat_runden/nachschub_noetig. Nur Zahlen im Bericht. md5 alt auswahl f25fab1c1599d980752c87b6849d557f, stand e73af9b462d741de80d4932d8fa7a38a, test_starten_intern b226ac94131e47a507462e9be303ef8f.
select set_config('lock_timeout', '3s', true), set_config('statement_timeout', '300s', true);
do $nf2$
declare v_a constant regprocedure := to_regprocedure('schule.nachtest_auswahl(bigint, bigint, text, integer)');
  v_s constant regprocedure := to_regprocedure('schule.nachtest_stand(bigint, bigint)');
  v_t constant regprocedure := to_regprocedure('schule.test_starten_intern(bigint, jsonb)');
  eig_a constant text := 's|f|f|{"search_path=\"\""}|proparallel u, procost 100, proleakproof f'; eig_t constant text := 'v|f|f|{"search_path=\"\""}|proparallel u, procost 100, proleakproof f';
  fehler text[] := '{}'; zst jsonb := '{}'; d text; e text; r record; va text; vb text; n_a int := 0; n_s int := 0; n_a_diff int := 0; n_s_diff int := 0; n_err int := 0; n_unerw int := 0;
  n_erlaubt int := 0; n_gesp int; fe text[] := '{}'; vc text; n_live int := 0;
begin
  if v_a is null or v_s is null or v_t is null or to_regclass('schule.aufgabe') is null or to_regclass('schule.lernender') is null or to_regclass('schule.lernziel_stand') is null then
    raise exception 'NF-S PROBE2 ABBRUCH: Funktionen oder Tabellen fehlen'; end if;
  -- 1. Zustände und vollständige Eigenschaften
  for r in select x.n, x.o, x.alt, x.neu, x.soll from (values ('auswahl', v_a, 'f25fab1c1599d980752c87b6849d557f', 'ca0c30a1913c27b5de0a5505a76a53e5', eig_a), ('stand', v_s, 'e73af9b462d741de80d4932d8fa7a38a', '971ea734cc6cf986e438a29995cb66cf', eig_a),
                            ('test_starten_intern', v_t, 'b226ac94131e47a507462e9be303ef8f', '7abcd2918f5042142d8720ae044b36c1', eig_t)) x(n, o, alt, neu, soll) loop
    select p.prosrc, concat_ws('|', p.provolatile, p.prosecdef, p.proisstrict, coalesce(p.proconfig::text, ''), pg_get_function_arguments(p.oid), p.prorettype::regtype::text, l.lanname,
           'proparallel ' || p.proparallel::text, 'procost ' || p.procost::text, 'proleakproof ' || (case when p.proleakproof then 't' else 'f' end)) into d, e
      from pg_proc p join pg_language l on l.oid = p.prolang where p.oid = r.o;
    zst := zst || jsonb_build_object(r.n, case md5(d) when r.alt then 'alt' when r.neu then 'neu' else 'unbekannt' end);
    if md5(d) not in (r.alt, r.neu) then fehler := fehler || format('%s: Funktionstext weder alt noch neu (md5 %s)', r.n, md5(d)); end if;
    if e not like (case when r.n = 'test_starten_intern' then 'v|f|f|%' else 's|f|f|%' end) then fehler := fehler || format('%s: Volatilität/Definer/STRICT: %s', r.n, e); end if;
    if position('search_path=""' in replace(e, '\"', '"')) = 0 then fehler := fehler || format('%s: search_path nicht leer: %s', r.n, e); end if;
    if position('proparallel u|procost 100|proleakproof f' in e) = 0 then fehler := fehler || format('%s: Parallelität/Kosten/LEAKPROOF abweichend: %s', r.n, e); end if;
  end loop;
  if position('p_l bigint, p_e bigint, p_lz text, p_anzahl integer|bigint[]|sql|' in (select concat_ws('|', pg_get_function_arguments(oid), prorettype::regtype::text, (select lanname from pg_language where oid = prolang), '') from pg_proc where oid = v_a)) = 0
     or position('p_lernender bigint, p_einheit bigint|jsonb|plpgsql|' in (select concat_ws('|', pg_get_function_arguments(oid), prorettype::regtype::text, (select lanname from pg_language where oid = prolang), '') from pg_proc where oid = v_s)) = 0
     or position('p_lernender bigint, p_daten jsonb|jsonb|plpgsql|' in (select concat_ws('|', pg_get_function_arguments(oid), prorettype::regtype::text, (select lanname from pg_language where oid = prolang), '') from pg_proc where oid = v_t)) = 0 then
    fehler := fehler || 'Argumente, Rückgabetyp oder Sprache einer der drei Funktionen weichen ab'::text; end if;
  if array_length(fehler, 1) > 0 then raise exception 'NF-S PROBE2 ABBRUCH (% Befunde): %', array_length(fehler, 1), array_to_string(fehler, ' | '); end if;
  -- 2. Alte Texte als temporäre Funktionen (Live-Stand), nur in dieser Transaktion
  execute $a$
create function pg_temp.nf_alt_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
 returns bigint[] language sql stable set search_path to ''
as $function$
  with a as (
    select a.id, a.reihenfolge,
           exists (select 1 from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id)
             or exists (select 1 from schule.testsitzung x where x.lernender_id = p_l and a.id = any(x.aufgaben)) gestellt,
           greatest((select max(v.am) from schule.versuch v where v.lernender_id = p_l and v.aufgabe_id = a.id),
                    (select max(x.gestartet_am) from schule.testsitzung x where x.lernender_id = p_l and a.id = any(x.aufgaben))) zuletzt
      from schule.aufgabe a
     where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'sicherung')
  select case when not exists (select 1 from a where not a.gestellt) then '{}'::bigint[]          -- wie bisher: ohne ungestellte Aufgabe „Vorrat erschöpft“
              when (select count(*) from a) < greatest(p_anzahl, 1) then '{}'::bigint[]             -- NT-S 2 (D1): nie ein verkürzter Nachtest – genau die Menge oder keine
              else array(select a.id from a order by a.gestellt, a.zuletzt nulls first, a.reihenfolge, a.id limit greatest(p_anzahl, 1)) end;
$function$
$a$;
  execute $s$
create function pg_temp.nf_alt_stand(p_lernender bigint, p_einheit bigint)
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
    left join schule.aufgabe a on a.einheit_id = p_einheit and a.variante_gruppe = s.lernziel and a.pool = 'sicherung'
      and not exists (select 1 from schule.versuch v where v.lernender_id = p_lernender and v.aufgabe_id = a.id)
      and not exists (select 1 from schule.testsitzung x where x.lernender_id = p_lernender and a.id = any(x.aufgaben))
    where s.lernender_id = p_lernender and s.einheit_id = p_einheit and s.pflicht group by s.lernziel) q;
  return jsonb_build_object('faellig', v_seit >= v_soll, 'grund', case when v_seit >= v_soll then 'faellig' else 'noch_nicht_faellig' end,
    'art', v_art, 'runde', least(v_best + 1, 3), 'folgerunde', v_best >= 3, 'bestandene_runden', v_best, 'lerntage_seit', v_seit, 'lerntage_noetig', v_soll, 'anker', v_anker,
    'aufgaben_je_etappe', v_je, 'vorrat_runden', v_vorrat, 'nachschub_noetig', v_vorrat <= 1);
end $function$
$s$;
  execute $a$
create function pg_temp.nf_neu_auswahl(p_l bigint, p_e bigint, p_lz text, p_anzahl int)
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
  execute $s$
create function pg_temp.nf_neu_stand(p_lernender bigint, p_einheit bigint)
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
  select count(*) into n_gesp from schule.aufgabe a where a.pool = 'sicherung' and not a.freigegeben;
  -- 3. nachtest_auswahl: alt (Kopie) gegen lebend, je Kind × Einheit/Lernziel × Menge; Fehler getrennt
  for r in select l.id l, g.e, g.lz, m.n, exists (select 1 from schule.aufgabe a where a.einheit_id = g.e and a.variante_gruppe is not distinct from g.lz and a.pool = 'sicherung' and not a.freigegeben) gesperrt
             from schule.lernender l cross join (select distinct a.einheit_id e, a.variante_gruppe lz from schule.aufgabe a where a.pool = 'sicherung') g cross join (values (1), (2), (3), (5)) m(n) loop
    n_a := n_a + 1; va := null; vb := null;
    begin va := pg_temp.nf_alt_auswahl(r.l, r.e, r.lz, r.n)::text; exception when others then n_err := n_err + 1; fe := fe || ('auswahl alt ' || sqlstate); end;
    begin vb := pg_temp.nf_neu_auswahl(r.l, r.e, r.lz, r.n)::text; exception when others then n_err := n_err + 1; fe := fe || ('auswahl neu ' || sqlstate); end;
    begin vc := schule.nachtest_auswahl(r.l, r.e, r.lz, r.n)::text; exception when others then n_err := n_err + 1; fe := fe || ('auswahl lebend ' || sqlstate); vc := null; end;
    if vc is distinct from (case zst->>'auswahl' when 'alt' then va else vb end) then n_live := n_live + 1; end if;
    if va is distinct from vb then
      n_a_diff := n_a_diff + 1;
      if r.gesperrt then n_erlaubt := n_erlaubt + 1; else n_unerw := n_unerw + 1; end if;
    end if;
  end loop;
  -- 4. nachtest_stand: je Kind × Einheit; nur vorrat_runden/nachschub_noetig dürfen abweichen, und nur mit gesperrter Sicherungsaufgabe an einem Pflicht-Lernziel des Kindes
  for r in select l.id l, en.id e, exists (select 1 from schule.aufgabe a join schule.lernziel_stand s on s.lernender_id = l.id and s.einheit_id = en.id and s.pflicht and s.lernziel = a.variante_gruppe
                                            where a.einheit_id = en.id and a.pool = 'sicherung' and not a.freigegeben) gesperrt
             from schule.lernender l cross join schule.einheit en loop
    n_s := n_s + 1; va := null; vb := null;
    begin va := pg_temp.nf_alt_stand(r.l, r.e)::text; exception when others then n_err := n_err + 1; fe := fe || ('stand alt ' || sqlstate); end;
    begin vb := pg_temp.nf_neu_stand(r.l, r.e)::text; exception when others then n_err := n_err + 1; fe := fe || ('stand neu ' || sqlstate); end;
    begin vc := schule.nachtest_stand(r.l, r.e)::text; exception when others then n_err := n_err + 1; fe := fe || ('stand lebend ' || sqlstate); vc := null; end;
    if vc is distinct from (case zst->>'stand' when 'alt' then va else vb end) then n_live := n_live + 1; end if;
    if va is distinct from vb then
      n_s_diff := n_s_diff + 1;
      if va is null or vb is null or (va::jsonb - 'vorrat_runden' - 'nachschub_noetig') is distinct from (vb::jsonb - 'vorrat_runden' - 'nachschub_noetig') or not r.gesperrt then
        n_unerw := n_unerw + 1; else n_erlaubt := n_erlaubt + 1; end if;
    end if;
  end loop;
  if n_err > 0 then raise exception 'NF-S PROBE2 ABBRUCH: % Aufrufe mit Fehler (getrennt gezählt, z. B. %)', n_err, array_to_string(fe[1:5], '; '); end if;
  if n_live > 0 then raise exception 'NF-S PROBE2 ABBRUCH: % lebende Aufrufe liefern nicht das Ergebnis ihres eigenen Zustands (alt/neu)', n_live; end if;
  if n_unerw > 0 then raise exception 'NF-S PROBE2 ABBRUCH: % Abweichungen ohne erlaubten Grund (kein gesperrtes Sicherungs-Lernziel bzw. andere Felder als vorrat_runden/nachschub_noetig)', n_unerw; end if;
  raise exception 'PROBELAUF2 bestanden, ALLES zurückgerollt (nichts geändert): %', jsonb_build_object('zustand', zst, 'verglichen_auswahl', n_a, 'verglichen_stand', n_s, 'abweichend_auswahl', n_a_diff,
    'abweichend_stand', n_s_diff, 'erlaubt_wegen_gesperrter_sicherungsaufgaben', n_erlaubt, 'unerwartet', n_unerw, 'lebend_abweichend_vom_eigenen_zustand', n_live, 'fehler', n_err, 'gesperrte_sicherungsaufgaben_live', n_gesp)::text;
end $nf2$;
