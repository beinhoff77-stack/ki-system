-- RB-S (Regelbezug, Teil Datenbank): Regel-Kennung und Fehlbilder je Aufgabe; Rückmeldung bei falscher Antwort; erkanntes Fehlbild im Versuch.
-- Plan und Begründung: inhalte/plan/regelbezug.md. Einspielen NUR über das selbstprüfende Paket tools/tests/regelbezug_einspielen.py (eine Transaktion);
-- die Daten (Regeln/Fehlbilder der schon eingespielten Aufgaben) danach getrennt mit tools/regelbezug_sql.py (je Runde ein Paket).
--
-- WAS
-- 1. Zwei EIGENE Tabellen (der Aufgaben-Datensatz bleibt unberührt; aufgabe_schutz bleibt, wie er ist):
--      schule.aufgabe_regel     (aufgabe_id PK) regel = Kennung aus inhalte/mathe-profi/regeln-uebersicht/kennungen.json (rr.… / id.…)
--      schule.aufgabe_fehlbild  (aufgabe_id, nr) nr = Platz in der Liste „fehlbilder“ der Aufgaben-Datei (1, 2, …; Lücken in nr = nicht
--                               übernommene Einträge); art zahl | index | luecke | text, luecke (1-basiert, nur bei art luecke), wert (normiert:
--                               Zahl mit Punkt, Index als Zahl, Text wie in der Datei), beschreibung (Rückmeldung fürs Kind), fehlbild (fb.…), regel.
--    Je Aufgabe ist jeder Schlüssel (art, luecke, wert) höchstens einmal da (eindeutiger Index): ein Fehlbild ist an der Antwort eindeutig erkennbar.
--    Beide Tabellen: Row-Level-Security an, keine Policy, keine Rechte für anon/authenticated (wie die übrigen schule-Tabellen; Lesen nur über
--    die security-definer-Funktionen). Schutz wie bei den Aufgaben: kein UPDATE/DELETE, solange die Einheit der Aufgabe freigegeben ist
--    (schule.regelbezug_schutz; Expeditions-Aufgaben ausgenommen wie in aufgabe_schutz). Einfügen ist erlaubt (Nachtrag).
-- 2. schule.fehlbild_finden(aufgabe, antwort) -> nr oder null. Normiert die Antwort wie schule.antwort_bewerten. zahl: Wert innerhalb der
--    Toleranz der Aufgabe; auswahl/markierung: Index; luecken: NUR die erste falsche Lücke zählt (spätere sind oft Folgefehler); text: ohne
--    Leerzeichen, Groß/Klein egal. Richtige Antwort, Formatfehler, kein oder mehr als ein Treffer -> null. Fehler in der Funktion -> null
--    (die Bewertung darf daran nie scheitern).
-- 3. schule.regelbezug_antwort(aufgabe, antwort, richtig, endgueltig) -> jsonb oder null (null bei richtig oder ohne Daten):
--      {regel, fehlbild, fehlbild_nr, fehlbild_regel, text}   – fehlende Felder fehlen (jsonb_strip_nulls).
--    endgueltig = false (erster Fehlversuch mit zweiter Chance, „nochmal“): NUR regel – die Beschreibung kann ein Zwischenergebnis verraten.
-- 4. schule.uebung_pruefen_intern liefert das Objekt als Feld „regelbezug“ (Text-Patch auf die Live-Definition, Stellen aus BD-S2):
--      endgültige Antwort (4 Stellen „…'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a)“) und wiederholte endgültige Übertragung
--      (aus dem gespeicherten Versuch): volles Objekt; erster Fehlversuch und dessen Wiederholung: nur regel.
--    Ohne Daten in den neuen Tabellen ist das Feld null und fällt weg: Bestand antwortet Zeichen für Zeichen wie bisher.
-- 5. schule.versuch bekommt fehlbild_nr (smallint) und fehlbild (text, Kennung), beide nullable, ohne Vorgabe (kein Umschreiben, kein UPDATE).
--    Ein BEFORE-INSERT-Trigger (schule.versuch_fehlbild) setzt sie bei jeder falschen Antwort (Übung, Mischkarte, Expedition, Test), wenn ein
--    gespeichertes Fehlbild passt. Fehler im Trigger -> Versuch wird ohne Fehlbild gespeichert (nie abgewiesen).
-- 6. schule.versuch_regelbezug(versuch) -> jsonb für „Was wackelt“ (Stufe 2): wie 3, aus dem gespeicherten fehlbild_nr; für Versuche von vor RB-S
--    (fehlbild_nr leer, falsch) nachträglich berechnet, dann mit nachtraeglich = true.
-- 7. schule.fehlbild_probeantwort(aufgabe, art, luecke, wert) -> eine Antwort, die genau dieses Fehlbild zeigt (für die Prüfungen der Pakete).
--
-- WIE: neue Funktionen mit create or replace, Rechte revoke von public, anon, authenticated. uebung_pruefen_intern per Text-Patch
-- (je Stelle alter Text, neuer Text, erwartete Anzahl; alt -> ersetzen, fertig -> nichts, sonst Abbruch; halb umgestellt = Abbruch).
--
-- WAS NICHT: keine Spalte an schule.aufgabe, keine Änderung an aufgabe_schutz, kein UPDATE/DELETE von Daten, kein DROP. Keine Daten (die kommen
-- mit tools/regelbezug_sql.py). Keine Lese-Aktion für Eltern („Was wackelt“ Stufe 2 baut auf 5/6 auf). Die Zuordnung Lernkarte -> Regel
-- (Erklärkarte, Rückfall für Aufgaben ohne Regel) liegt NICHT in der Datenbank, sondern als Datei (inhalte/plan/regelbezug-lernkarten.json,
-- für den Client als statische Daten). Tests und Expeditionen bekommen kein „regelbezug“ in der Antwort (nur der Versuch speichert das Fehlbild).
-- Wiederholbar: ein zweiter Lauf ändert nichts.
-- Sperre: ALTER TABLE hält schule.versuch bis zum Ende der Transaktion (auch für Lesen) – nur in einer Nutzungspause einspielen.

select set_config('lock_timeout', '3s', true);

do $$ begin
  if to_regprocedure('schule.loesung_sicht(schule.aufgabe)') is null or to_regprocedure('schule.aufgabe_zaehlt(schule.aufgabe)') is null
     or to_regprocedure('schule.antwort_bewerten(schule.aufgabe, jsonb)') is null or to_regprocedure('schule.uebung_pruefen_intern(bigint, jsonb)') is null
  then raise exception 'RB-S: Voraussetzung fehlt (BD-S2, FT-S)'; end if;
end $$;

-- 1. Tabellen
create table if not exists schule.aufgabe_regel (
  aufgabe_id bigint primary key references schule.aufgabe(id) on delete cascade,
  regel text not null,
  am timestamptz not null default now(),
  constraint aufgabe_regel_kennung_check check (regel ~ '^(rr|id)\.[a-z0-9_.]+$')
);
create table if not exists schule.aufgabe_fehlbild (
  aufgabe_id bigint not null references schule.aufgabe(id) on delete cascade,
  nr smallint not null,
  art text not null,
  luecke smallint,
  wert text not null,
  beschreibung text not null,
  fehlbild text,
  regel text,
  am timestamptz not null default now(),
  primary key (aufgabe_id, nr),
  constraint aufgabe_fehlbild_nr_check check (nr >= 1),
  constraint aufgabe_fehlbild_art_check check (art in ('zahl', 'index', 'luecke', 'text')),
  constraint aufgabe_fehlbild_luecke_check check ((art = 'luecke') = (luecke is not null) and (luecke is null or luecke >= 1)),
  constraint aufgabe_fehlbild_wert_check check (case art when 'index' then wert ~ '^\d{1,4}$' when 'text' then length(wert) between 1 and 200
                                                     else wert ~ '^-?\d{1,15}(\.\d{1,15})?$' end),
  constraint aufgabe_fehlbild_beschreibung_check check (length(beschreibung) between 1 and 600),
  constraint aufgabe_fehlbild_kennung_check check (fehlbild is null or fehlbild ~ '^fb\.[a-z0-9_.]+$'),
  constraint aufgabe_fehlbild_regel_check check (regel is null or regel ~ '^(rr|id)\.[a-z0-9_.]+$')
);
create unique index if not exists aufgabe_fehlbild_schluessel on schule.aufgabe_fehlbild (aufgabe_id, art, coalesce(luecke, 0), wert);
alter table schule.aufgabe_regel enable row level security;     -- nur über die security-definer-Funktionen, wie die übrigen schule-Tabellen
alter table schule.aufgabe_fehlbild enable row level security;
revoke all on table schule.aufgabe_regel, schule.aufgabe_fehlbild from public, anon, authenticated;
comment on table schule.aufgabe_regel is 'RB-S: Regel-Kennung (kennungen.json) je Aufgabe; Quelle: Feld regel der Aufgaben-Datei (inhalte/mathe-profi/rollend-*)';
comment on table schule.aufgabe_fehlbild is 'RB-S: Fehlbilder je Aufgabe (nr = Platz in der Liste fehlbilder der Datei); erkannt von schule.fehlbild_finden, Rückmeldung in uebung_pruefen_intern.regelbezug';

-- Schutz wie aufgabe_schutz: freigegebene Einheit = unveränderlich (Einfügen bleibt erlaubt)
create or replace function schule.regelbezug_schutz()
 returns trigger language plpgsql set search_path to ''
as $function$
begin
  if exists (select 1 from schule.aufgabe a join schule.einheit e on e.id = a.einheit_id
              where a.id = old.aufgabe_id and e.status = 'freigegeben' and a.pool is distinct from 'expedition') then
    raise exception 'RB-S: Regel und Fehlbilder einer Aufgabe in einer freigegebenen Einheit sind unveränderlich (Berichtigung = neue Aufgabe)';
  end if;
  return coalesce(new, old);
end $function$;
do $$ begin
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.aufgabe_regel'::regclass and tgname = 'aufgabe_regel_schutz') then
    create trigger aufgabe_regel_schutz before update or delete on schule.aufgabe_regel for each row execute function schule.regelbezug_schutz();
  end if;
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.aufgabe_fehlbild'::regclass and tgname = 'aufgabe_fehlbild_schutz') then
    create trigger aufgabe_fehlbild_schutz before update or delete on schule.aufgabe_fehlbild for each row execute function schule.regelbezug_schutz();
  end if;
end $$;

-- 2. Erkennen
create or replace function schule.fehlbild_finden(a schule.aufgabe, p_antwort jsonb)
 returns smallint language plpgsql stable set search_path to ''
as $function$
declare s text; e text; v numeric; tol numeric; i int; n int := 0; v_nr smallint; v_soll jsonb;
begin
  if a.id is null or jsonb_typeof(p_antwort) is distinct from 'object' then return null; end if;
  if not exists (select 1 from schule.aufgabe_fehlbild f where f.aufgabe_id = a.id) then return null; end if;
  if a.antworttyp in ('auswahl', 'markierung') then
    if coalesce(p_antwort->>'index', '') !~ '^\d{1,4}$' or (p_antwort->>'index')::int = (a.loesung->>'index')::int then return null; end if;
    select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
     where f.aufgabe_id = a.id and f.art = 'index' and f.wert::int = (p_antwort->>'index')::int;
  elsif a.antworttyp = 'luecken' then
    v_soll := a.loesung->'werte';
    if jsonb_typeof(p_antwort->'werte') is distinct from 'array' or jsonb_typeof(v_soll) is distinct from 'array'
       or jsonb_array_length(p_antwort->'werte') <> jsonb_array_length(v_soll) then return null; end if;
    for i in 0 .. jsonb_array_length(v_soll) - 1 loop
      s := replace(replace(regexp_replace(coalesce(p_antwort->'werte'->>i, ''), '[\s  ]', '', 'g'), '−', '-'), '–', '-');
      if left(s, 1) = '+' then s := substr(s, 2); end if;
      if s !~ '^-?\d{1,15}$' then return null; end if;
      if s::numeric <> (v_soll->>i)::numeric then   -- erste falsche Lücke: nur sie zählt
        select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
         where f.aufgabe_id = a.id and f.art = 'luecke' and f.luecke = i + 1 and f.wert::numeric = s::numeric;
        exit;
      end if;
    end loop;
  elsif a.antworttyp = 'text' then
    s := upper(regexp_replace(coalesce(p_antwort->>'wert', ''), '[\s  ]', '', 'g'));
    if s = '' or s = upper(a.loesung->>'text') then return null; end if;
    select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
     where f.aufgabe_id = a.id and f.art = 'text' and upper(regexp_replace(f.wert, '[\s  ]', '', 'g')) = s;
  elsif a.antworttyp = 'zahl' then
    s := regexp_replace(coalesce(p_antwort->>'wert', ''), '[\s  ]', '', 'g');
    if s = '' or position('.' in s) > 0 then return null; end if;
    e := a.loesung->>'einheit';
    if e is not null then s := replace(s, e, ''); end if;
    s := replace(replace(s, '−', '-'), ',', '.');
    if s !~ '^-?\d{1,15}(\.\d{1,15})?$' then return null; end if;
    v := s::numeric;
    tol := greatest(1e-9, coalesce((a.loesung->>'toleranz')::numeric, 0));
    if abs(v - (a.loesung->>'wert')::numeric) <= tol then return null; end if;
    select min(f.nr), count(*) into v_nr, n from schule.aufgabe_fehlbild f
     where f.aufgabe_id = a.id and f.art = 'zahl' and abs(f.wert::numeric - v) <= tol;
  end if;
  return case when n = 1 then v_nr end;
exception when others then
  return null;   -- die Bewertung darf an der Fehlbild-Suche nie scheitern
end $function$;
comment on function schule.fehlbild_finden(schule.aufgabe, jsonb) is 'RB-S: nr des Fehlbilds, das die (falsche) Antwort zeigt; null bei richtig, Formatfehler, keinem oder mehr als einem Treffer. Lücken: nur die erste falsche Lücke';

-- 3. Rückmeldung
create or replace function schule.regelbezug_antwort(a schule.aufgabe, p_antwort jsonb, p_richtig boolean, p_endgueltig boolean)
 returns jsonb language sql stable set search_path to ''
as $function$
  select case when p_richtig is distinct from false or a.id is null then null else
    nullif(jsonb_strip_nulls(jsonb_build_object(
      'regel', (select r.regel from schule.aufgabe_regel r where r.aufgabe_id = a.id),
      'fehlbild', f.fehlbild, 'fehlbild_nr', f.nr, 'fehlbild_regel', f.regel, 'text', f.beschreibung)), '{}'::jsonb) end
    from (select case when p_endgueltig then schule.fehlbild_finden(a, p_antwort) end nr) k
    left join schule.aufgabe_fehlbild f on f.aufgabe_id = a.id and f.nr = k.nr;
$function$;
comment on function schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean) is 'RB-S: Feld regelbezug der Bewertungsantwort {regel, fehlbild, fehlbild_nr, fehlbild_regel, text}; null bei richtig/ohne Daten; nicht endgültig: nur regel';

