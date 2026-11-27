-- FT-S (Form-Takt, Teil Datenbank): neue Aufgabenformen im festen Takt und Sachaufgaben-Pflicht. Vorgabe: inhalte/plan/form-takt.md (Regeln 1–8),
-- Bericht: inhalte/plan/form-takt-bau.md. Einspielen NUR über das selbstprüfende Paket tools/tests/form_takt_einspielen.py (eine Transaktion).
--
-- WAS
-- 1. schule.aufgabe bekommt zwei neue, freiwillige Spalten (nullable, kein Massen-UPDATE; leer = Bestand):
--      form    leer = Bestand, sonst lueckenweg | fehler_detektiv | verfahren_waehlen | zwei_wege | umkehren | bruecke | anwenden | viele_antworten
--      zaehlt  leer = ja (Bestand verhält sich wie bisher), sonst ja | nein       – beide mit Prüfbedingung, unbekannte Werte werden abgewiesen
-- 2. Regel form_jede (Vorgabe 3) in schule.regel; einheit_lesen_intern liefert sie (wie misch_jede). Die App wählt den Takt weiter selbst.
-- 3. Ein gemeinsamer Filter schule.aufgabe_zaehlt(a) (Regel 5) an allen Stellen, an denen Rechenbelege entstehen oder gezählt werden:
--      karte_buchen (Aufgabe mit zaehlt = nein ändert an der Karte NICHTS – keine Zeile, kein Zähler, Folge neutral), misch_buchen,
--      expedition_buchen (kein Beleg, nichts fällig; Sterne für die geschaffte Expedition wie bisher), folge_nachrechnen, landung_zaehlen,
--      karte_ziel, karte_typen_noetig, karte_schwer_noetig, wdh_aufgabe_waehlen (damit auch Mischkarten), wdh_aufgabe_da (beide Fassungen).
--    Bewertet und als Versuch gespeichert wird jede Aufgabe wie bisher (uebung_pruefen_intern bleibt dort unverändert).
-- 4. Sachaufgaben-Pflicht (Regel 6) in der gemeinsamen Landeregel schule.karte_landet: Eine Lernkarte landet nur, wenn unter den gezählten Aufgaben
--    (karte_stand.gezaehlt) eine der Art „anwenden“ ist (Typ einkleidung, transfer, pruefung – schule.aufgabe_anwenden) – aber nur, wenn
--      a) die Lernkarte eine freigegebene, zählende Übung dieser Art hat (schule.karte_anwenden_noetig), und
--      b) die Karte noch nie gelandet ist (sitzt_am leer, nicht sitzt). Gelandete, wieder geöffnete und gesetzte Karten: keine Pflicht – nichts wird
--         zurückgenommen, Rücknahme und Rückgängig (karte_landet bei sitzenden Karten) verhalten sich wie bisher.
--    „anwenden erfüllt“ wird abgeleitet (schule.karte_anwenden_ok aus karte_stand.gezaehlt), keine neue Spalte: gezaehlt ist schon die Liste der
--    gezählten Aufgaben, wird beim Nachrechnen der Folge nicht berührt und bleibt beim Wiederöffnen erhalten; früher gelöste Sachaufgaben zählen mit.
-- 5. Neue Felder für die App (nur Ausgaben ergänzt, nichts entfernt):
--      aufgabe_anzeige: form, zaehlt (nur wenn gesetzt)
--      uebung_pruefen_intern.karte und etappen_stand[lernziel]: anwenden_noetig, anwenden_ok, bearbeitungen
--      einheit_lesen_intern: form_jede
--    bearbeitungen = Zahl der Bearbeitungen des Kindes an der Lernkarte (Übungsversuche ohne Test und ohne Mischkarte, der 2. Anlauf derselben
--    Aufgabe zählt nicht extra) – daraus der Platz im Takt, über Geräte und Sitzungen gleich.
-- 6. aufgaben_einfuegen übernimmt form und zaehlt aus dem JSON.
-- 7. Nachträge nach Gegenprüfung 1030/1032:
--    a) Schalter anwenden_pflicht (Regel in schule.regel, 0 = aus, 1 = an; beim Einspielen 0). Er sitzt an EINER Stelle, in
--       schule.karte_anwenden_pflicht – die nutzen karte_landet (Landeregel) und beide Ausgaben anwenden_noetig. Aus = keine Sachaufgaben-Pflicht,
--       anwenden_noetig = false. Einschalten: update schule.regel set wert = '1'::jsonb where schluessel = 'anwenden_pflicht';
--       Ein zweiter Lauf der Migration setzt den Schalter nicht zurück (on conflict do nothing).
--    b) uebung_pruefen_intern: die Antwort auf eine Übung (Weg mit Lösung, nicht Mischkarte/Knobel/Expedition) trägt bearbeitungen auch
--       AUSSERHALB von karte – nach der ersten nicht zählenden Aufgabe einer Lernkarte gibt es noch keine Kartenzeile und damit kein karte.
--
-- WIE: neue Hilfsfunktionen mit create or replace (Rechte: revoke von public, anon, authenticated). Bestehende Funktionen per Text-Patch auf die
-- Live-Definition (je Stelle: alter Text, neuer Text, erwartete Anzahl; drei Zustände wie BD-S2: alt -> ersetzen, fertig -> nichts, sonst Abbruch;
-- halb umgestellte Funktion = Abbruch). Rechte bestehender Funktionen bleiben (create or replace aus pg_get_functiondef).
--
-- WAS NICHT: keine Spalte an karte_stand, kein UPDATE/DELETE von Daten, kein DROP. Tests (Flug-Test, Nachtest) unverändert (Regel 7). Der Takt selbst,
-- der Lückenweg nach zwei Fehlern und die Anzeige „Sachaufgabe fehlt noch“ sind App-Sache. einheit_abgleichen ändert form/zaehlt vorhandener
-- Aufgaben nicht (nur neue Aufgaben über aufgaben_einfuegen). Wiederholbar: ein zweiter Lauf ändert nichts.
-- Sperre: ALTER TABLE hält schule.aufgabe bis zum Ende der Transaktion (auch für Lesen) – nur in einer Nutzungspause einspielen.

