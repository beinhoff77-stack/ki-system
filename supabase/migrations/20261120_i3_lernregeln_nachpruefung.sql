-- Bau-Auftrag I, Teil 3 (20.11.): Nachprüfung von ChatGPT zu Teil 2 (Werkstatt-Nachricht 878). Nach 20261120_i2_lernregeln.sql.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE, keine Bestandsänderung. Wiederholt ausführbar.
--
-- H2-1 Endgültige Wertung festhalten: versuch.wertung_fest (eigen | neutral | falsch | ersetzt) wird bei der Entscheidung geschrieben; versuch_wertung liest ihn zuerst.
--      Ein 2. Anlauf nach einem schon endgültig falsch gebuchten 1. Anlauf ist „neutral“ (ändert nichts, bucht keinen Fehler).
-- H2-2 Nachbuchen genau einmal: schule.offene_entscheiden(kind, ausser) beansprucht offene erste Anläufe in einem Schritt
--      (update … set wertung_offen = false … for update skip locked … returning) und bucht nur die beanspruchten.
-- H2-5 30-Minuten-Grenze: offene_entscheiden läuft auch beim Lesen des Flugs (einheit_lesen_intern) und beim Teststart (test_starten_intern).
-- H10-3 Einlösen atomar: misch_buchen bucht den Beleg nur, wenn das Einlösen eine Ausgabe getroffen hat (update … returning), sonst normale Buchung;
--      eindeutiger Index auf offene Ausgaben je Kind und Bordkarte (bricht ab, falls im Bestand Dopplungen liegen – heute gelesen: keine Zeile);
--      schule.mischkarten legt Ausgaben konfliktfest an (insert … on conflict).
-- H10-4 Ausgabe an die Lage binden: misch_ausgabe speichert einheit_id (gelesener Flug) und lernziel (erste noch nicht gelandete Etappe dieses Flugs);
--      misch_gueltig vergleicht mit dieser Lage statt mit den Angaben des Geräts. Ausgaben ohne gespeicherte Lage (aus 0.81.1) prüfen wie bisher die Geräte-Angaben.

-- ---------- H2-1: festgehaltene Wertung ----------
alter table schule.versuch add column if not exists wertung_fest text;
do $mig$ begin
  if not exists (select 1 from pg_constraint where conname = 'versuch_wertung_fest_check') then
    alter table schule.versuch add constraint versuch_wertung_fest_check check (wertung_fest is null or wertung_fest in ('eigen', 'neutral', 'falsch', 'ersetzt'));
  end if;
end $mig$;
comment on column schule.versuch.wertung_fest is 'I-3/H2: bei der Buchung getroffene, endgültige Wertung; null = vor I-3 (dann rechnet versuch_wertung wie bisher)';

create or replace function schule.versuch_wertung(v schule.versuch)
 returns text
 language sql
 stable
 set search_path to ''
as $function$
  select case
    when v.testsitzung_id is not null then 'test'
    when v.wertung_fest is not null then v.wertung_fest            -- I-3: einmal entschieden, bleibt es
    when v.anlauf = 2 and coalesce((select p.anlauf = 1 and p.wertung_fest = 'falsch' from schule.versuch p
                                      where p.lernender_id = v.lernender_id and p.aufgabe_id = v.aufgabe_id and p.testsitzung_id is null
                                        and (p.am, p.id) < (v.am, v.id) order by p.am desc, p.id desc limit 1), false) then 'neutral' -- I-3: 2. Anlauf nach endgültig gebuchtem 1. Anlauf
    when v.richtig and coalesce(v.hilfe, 0) = 0 and coalesce(v.anlauf, 1) = 1 then 'eigen'
    when v.richtig then 'neutral'                                   -- Tipp oder 2. Anlauf richtig: zählt nicht, bricht nichts
    when coalesce(v.anlauf, 0) <> 1 then 'falsch'                   -- ohne zweite Chance oder 2. Anlauf: endgültig
    when exists (select 1 from schule.versuch n where n.lernender_id = v.lernender_id and n.aufgabe_id = v.aufgabe_id and n.testsitzung_id is null
                   and n.anlauf = 2 and (n.am, n.id) > (v.am, v.id) and n.am <= v.am + interval '30 minutes') then 'ersetzt' -- der 2. Anlauf entscheidet
    when v.am < now() - interval '30 minutes'
      or exists (select 1 from schule.versuch n where n.lernender_id = v.lernender_id and n.testsitzung_id is null and n.id <> v.id
                   and (n.am, n.id) > (v.am, v.id) and not (n.aufgabe_id = v.aufgabe_id and n.anlauf = 2)) then 'falsch' -- weitergegangen: endgültig
    else 'offen' end;
