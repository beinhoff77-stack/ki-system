-- BD-S2 (Fundament, Schritt 2, Teil 2 von 2): Antworttyp „bedingung“ freischalten – zusammen mit dem Schutz der Prüf-Bäume.
-- Voraussetzung: BD-S1 (Rechner, schule.bed_gueltig, Zweig in schule.antwort_bewerten).
-- Alles in EINER Transaktion: Schutz und Öffnung gelten gemeinsam oder gar nicht.
--
-- 1. schule.loesung_sicht(aufgabe): die einzige Stelle, die festlegt, was von einer Lösung den Server verlässt (Positivliste).
--    Typ „bedingung“: nur „beispiel“ und die NAMEN der Bedingungen. pruefe, zeige, hinweis-Vorlagen, gut, gegenbeispiele bleiben intern.
--    Alle anderen Typen: unverändert die ganze Lösung (wie bisher).
-- 2. Alle sechs Ausgaben, die bisher a.loesung sendeten, senden schule.loesung_sicht(a) (Text-Patch mit Zählung, drei Zustände):
--    schule.uebung_pruefen_intern (sieben Stellen), schule.test_abschliessen_intern, schule.expeditionen_kind, schule.expeditionen_alle,
--    api.schule_lernstand, api.schule_inhalt_lesen.   Gelesen am 27.11.: Weitere Ausgaben der Lösung gibt es nicht
--    (kein to_jsonb(a), keine Sicht; schule.aufgabe_anzeige sendet nur loesung->>'einheit'; test_antwort_intern sendet nur den Formatstatus).
-- 3. Übung: Beim ersten Fehlversuch und nach der endgültigen Antwort gehen zusätzlich „verletzt“ (Name der Bedingung) und
--    „hinweis“ („Deine Summe ist 1.“) an die App. Bei JEDER wiederholten Übertragung (erster wie endgültiger Fehlversuch) wird beides
--    einmal aus dem gespeicherten Versuch neu berechnet (die Bedingungen sind ab dem ersten Versuch unveränderlich, siehe 4) –
--    die Wiederholung antwortet also wie das Original. Für die fünf alten Typen ändert sich an den Antworten nichts.
--    Neu für ALLE Typen: Eine wiederholte Übertragung, deren client_id zu einer anderen Aufgabe gehört, wird abgewiesen
--    (bisher lieferte sie die Lösung der genannten Aufgabe ohne Versuch).
-- 4. Schutz der Versionen: Felder, Bedingungen und Beispiel einer Aufgabe dieses Typs sind unveränderlich, sobald es einen Versuch gibt
--    (gilt auch für Expeditionen, die der vorhandene Schutz ausnimmt). Inhaltliche Änderung = neue Aufgabe.
-- 5. Constraint: aufgabe_antworttyp_check lässt „bedingung“ zu; neuer Constraint aufgabe_bedingung_gueltig prüft jede solche Aufgabe
--    mit schule.bed_gueltig – für jeden Schreibweg (aufgaben_einfuegen, einheit_abgleichen, expedition_importieren, Handarbeit) –
--    und lässt in der Lösung NUR die Schlüssel bedingungen, beispiel, gut, gegenbeispiele zu. Damit kann schule.aufgabe_anzeige
--    (sendet loesung->>'einheit' vor der Antwort) bei diesem Typ nichts aus der Lösung zeigen.
--    Beide Constraints werden gegen eine Soll-Fassung verglichen (Zwilling an einer Temp-Tabelle); jede andere Fassung = Abbruch.
--    Das Ersetzen des alten Constraints braucht ein DROP CONSTRAINT (eine Check-Bedingung lässt sich nicht ändern); Daten werden nicht gelöscht.
-- Nicht in dieser Datei: Feld für Regel-Kennung und Fehlbild (kommt mit dem Einbau des Regel-Universums); Eltern-Ansicht „verletzt“.
-- Wiederholbar. Kein DELETE. Nicht eingespielt ohne ausdrücklichen Satz des Nutzers.