do $$ begin
  if to_regprocedure('schule.karte_landet(schule.karte_stand)') is null or to_regprocedure('schule.loesung_sicht(schule.aufgabe)') is null
     or to_regprocedure('schule.wd_regel(text, integer)') is null then raise exception 'FT-S: Voraussetzung fehlt (LB-3 Nachbesserung, WD-S, BD-S2)'; end if;
end $$;

-- 1. Spalten (nullable, ohne Vorgabewert: kein Umschreiben der Tabelle, Bestand bleibt leer)
alter table schule.aufgabe add column if not exists form text;
alter table schule.aufgabe add column if not exists zaehlt text;
comment on column schule.aufgabe.form is 'FT-S: neue Aufgabenform (leer = Bestand): lueckenweg|fehler_detektiv|verfahren_waehlen|zwei_wege|umkehren|bruecke|anwenden|viele_antworten';
comment on column schule.aufgabe.zaehlt is 'FT-S: zählt für Karte/„sitzt“ (leer = ja): ja|nein. nein = wird bewertet und gespeichert, ändert an der Karte nichts';

-- Prüfbedingungen: Soll-Fassung über einen Zwilling an einer Temp-Tabelle (so, wie die Datenbank sie schreibt); jede andere Fassung = Abbruch
do $$
declare v_ist text; v_soll text; c record;
begin
  if to_regclass('pg_temp.ft_zwilling') is null then
    create temp table ft_zwilling (form text, zaehlt text,
      constraint aufgabe_form_check check (form is null or form in ('lueckenweg', 'fehler_detektiv', 'verfahren_waehlen', 'zwei_wege', 'umkehren', 'bruecke', 'anwenden', 'viele_antworten')),
      constraint aufgabe_zaehlt_check check (zaehlt is null or zaehlt in ('ja', 'nein'))) on commit drop;
  end if;
  for c in select conname, pg_get_constraintdef(oid) d from pg_constraint where conrelid = 'pg_temp.ft_zwilling'::regclass and contype = 'c' order by conname loop
    select pg_get_constraintdef(oid) into v_ist from pg_constraint where conname = c.conname and conrelid = 'schule.aufgabe'::regclass;
    if v_ist is null then execute format('alter table schule.aufgabe add constraint %I %s', c.conname, c.d);
    elsif v_ist <> c.d then raise exception 'FT-S: % hat eine unerwartete Fassung: %', c.conname, v_ist;
    end if;
  end loop;
