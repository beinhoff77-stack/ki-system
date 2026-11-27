-- NT-S / NT-S 2 (22.11.): Nachtests bei kleinen Flügen (Bau-Auftrag NT, Entscheidung des Nutzers 22.11., 17:50 Berlin). Nach TL-S. Nicht einspielen ohne Ansage.
-- Regel: jeder Nachtest hat mindestens 5 Aufgaben je Flug – 1 Pflicht-Etappe → 5 Aufgaben, 2 → je 3, 3–4 → je 2, ab 5 → je 1 (= aufrunden(5 / Pflicht-Etappen)).
-- Gezählt werden die Pflicht-Etappen des Kindes (lernziel_stand.pflicht, nach TL-S die Regel Pflicht/Kür je Schulart). Quote und Einstufung unverändert
-- (≥ 0,8 bestanden, ≥ 0,6 wiederholen, sonst Rückreise; Wertung je Etappe wie bisher). Flug-Test (Blocktest) und Korrektur-Test unverändert.
-- Auswahl je Etappe: zuerst noch nie gestellte Sicherungs-Aufgaben (wie bisher); fehlen welche zur Menge, wird mit schon gestellten aufgefüllt (die am längsten
-- zurückliegenden zuerst) – nie doppelt im selben Nachtest. Hat eine Etappe keine ungestellte Aufgabe mehr, bleibt es wie bisher „Vorrat erschöpft“
-- (so ändert sich für Flüge mit 5 und mehr Pflicht-Etappen nichts). nachtest_stand: vorrat_runden = Runden mit ungestellten Aufgaben bei dieser Menge.
-- Umbau per Anker (wiederholbar); bricht ab, wenn eine Stelle nicht genau einmal gefunden wird. Kein DROP, kein DELETE.

-- 1. Regel
insert into schule.regel (schluessel, wert)
select 'nachtest_min_aufgaben', '5'::jsonb where not exists (select 1 from schule.regel where schluessel = 'nachtest_min_aufgaben');

create or replace function schule.nachtest_je_etappe(p_pflicht int)
 returns int language sql stable set search_path to ''