do $$ begin
  if to_regprocedure('schule.bed_gueltig(jsonb, jsonb)') is null
     or position('schule.bed_bewerten' in pg_get_functiondef('schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure)) = 0
  then raise exception 'BD-S2: BD-S1 fehlt'; end if;
end $$;

create or replace function schule.loesung_sicht(a schule.aufgabe)
 returns jsonb language sql immutable set search_path to ''
as $$
  select case when a.antworttyp = 'bedingung'
    then jsonb_build_object('beispiel', a.loesung->'beispiel',
                            'bedingungen', coalesce((select jsonb_agg(b->>'name' order by o) from jsonb_array_elements(a.loesung->'bedingungen') with ordinality t(b, o)), '[]'::jsonb))
    else a.loesung end
$$;
revoke all on function schule.loesung_sicht(schule.aufgabe) from public, anon, authenticated;

-- Text-Patches. Je Funktion eine Liste (alt, neu, erwartete Anzahl). Zustände je Eintrag:
--   alt    = alt steht genau so oft da wie erwartet, neu gar nicht  -> ersetzen
--   fertig = alt steht nicht mehr da, neu genau so oft wie erwartet -> nichts tun
--   sonst  -> Abbruch (nichts wird geändert). Auch Abbruch, wenn in EINER Funktion manche Stellen alt und andere fertig sind.
do $$
declare
  f record; e jsonb; d text; d0 text; n_alt int; n_neu int; soll int; z_alt int; z_fertig int;
  zaehle constant text := 'select (length($1) - length(replace($1, $2, ''''))) / length($2)';
  plan constant jsonb := jsonb_build_array(
    jsonb_build_object('f', 'schule.uebung_pruefen_intern(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array('if v_alt.id is not null then
      if coalesce(v_alt.anlauf, 0) = 1 and not v_alt.richtig then',
                        'if v_alt.id is not null then
      if v_alt.aufgabe_id is distinct from a.id then raise exception ''Diese Antwort gehört zu einer anderen Aufgabe'' using errcode = ''P0001''; end if;
      b := case when a.antworttyp = ''bedingung'' and not v_alt.richtig then schule.antwort_bewerten(a, v_alt.antwort) end; -- BD-S2: Rückmeldung aus dem gespeicherten Versuch
      if coalesce(v_alt.anlauf, 0) = 1 and not v_alt.richtig then', 1),
      jsonb_build_array('''grund'', b->>''grund'', ''loesung'', a.loesung',
                        '''grund'', b->>''grund'', ''verletzt'', b->>''verletzt'', ''hinweis'', b->>''hinweis'', ''loesung'', schule.loesung_sicht(a)', 4),
      jsonb_build_array('return jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', v_alt.richtig, ''loesung'', a.loesung, ''loesungsweg'', a.loesungsweg, ''wiederholt'', true);',
                        'return jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', v_alt.richtig, ''loesung'', schule.loesung_sicht(a), ''loesungsweg'', a.loesungsweg, ''wiederholt'', true) || jsonb_strip_nulls(jsonb_build_object(''verletzt'', b->>''verletzt'', ''hinweis'', b->>''hinweis''));', 1),
      jsonb_build_array('return jsonb_strip_nulls(jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', false, ''nochmal'', true, ''grund'', b->>''grund''));',
                        'return jsonb_strip_nulls(jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', false, ''nochmal'', true, ''grund'', b->>''grund'', ''verletzt'', b->>''verletzt'', ''hinweis'', b->>''hinweis''));', 1),
      jsonb_build_array('return jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', false, ''nochmal'', true, ''wiederholt'', true);',
                        'return jsonb_strip_nulls(jsonb_build_object(''ok'', true, ''format_ok'', true, ''richtig'', false, ''nochmal'', true, ''wiederholt'', true, ''verletzt'', b->>''verletzt'', ''hinweis'', b->>''hinweis''));', 1))),
    jsonb_build_object('f', 'schule.test_abschliessen_intern(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array('''loesung'', a.loesung', '''loesung'', schule.loesung_sicht(a)', 1))),
    jsonb_build_object('f', 'schule.expeditionen_kind(bigint)', 'p', jsonb_build_array(
      jsonb_build_array('''loesung'', a.loesung', '''loesung'', schule.loesung_sicht(a)', 1))),
    jsonb_build_object('f', 'schule.expeditionen_alle()', 'p', jsonb_build_array(
      jsonb_build_array('''loesung'', a.loesung', '''loesung'', schule.loesung_sicht(a)', 1))),
    jsonb_build_object('f', 'api.schule_lernstand(text, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array('''loesung'', a.loesung', '''loesung'', schule.loesung_sicht(a)', 1))),
    jsonb_build_object('f', 'api.schule_inhalt_lesen(text, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array('''loesung'', a.loesung', '''loesung'', schule.loesung_sicht(a)', 1))));
begin
  for f in select x->>'f' as name, x->'p' as p from jsonb_array_elements(plan) x loop
    if to_regprocedure(f.name) is null then raise exception 'BD-S2: Funktion % fehlt', f.name; end if;
    d0 := pg_get_functiondef(to_regprocedure(f.name)); d := d0; z_alt := 0; z_fertig := 0;
    for e in select * from jsonb_array_elements(f.p) loop
      soll := (e->>2)::int;
      execute zaehle into n_alt using d, e->>0;
      execute zaehle into n_neu using d, e->>1;
      if n_alt = soll and n_neu = 0 then d := replace(d, e->>0, e->>1); z_alt := z_alt + 1;
      elsif n_alt = 0 and n_neu = soll then z_fertig := z_fertig + 1;
      else raise exception 'BD-S2: % ist weder im alten noch im fertigen Zustand (Stelle „%…“: alt %, neu %, erwartet %)', f.name, left(e->>0, 40), n_alt, n_neu, soll;
      end if;
    end loop;
    -- eine Funktion ist ganz alt oder ganz fertig; halb umgestellt ist ein Mischstand
    if z_alt > 0 and z_fertig > 0 then raise exception 'BD-S2: % ist halb umgestellt (% Stellen alt, % fertig)', f.name, z_alt, z_fertig; end if;
    -- danach darf die rohe Lösung in dieser Funktion nicht mehr gesendet werden
    execute zaehle into n_alt using d, '''loesung'', a.loesung';
    if n_alt <> 0 then raise exception 'BD-S2: in % wird a.loesung noch % Mal gesendet', f.name, n_alt; end if;
    if d is distinct from d0 then execute d; end if;
  end loop;
end $$;

-- Versionen: Felder, Bedingungen und Beispiel sind fest, sobald es einen Versuch gibt.
create or replace function schule.aufgabe_bedingung_schutz()
 returns trigger language plpgsql set search_path to ''
as $$
begin
  if old.antworttyp = 'bedingung'
     and (new.antworttyp, new.frage->'felder', new.loesung->'bedingungen', new.loesung->'beispiel')
         is distinct from (old.antworttyp, old.frage->'felder', old.loesung->'bedingungen', old.loesung->'beispiel')
     and exists (select 1 from schule.versuch v where v.aufgabe_id = old.id) then
    raise exception 'Aufgabe % (Typ bedingung) hat schon Versuche: Felder, Bedingungen und Beispiel sind unveränderlich. Lege eine neue Aufgabe an.', old.id;
  end if;
  return new;
end $$;
do $$ begin
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.aufgabe'::regclass and tgname = 'aufgabe_bedingung_schutz') then
    create trigger aufgabe_bedingung_schutz before update on schule.aufgabe for each row execute function schule.aufgabe_bedingung_schutz();
  end if;
end $$;

-- Öffnung: erst jetzt, in derselben Transaktion wie der Schutz.
do $$
declare
  v_ist text; v_soll text;
  alt constant text := 'CHECK ((antworttyp = ANY (ARRAY[''auswahl''::text, ''zahl''::text, ''text''::text, ''markierung''::text, ''luecken''::text])))';
  c_typ constant text := 'check (antworttyp = any (array[''auswahl''::text, ''zahl''::text, ''text''::text, ''markierung''::text, ''luecken''::text, ''bedingung''::text]))';
  c_gueltig constant text := 'check (antworttyp <> ''bedingung'' or (schule.bed_gueltig(frage, loesung) is null and (loesung - array[''bedingungen'', ''beispiel'', ''gut'', ''gegenbeispiele'']) = ''{}''::jsonb))';
begin
  -- Zwilling: dieselben Bedingungen an einer Temp-Tabelle, damit die Soll-Fassung so vorliegt, wie die Datenbank sie schreibt
  if to_regclass('pg_temp.bd_s2_zwilling') is null then
    execute format('create temp table bd_s2_zwilling (antworttyp text, frage jsonb, loesung jsonb, constraint z_typ %s, constraint z_gueltig %s) on commit drop', c_typ, c_gueltig);
  end if;
  select pg_get_constraintdef(oid) into v_ist from pg_constraint where conname = 'aufgabe_antworttyp_check' and conrelid = 'schule.aufgabe'::regclass;
  select pg_get_constraintdef(oid) into v_soll from pg_constraint where conname = 'z_typ' and conrelid = 'pg_temp.bd_s2_zwilling'::regclass;
  if v_ist is null or v_soll is null then raise exception 'BD-S2: aufgabe_antworttyp_check fehlt'; end if;
  if v_ist = alt then
    alter table schule.aufgabe drop constraint aufgabe_antworttyp_check;
    execute 'alter table schule.aufgabe add constraint aufgabe_antworttyp_check ' || c_typ;
  elsif v_ist <> v_soll then
    raise exception 'BD-S2: aufgabe_antworttyp_check hat eine unerwartete Fassung: %', v_ist;
  end if;
  select pg_get_constraintdef(oid) into v_ist from pg_constraint where conname = 'aufgabe_bedingung_gueltig' and conrelid = 'schule.aufgabe'::regclass;
  select pg_get_constraintdef(oid) into v_soll from pg_constraint where conname = 'z_gueltig' and conrelid = 'pg_temp.bd_s2_zwilling'::regclass;
  if v_ist is null then
    execute 'alter table schule.aufgabe add constraint aufgabe_bedingung_gueltig ' || c_gueltig;
  elsif v_ist <> v_soll then
    raise exception 'BD-S2: aufgabe_bedingung_gueltig hat eine unerwartete Fassung: %', v_ist;
  end if;
end $$;