end $$;

-- 2. Regel
insert into schule.regel (schluessel, wert, hinweis) values ('form_jede', '3'::jsonb, 'FT-S: je Lernkarte jede n-te Bearbeitung eine Aufgabe mit neuer Form (Plätze n, 2n, …), wenn eine ungelöste da ist')
  on conflict (schluessel) do nothing;
-- Schalter Sachaufgaben-Pflicht (Nachtrag 1032): 0 = aus bis zur App 0.94.0. Kein Zurücksetzen bei einem zweiten Lauf.
insert into schule.regel (schluessel, wert, hinweis) values ('anwenden_pflicht', '0'::jsonb, 'FT-S Regel 6: Sachaufgaben-Pflicht 1 = an, 0 = aus (an erst mit App ab 0.94.0)')
  on conflict (schluessel) do nothing;

-- 3./4. Hilfsfunktionen
create or replace function schule.aufgabe_zaehlt(a schule.aufgabe)
 returns boolean language sql immutable set search_path to ''
as $function$
  select a.zaehlt is distinct from 'nein';
$function$;
comment on function schule.aufgabe_zaehlt(schule.aufgabe) is 'FT-S Regel 5: ist die Aufgabe ein Rechenbeleg (zaehlt leer oder ja)';

create or replace function schule.aufgabe_anwenden(a schule.aufgabe)
 returns boolean language sql immutable set search_path to ''
as $function$
  select coalesce(a.typ in ('einkleidung', 'transfer', 'pruefung'), false);
$function$;
comment on function schule.aufgabe_anwenden(schule.aufgabe) is 'FT-S Regel 6: Art „anwenden“ (Typ g einkleidung, transfer, pruefung – Tabelle in inhalte/mathe-profi/rollend-2/verhaeltnis.md)';

create or replace function schule.karte_anwenden_noetig(p_einheit bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from schule.aufgabe a
   where a.einheit_id = p_einheit and a.pool = 'uebung' and a.variante_gruppe = p_lz and a.freigegeben and schule.aufgabe_zaehlt(a) and schule.aufgabe_anwenden(a));
$function$;

create or replace function schule.karte_anwenden_pflicht(k schule.karte_stand, p_einheit bigint, p_lz text)
 returns boolean language sql stable set search_path to ''
as $function$
  select schule.wd_regel('anwenden_pflicht', 0) = 1
     and k.sitzt_am is null and not coalesce(k.sitzt, false) and schule.karte_anwenden_noetig(p_einheit, p_lz);
$function$;
comment on function schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text) is 'FT-S Regel 6: Sachaufgabe nötig – nur bei Schalter anwenden_pflicht = 1, nur für nie gelandete Karten und nur, wenn die Lernkarte eine freigegebene, zählende Übung der Art anwenden hat';

create or replace function schule.karte_anwenden_ok(k schule.karte_stand)
 returns boolean language sql stable set search_path to ''
as $function$
  select exists (select 1 from jsonb_object_keys(coalesce(k.gezaehlt, '{}'::jsonb)) x join schule.aufgabe a on a.id = x::bigint
                  where schule.aufgabe_anwenden(a) and schule.aufgabe_zaehlt(a));
$function$;
comment on function schule.karte_anwenden_ok(schule.karte_stand) is 'FT-S Regel 6: unter den gezählten Aufgaben (gezaehlt) ist eine der Art anwenden';

create or replace function schule.karte_bearbeitungen(p_l bigint, p_e bigint, p_lz text)
 returns integer language sql stable set search_path to ''
as $function$
  select count(*)::int from schule.versuch v join schule.aufgabe a on a.id = v.aufgabe_id
   where v.lernender_id = p_l and a.einheit_id = p_e and a.variante_gruppe = p_lz and a.pool = 'uebung'
     and v.testsitzung_id is null and not coalesce(v.misch, false) and coalesce(v.anlauf, 1) <> 2;