as $function$
  select greatest(1, ceil(coalesce((select (wert #>> '{}')::numeric from schule.regel where schluessel = 'nachtest_min_aufgaben'), 5) / greatest(p_pflicht, 1))::int);
$function$;
comment on function schule.nachtest_je_etappe(int) is 'NT-S: Aufgaben je Pflicht-Etappe im Nachtest = aufrunden(nachtest_min_aufgaben / Pflicht-Etappen) – 1 → 5, 2 → 3, 3–4 → 2, ab 5 → 1';

-- 2. Auswahl je Etappe
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
     where a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'sicherung')
  select case when not exists (select 1 from a where not a.gestellt) then '{}'::bigint[]          -- wie bisher: ohne ungestellte Aufgabe „Vorrat erschöpft“
              when (select count(*) from a) < greatest(p_anzahl, 1) then '{}'::bigint[]             -- NT-S 2 (D1): nie ein verkürzter Nachtest – genau die Menge oder keine
              else array(select a.id from a order by a.gestellt, a.zuletzt nulls first, a.reihenfolge, a.id limit greatest(p_anzahl, 1)) end;
$function$;
comment on function schule.nachtest_auswahl(bigint, bigint, text, int) is 'NT-S 2: genau p_anzahl Sicherungs-Aufgaben einer Etappe – ungestellte zuerst, aufgefüllt mit den am längsten zurückliegenden; leer (kein Teststart), wenn keine ungestellte mehr da ist oder die Etappe weniger als p_anzahl Aufgaben hat';
revoke all on function schule.nachtest_je_etappe(int), schule.nachtest_auswahl(bigint, bigint, text, int) from public, anon, authenticated;

-- 3. test_starten_intern (nur der Nachtest-Zweig)
do $$
declare d text := pg_get_functiondef('schule.test_starten_intern(bigint, jsonb)'::regprocedure); n int;
  a1 text := $a$v_runde smallint; v_ns jsonb;$a$;
  b1 text := $a$v_runde smallint; v_ns jsonb; v_sel bigint[]; v_je int; /* NT-S */$a$;
  a2 text := $a$      v_runde := (v_ns->>'runde')::smallint;$a$;
  b2 text := $a$      v_runde := (v_ns->>'runde')::smallint;
      v_je := schule.nachtest_je_etappe((select count(*)::int from schule.lernziel_stand s where s.lernender_id = p_lernender and s.einheit_id = v_einheit and s.pflicht)); -- NT-S$a$;
  kopf text := $a$        select a.id into v_aid from schule.aufgabe a
          where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'sicherung'$a$;
  fuss text := $a$        if v_aid is null then v_leer := v_leer || r.lernziel; else v_ids := v_ids || v_aid; end if;$a$;
  neu text := $a$        v_sel := schule.nachtest_auswahl(p_lernender, v_einheit, r.lernziel, v_je); -- NT-S: Menge je Etappe nach der Regel
        if cardinality(v_sel) <> v_je then v_leer := v_leer || r.lernziel; else v_ids := v_ids || v_sel; end if; -- NT-S 2: genau v_je, sonst kein Start$a$;
  i int; j int;
begin
  if position('NT-S' in d) > 0 then raise notice 'test_starten_intern schon umgestellt'; return; end if;
  foreach n in array array[(length(d) - length(replace(d, a1, ''))) / length(a1), (length(d) - length(replace(d, a2, ''))) / length(a2),
                           (length(d) - length(replace(d, kopf, ''))) / length(kopf)] loop
    if n <> 1 then raise exception 'NT-S: Anker in test_starten_intern nicht genau einmal gefunden'; end if;
  end loop;
  i := position(kopf in d);
  j := i + position(fuss in substr(d, i)) - 1;
  if j < i or j - i > 600 then raise exception 'NT-S: Ende des Nachtest-Blocks nicht gefunden'; end if;
  d := substr(d, 1, i - 1) || neu || substr(d, j + length(fuss));
  execute replace(replace(d, a1, b1), a2, b2);
end $$;

-- 4. nachtest_stand: Vorrat in Runden bei dieser Menge, Menge je Etappe im Ergebnis
do $$
declare d text := pg_get_functiondef('schule.nachtest_stand(bigint, bigint)'::regprocedure);
  a1 text := $a$v_art text; v_vorrat int;$a$;                      b1 text := $a$v_art text; v_vorrat int; v_je int; /* NT-S */$a$;
  a2 text := $a$  v_seit := schule.lerntage_seit(p_lernender, coalesce(v_anker, now()));$a$;
  b2 text := a2 || $a$
  v_je := schule.nachtest_je_etappe(v_alle); -- NT-S$a$;
  a3 text := $a$select s.lernziel, count(a.id) n from schule.lernziel_stand s$a$;
  b3 text := $a$select s.lernziel, count(a.id) / greatest(v_je, 1) n from schule.lernziel_stand s$a$;
  a4 text := $a$'vorrat_runden', v_vorrat,$a$;                     b4 text := $a$'aufgaben_je_etappe', v_je, 'vorrat_runden', v_vorrat,$a$;
  x text;
begin
  if position('NT-S' in d) > 0 then raise notice 'nachtest_stand schon umgestellt'; return; end if;
  foreach x in array array[a1, a2, a3, a4] loop
    if (length(d) - length(replace(d, x, ''))) / length(x) <> 1 then raise exception 'NT-S: Anker in nachtest_stand nicht genau einmal gefunden: %', x; end if;
  end loop;
  execute replace(replace(replace(replace(d, a1, b1), a2, b2), a3, b3), a4, b4);
end $$;

-- 5. Fehlliste (Bericht, ändert nichts): je Gruppe und Pflicht-Etappe Sicherungs-Aufgaben gegen den Bedarf für drei Nachtests (Bedarf = 3 × Menge je Etappe).
--    NT-S 2 (D2): Pflicht je Gruppe (bewertung.pflicht_je_schulart der Gruppe, sonst lernziele_pflicht) – wie schule.pflicht_lernziele; leere Liste = kein Nachtest.
create or replace view schule.nachtest_vorrat as
with g as (select unnest(array['gym_by', 'rs_I', 'rs_II_III', 'myp_standard', 'myp_extended']) gruppe),
e as (
  select en.id einheit_id, en.thema_id, g.gruppe,
         array(select jsonb_array_elements_text(coalesce(case when jsonb_typeof(en.inhalt#>array['bewertung', 'pflicht_je_schulart', g.gruppe]) = 'array'
                                                              then en.inhalt#>array['bewertung', 'pflicht_je_schulart', g.gruppe] end,
                                                         en.inhalt#>'{bewertung,lernziele_pflicht}', '[]'::jsonb))) pflicht
    from schule.einheit en cross join g where en.status in ('freigegeben', 'geprueft'))
select e.gruppe, e.thema_id, e.einheit_id, t.unterthema titel, cardinality(e.pflicht) pflicht_etappen, p.lz lernziel,
       schule.nachtest_je_etappe(cardinality(e.pflicht)) je_nachtest, 3 * schule.nachtest_je_etappe(cardinality(e.pflicht)) bedarf,
       (select count(*) from schule.aufgabe a where a.einheit_id = e.einheit_id and a.variante_gruppe = p.lz and a.pool = 'sicherung')::int vorhanden,
       greatest(0, 3 * schule.nachtest_je_etappe(cardinality(e.pflicht))
                   - (select count(*) from schule.aufgabe a where a.einheit_id = e.einheit_id and a.variante_gruppe = p.lz and a.pool = 'sicherung'))::int fehlen
  from e join schule.thema t on t.id = e.thema_id cross join lateral unnest(e.pflicht) p(lz);
comment on view schule.nachtest_vorrat is 'NT-S 2: Sicherungs-Aufgaben je Gruppe und Pflicht-Etappe gegen den Bedarf für drei Nachtests nach der Regel nachtest_je_etappe';
revoke all on schule.nachtest_vorrat from public, anon, authenticated;