-- 5. Versuch: erkanntes Fehlbild
alter table schule.versuch add column if not exists fehlbild_nr smallint;
alter table schule.versuch add column if not exists fehlbild text;
comment on column schule.versuch.fehlbild_nr is 'RB-S: nr des erkannten Fehlbilds (schule.aufgabe_fehlbild), gesetzt beim Speichern einer falschen Antwort; leer = keins erkannt oder Versuch von vor RB-S';
comment on column schule.versuch.fehlbild is 'RB-S: Kennung (fb.…) des erkannten Fehlbilds, falls das Fehlbild eine hat';

create or replace function schule.versuch_fehlbild()
 returns trigger language plpgsql set search_path to ''
as $function$
declare a schule.aufgabe; f schule.aufgabe_fehlbild;
begin
  if new.richtig is distinct from false or new.fehlbild_nr is not null then return new; end if;
  begin
    select * into a from schule.aufgabe where id = new.aufgabe_id;
    select * into f from schule.aufgabe_fehlbild x where x.aufgabe_id = a.id and x.nr = schule.fehlbild_finden(a, new.antwort);
    if f.nr is not null then new.fehlbild_nr := f.nr; new.fehlbild := f.fehlbild; end if;
  exception when others then null;   -- nie den Versuch abweisen
  end;
  return new;