$function$;

create or replace function schule.versuch_buchen(v schule.versuch)
 returns void
 language plpgsql
 set search_path to ''
as $function$
begin
  if v.wertung_fest = 'neutral' and not v.richtig then return; end if; -- I-3: 2. Anlauf nach endgültigem Fehler bucht nichts (Aufrufer gibt die Wertung im Datensatz mit)
  if coalesce(v.misch, false) then perform schule.misch_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, now());
  else perform schule.karte_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, now()); end if;
  perform schule.expedition_buchen(v.lernender_id, v.aufgabe_id, v.richtig, v.hilfe, v.anlauf, now()); -- prüft selbst den Pool
end $function$;

-- ---------- H2-2/H2-5: offene erste Anläufe genau einmal entscheiden ----------
create or replace function schule.offene_entscheiden(p_l bigint, p_ausser bigint default null)
 returns integer
 language plpgsql
 set search_path to ''
as $function$
declare o schule.versuch; w text; n_gebucht int := 0;
begin
  for o in with beansprucht as (
             update schule.versuch x set wertung_offen = false
              where x.id in (select y.id from schule.versuch y where y.lernender_id = p_l and y.wertung_offen and y.id is distinct from p_ausser
                               and schule.versuch_wertung(y) <> 'offen' for update skip locked)
                and x.wertung_offen
             returning x.*)
           select * from beansprucht order by am, id loop
    w := schule.versuch_wertung(o);
    update schule.versuch set wertung_fest = w where id = o.id;
    o.wertung_fest := w;
    if w = 'falsch' then perform schule.versuch_buchen(o); n_gebucht := n_gebucht + 1; end if;
  end loop;
  return n_gebucht;
end $function$;
comment on function schule.offene_entscheiden(bigint, bigint) is 'I-3/H2: offene erste Anläufe eines Kindes beanspruchen (einmal) und entscheiden; Rückgabe: Zahl der nachgebuchten Fehler';

create or replace function schule.versuch_karte()
 returns trigger
 language plpgsql
 set search_path to ''
as $function$
declare w text; v_neu schule.versuch;
begin
  if new.testsitzung_id is not null then return new; end if;
  perform schule.offene_entscheiden(new.lernender_id, new.id); -- I-2/H2, seit I-3 mit Beanspruchen
  w := schule.versuch_wertung(new);
  if w = 'offen' then
    update schule.versuch set wertung_offen = true where id = new.id;
  else
    update schule.versuch set wertung_fest = w where id = new.id;
    v_neu := new; v_neu.wertung_fest := w;
    perform schule.versuch_buchen(v_neu);
  end if;
  return new;
end $function$;

-- ---------- H10-3/H10-4: Ausgaben eindeutig, an die Lage gebunden, atomar eingelöst ----------
alter table schule.misch_ausgabe add column if not exists einheit_id bigint references schule.einheit(id);
alter table schule.misch_ausgabe add column if not exists lernziel text;
comment on column schule.misch_ausgabe.einheit_id is 'I-3/H10: Flug, der beim Ausliefern gelesen wurde (Lage); null = Ausgabe aus 0.81.1';
comment on column schule.misch_ausgabe.lernziel is 'I-3/H10: erste noch nicht gelandete Etappe dieses Flugs beim Ausliefern';
do $mig$
declare n_doppelt int;
begin
  select count(*) into n_doppelt from (select 1 from schule.misch_ausgabe where eingeloest_am is null group by lernender_id, aufgabe_id having count(*) > 1) q;
  if n_doppelt > 0 then raise exception 'misch_ausgabe: % offene Dopplungen im Bestand – eindeutiger Index nicht angelegt, bitte melden', n_doppelt; end if;
end $mig$;
create unique index if not exists misch_ausgabe_offen_eindeutig on schule.misch_ausgabe (lernender_id, aufgabe_id) where eingeloest_am is null;

create or replace function schule.mischkarten(p_lernender bigint, p_einheit bigint, p_anzahl integer default 8)
 returns jsonb
 language plpgsql
 set search_path to ''