$function$;
comment on function schule.karte_bearbeitungen(bigint, bigint, text) is 'FT-S Regel 2: Bearbeitungen des Kindes an der Lernkarte (ohne Test, ohne Mischkarte; 2. Anlauf derselben Aufgabe zählt nicht extra)';

revoke all on function schule.aufgabe_zaehlt(schule.aufgabe), schule.aufgabe_anwenden(schule.aufgabe), schule.karte_anwenden_noetig(bigint, text),
  schule.karte_anwenden_pflicht(schule.karte_stand, bigint, text), schule.karte_anwenden_ok(schule.karte_stand), schule.karte_bearbeitungen(bigint, bigint, text)
  from public, anon, authenticated;

-- 5. Text-Patches. Je Funktion eine Liste (alt, neu, erwartete Anzahl). Zustände je Eintrag:
--   alt    = alt steht genau so oft da wie erwartet, neu gar nicht  -> ersetzen
--   fertig = alt steht nicht mehr da, neu genau so oft wie erwartet -> nichts tun
--   sonst  -> Abbruch. Auch Abbruch, wenn in EINER Funktion manche Stellen alt und andere fertig sind.
do $$
declare
  f record; e jsonb; d text; d0 text; n_alt int; n_neu int; soll int; z_alt int; z_fertig int;
  zaehle constant text := 'select (length($1) - length(replace($1, $2, ''''))) / length($2)';
  plan constant jsonb := jsonb_build_array(
    jsonb_build_object('f', 'schule.aufgabe_anzeige(schule.aufgabe, boolean)', 'p', jsonb_build_array(
      jsonb_build_array($a$'typ', a.typ, 'bonus'$a$, $a$'typ', a.typ, 'form', a.form, 'zaehlt', a.zaehlt, 'bonus'$a$, 1))),
    jsonb_build_object('f', 'schule.aufgaben_einfuegen(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array($a$reihenfolge, pool, typ)$a$, $a$reihenfolge, pool, typ, form, zaehlt)$a$, 1),
      jsonb_build_array($a$x->>'g' from q$a$, $a$x->>'g', x->>'form', x->>'zaehlt' from q$a$, 1))),
    jsonb_build_object('f', 'schule.karte_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$if a.id is null or a.pool <> 'uebung' then return; end if;$a$, $a$if a.id is null or a.pool <> 'uebung' or not schule.aufgabe_zaehlt(a) then return; end if;$a$, 1))),
    jsonb_build_object('f', 'schule.misch_buchen(bigint, bigint, boolean, smallint, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$if a.id is null or a.pool <> 'uebung' then return; end if;$a$, $a$if a.id is null or a.pool <> 'uebung' or not schule.aufgabe_zaehlt(a) then return; end if;$a$, 1))),
    jsonb_build_object('f', 'schule.expedition_buchen(bigint, bigint, boolean, smallint, smallint, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$coalesce(p_anlauf, 1) = 1 then$a$, $a$coalesce(p_anlauf, 1) = 1 and schule.aufgabe_zaehlt(a) then$a$, 1),
      jsonb_build_array($a$a.variante_gruppe, p_zeit); -- H8$a$, $a$a.variante_gruppe, p_zeit) where schule.aufgabe_zaehlt(a); -- H8$a$, 1))),
    jsonb_build_object('f', 'schule.karte_landet(schule.karte_stand)', 'p', jsonb_build_array(
      jsonb_build_array($a$least(3, schule.karte_ziel(k.einheit_id, k.lernziel));$a$, $a$least(3, schule.karte_ziel(k.einheit_id, k.lernziel))
     and (schule.karte_anwenden_ok(k) or not schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel)); -- FT-S Regel 6$a$, 1))),
    jsonb_build_object('f', 'schule.karte_ziel(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_einheit and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and$a$, 1))),
    jsonb_build_object('f', 'schule.karte_typen_noetig(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_einheit and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and$a$, 1))),
    jsonb_build_object('f', 'schule.karte_schwer_noetig(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_einheit and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_einheit and$a$, 1))),
    jsonb_build_object('f', 'schule.folge_nachrechnen(bigint, bigint, text, timestamp with time zone)', 'p', jsonb_build_array(
      jsonb_build_array($a$a.variante_gruppe = p_lz and a.pool = 'uebung'$a$, $a$a.variante_gruppe = p_lz and schule.aufgabe_zaehlt(a) and a.pool = 'uebung'$a$, 1))),
    jsonb_build_object('f', 'schule.landung_zaehlen(bigint, bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$a.variante_gruppe = p_lz and a.pool = 'uebung'$a$, $a$a.variante_gruppe = p_lz and schule.aufgabe_zaehlt(a) and a.pool = 'uebung'$a$, 2))),
    jsonb_build_object('f', 'schule.wdh_aufgabe_waehlen(bigint, bigint, text, boolean)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_e and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and$a$, 1))),
    jsonb_build_object('f', 'schule.wdh_aufgabe_da(bigint, bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_e and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and$a$, 1))),
    jsonb_build_object('f', 'schule.wdh_aufgabe_da(bigint, text)', 'p', jsonb_build_array(
      jsonb_build_array($a$where a.einheit_id = p_e and$a$, $a$where schule.aufgabe_zaehlt(a) and a.einheit_id = p_e and$a$, 1))),
    jsonb_build_object('f', 'schule.uebung_pruefen_intern(bigint, jsonb)', 'p', jsonb_build_array(
      jsonb_build_array($a$'schwer_ok', k.schwer_ok, 'schwer_noetig'$a$, $a$'schwer_ok', k.schwer_ok, 'anwenden_noetig', schule.karte_anwenden_pflicht(k, k.einheit_id, k.lernziel), 'anwenden_ok', schule.karte_anwenden_ok(k),
                'bearbeitungen', schule.karte_bearbeitungen(k.lernender_id, k.einheit_id, k.lernziel), 'schwer_noetig'$a$, 1),
      jsonb_build_array($a$k.lernziel = a.variante_gruppe)));$a$, $a$k.lernziel = a.variante_gruppe), 'bearbeitungen', schule.karte_bearbeitungen(p_lernender, a.einheit_id, a.variante_gruppe)));$a$, 1))),
    jsonb_build_object('f', 'schule.etappen_stand(bigint, bigint)', 'p', jsonb_build_array(
      jsonb_build_array($a$'schwer_ok', coalesce(k.schwer_ok, false), 'schwer_noetig'$a$, $a$'schwer_ok', coalesce(k.schwer_ok, false), 'anwenden_noetig', schule.karte_anwenden_pflicht(k, p_einheit, z.lz), 'anwenden_ok', coalesce(schule.karte_anwenden_ok(k), false),
           'bearbeitungen', schule.karte_bearbeitungen(p_lernender, p_einheit, z.lz), 'schwer_noetig'$a$, 1))),
    jsonb_build_object('f', 'schule.einheit_lesen_intern(bigint, bigint)', 'p', jsonb_build_array(
      jsonb_build_array($a$'heute_tag', schule.heute_tag(p_lernender), 'heute_bis'$a$, $a$'heute_tag', schule.heute_tag(p_lernender), 'form_jede', schule.wd_regel('form_jede', 3), 'heute_bis'$a$, 1))));
begin
  for f in select x->>'f' as name, x->'p' as p from jsonb_array_elements(plan) x loop
    if to_regprocedure(f.name) is null then raise exception 'FT-S: Funktion % fehlt', f.name; end if;
    d0 := pg_get_functiondef(to_regprocedure(f.name)); d := d0; z_alt := 0; z_fertig := 0;
    for e in select * from jsonb_array_elements(f.p) loop
      soll := (e->>2)::int;
      execute zaehle into n_alt using d, e->>0;
      execute zaehle into n_neu using d, e->>1;
      if n_alt = soll and n_neu = 0 then d := replace(d, e->>0, e->>1); z_alt := z_alt + 1;
      elsif n_alt = 0 and n_neu = soll then z_fertig := z_fertig + 1;
      else raise exception 'FT-S: % ist weder im alten noch im fertigen Zustand (Stelle „%…“: alt %, neu %, erwartet %)', f.name, left(e->>0, 40), n_alt, n_neu, soll;
      end if;
    end loop;
    if z_alt > 0 and z_fertig > 0 then raise exception 'FT-S: % ist halb umgestellt (% Stellen alt, % fertig)', f.name, z_alt, z_fertig; end if;
    if d is distinct from d0 then execute d; end if;
  end loop;
end $$;