end $function$;
do $$ begin
  if not exists (select 1 from pg_trigger where tgrelid = 'schule.versuch'::regclass and tgname = 'versuch_fehlbild') then
    create trigger versuch_fehlbild before insert on schule.versuch for each row execute function schule.versuch_fehlbild();
  end if;
end $$;

-- 6. Lesen für „Was wackelt“
create or replace function schule.versuch_regelbezug(v schule.versuch)
 returns jsonb language sql stable set search_path to ''
as $function$
  with n as (select coalesce(v.fehlbild_nr, case when not v.richtig then (select schule.fehlbild_finden(x, v.antwort) from schule.aufgabe x where x.id = v.aufgabe_id) end) nr)
  select case when v.richtig then null else nullif(jsonb_strip_nulls(jsonb_build_object(
    'regel', (select r.regel from schule.aufgabe_regel r where r.aufgabe_id = v.aufgabe_id),
    'fehlbild', f.fehlbild, 'fehlbild_nr', f.nr, 'fehlbild_regel', f.regel, 'text', f.beschreibung,
    'nachtraeglich', case when v.fehlbild_nr is null and f.nr is not null then true end)), '{}'::jsonb) end
    from n left join schule.aufgabe_fehlbild f on f.aufgabe_id = v.aufgabe_id and f.nr = n.nr;