as $function$
declare v_j jsonb; v_ids bigint[]; v_lz text;
begin
  v_j := schule.mischkarten_waehlen(p_lernender, p_einheit, p_anzahl);
  select coalesce(array_agg((x->>'id')::bigint), '{}') into v_ids from jsonb_array_elements(v_j) x;
  -- I-3/H10: Lage = gelesener Flug und seine erste noch nicht gelandete Etappe
  select et.x->>'lernziel' into v_lz from schule.einheit e, jsonb_array_elements(coalesce(e.inhalt->'etappen', '[]'::jsonb)) with ordinality et(x, nr)
   where e.id = p_einheit and not exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = e.id and k.lernziel = et.x->>'lernziel' and k.sitzt)
   order by et.nr limit 1;
  insert into schule.misch_ausgabe(lernender_id, aufgabe_id, einheit_id, lernziel)
  select p_lernender, u.id, p_einheit, v_lz from unnest(v_ids) u(id)
  on conflict (lernender_id, aufgabe_id) where eingeloest_am is null
  do update set ausgegeben_am = now(), einheit_id = excluded.einheit_id, lernziel = excluded.lernziel;
  return v_j;
end $function$;

create or replace function schule.misch_gueltig(p_lernender bigint, a schule.aufgabe, p jsonb)
 returns boolean
 language sql
 stable
 set search_path to ''
as $function$
  select coalesce(coalesce((p->>'misch')::boolean, false) and a.pool = 'uebung' and a.stufe in (2, 3) and a.freigegeben
     and exists (select 1 from schule.karte_stand k where k.lernender_id = p_lernender and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt)
     and exists (select 1 from schule.misch_ausgabe m where m.lernender_id = p_lernender and m.aufgabe_id = a.id and m.eingeloest_am is null
                   and m.ausgegeben_am >= now() - interval '24 hours'
                   and case when m.einheit_id is not null
                            then not (m.einheit_id = a.einheit_id and m.lernziel is not distinct from a.variante_gruppe) -- I-3: gespeicherte Lage
                            else nullif(p->>'aktuell_einheit', '') is not null and nullif(p->>'aktuell_lernziel', '') is not null
                                 and not ((p->>'aktuell_einheit')::bigint = a.einheit_id and p->>'aktuell_lernziel' = a.variante_gruppe) end), false); -- Ausgabe aus 0.81.1
$function$;

create or replace function schule.misch_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe; v_mid bigint;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if;
  -- I-3/H10: einlösen; nur wenn das eine offene Ausgabe trifft, gibt es eine Mischkarten-Buchung – sonst normale Buchung als Übung
  update schule.misch_ausgabe set eingeloest_am = p_zeit
   where id = (select m.id from schule.misch_ausgabe m where m.lernender_id = p_l and m.aufgabe_id = p_aufgabe and m.eingeloest_am is null
                order by m.ausgegeben_am limit 1 for update skip locked) and eingeloest_am is null
  returning id into v_mid;
  if v_mid is null or not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt) then
    perform schule.karte_buchen(p_l, p_aufgabe, p_richtig, p_hilfe, p_zeit); return;
  end if;
  if p_richtig then
    if coalesce(p_hilfe, 0) = 0 then
      update schule.karte_stand set misch_ok_am = p_zeit, richtig = richtig + 1, zuletzt = p_zeit
       where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    end if; -- Tipp oder 2. Versuch: kein Beleg, nichts fällig
  else
    update schule.karte_stand set falsch = falsch + 1 where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    perform schule.karte_faellig_machen(p_l, a.einheit_id, a.variante_gruppe, p_zeit); -- H8: nur fällig, nie wieder öffnen
  end if;
end $function$;

-- ---------- H2-5: auch beim Lesen des Flugs und beim Teststart entscheiden ----------
do $mig$
declare d text;
begin
  d := pg_get_functiondef('schule.einheit_lesen_intern(bigint, bigint)'::regprocedure);
  if position('offene_entscheiden' in d) = 0 then
    if position('  perform schule.lernziele_anlegen(p_lernender, p_einheit);' in d) = 0 then raise exception 'einheit_lesen_intern: Stelle nicht gefunden'; end if;
    d := replace(d, '  perform schule.lernziele_anlegen(p_lernender, p_einheit);',
                    '  perform schule.lernziele_anlegen(p_lernender, p_einheit);
  perform schule.offene_entscheiden(p_lernender); -- I-3/H2: offene erste Anläufe über 30 Minuten entscheiden');
    execute d;
  end if;
  d := pg_get_functiondef('schule.test_starten_intern(bigint, jsonb)'::regprocedure);
  if position('offene_entscheiden' in d) = 0 then
    if position('  perform schule.lernziele_anlegen(p_lernender, v_einheit);' in d) = 0 then raise exception 'test_starten_intern: Stelle nicht gefunden'; end if;
    d := replace(d, '  perform schule.lernziele_anlegen(p_lernender, v_einheit);',
                    '  perform schule.lernziele_anlegen(p_lernender, v_einheit);
  perform schule.offene_entscheiden(p_lernender); -- I-3/H2: offene erste Anläufe über 30 Minuten entscheiden');
    execute d;
  end if;
end $mig$;