$function$;

-- 7. Probe-Antwort zu einem Fehlbild (für die Prüfungen der Pakete)
create or replace function schule.fehlbild_probeantwort(a schule.aufgabe, p_art text, p_luecke int, p_wert text)
 returns jsonb language sql immutable set search_path to ''
as $function$
  select case p_art
    when 'index' then jsonb_build_object('index', p_wert::int)
    when 'text' then jsonb_build_object('wert', p_wert)
    when 'zahl' then jsonb_build_object('wert', replace(p_wert, '.', ','))
    when 'luecke' then jsonb_build_object('werte', (select jsonb_agg(case when o = p_luecke then to_jsonb(p_wert::numeric) else x end order by o)
                                                     from jsonb_array_elements(a.loesung->'werte') with ordinality t(x, o)))
  end;
$function$;

revoke all on function schule.regelbezug_schutz(), schule.fehlbild_finden(schule.aufgabe, jsonb), schule.regelbezug_antwort(schule.aufgabe, jsonb, boolean, boolean),
  schule.versuch_fehlbild(), schule.versuch_regelbezug(schule.versuch), schule.fehlbild_probeantwort(schule.aufgabe, text, integer, text)
  from public, anon, authenticated;

-- 4. Text-Patch uebung_pruefen_intern. Zustände je Eintrag:
--   alt    = alt steht genau so oft da wie erwartet, neu gar nicht  -> ersetzen
--   fertig = alt steht nicht mehr da, neu genau so oft wie erwartet -> nichts tun
--   sonst  -> Abbruch. Auch Abbruch, wenn manche Stellen alt und andere fertig sind.
do $$
declare
  f record; e jsonb; d text; d0 text; n_alt int; n_neu int; soll int; z_alt int; z_fertig int;
  zaehle constant text := 'select (length($1) - length(replace($1, $2, ''''))) / length($2)';
  plan constant jsonb := jsonb_build_array(
    jsonb_build_object('f', 'schule.uebung_pruefen_intern(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array($a$'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'loesung', schule.loesung_sicht(a)$a$,
                        $a$'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, p_daten->'antwort', (b->>'richtig')::boolean, true), 'loesung', schule.loesung_sicht(a)$a$, 4),
      jsonb_build_array($a$'richtig', false, 'nochmal', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$,
                        $a$'richtig', false, 'nochmal', true, 'grund', b->>'grund', 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, p_daten->'antwort', false, false)));$a$, 1),
      jsonb_build_array($a$'wiederholt', true) || jsonb_strip_nulls(jsonb_build_object('verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$,
                        $a$'wiederholt', true) || jsonb_strip_nulls(jsonb_build_object('verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, v_alt.antwort, v_alt.richtig, true)));$a$, 1),
      jsonb_build_array($a$'nochmal', true, 'wiederholt', true, 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis'));$a$,
                        $a$'nochmal', true, 'wiederholt', true, 'verletzt', b->>'verletzt', 'hinweis', b->>'hinweis', 'regelbezug', schule.regelbezug_antwort(a, v_alt.antwort, false, false)));$a$, 1))));
begin
  for f in select x->>'f' as name, x->'p' as p from jsonb_array_elements(plan) x loop
    if to_regprocedure(f.name) is null then raise exception 'RB-S: Funktion % fehlt', f.name; end if;
    d0 := pg_get_functiondef(to_regprocedure(f.name)); d := d0; z_alt := 0; z_fertig := 0;
    for e in select * from jsonb_array_elements(f.p) loop
      soll := (e->>2)::int;
      execute zaehle into n_alt using d, e->>0;
      execute zaehle into n_neu using d, e->>1;
      if n_alt = soll and n_neu = 0 then d := replace(d, e->>0, e->>1); z_alt := z_alt + 1;
      elsif n_alt = 0 and n_neu = soll then z_fertig := z_fertig + 1;
      else raise exception 'RB-S: % ist weder im alten noch im fertigen Zustand (Stelle „%…“: alt %, neu %, erwartet %)', f.name, left(e->>0, 50), n_alt, n_neu, soll;
      end if;
    end loop;
    if z_alt > 0 and z_fertig > 0 then raise exception 'RB-S: % ist halb umgestellt (% Stellen alt, % fertig)', f.name, z_alt, z_fertig; end if;
    if d is distinct from d0 then execute d; end if;
  end loop;
end $$;
