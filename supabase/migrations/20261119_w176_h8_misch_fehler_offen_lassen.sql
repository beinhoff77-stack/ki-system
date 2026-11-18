-- Bau-Auftrag H, H8 (Werkstatt-Wunsch 176): Ein Fehler in einer Mischkarte oder Expedition darf eine gelandete Etappe nie wieder öffnen.
-- Vorher: schule.misch_buchen und schule.expedition_buchen gaben einen endgültigen Fehler an schule.karte_buchen(…, false, …) weiter; dort setzt der zweite Fehler (wdh_fehler ≥ 1) sitzt = false.
-- Jetzt: eigener Fehlerweg schule.karte_faellig_machen – die Etappe ist am nächsten Lerntag zur Wiederholung fällig; sitzt, wdh_stufe, wdh_fehler und alle Belege bleiben unverändert –
-- auch beim zweiten und dritten Fehler und auch, wenn wdh_fehler schon 1 ist. Ist die Etappe schon fällig, bleibt der frühere Termin. Wieder öffnen kann allein die fällige Wiederholung.
-- Stand vor dem Einspielen (gelesen 18.11.): 0 Mischkarten-Versuche, 0 Expeditionen, 0 Expeditions-Versuche; 34 von 36 Karten-Ständen gelandet → nichts zu reparieren.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE. Sofort einspielbar (setzt W176 Teil 3 und 4 voraus, die live sind).

create or replace function schule.karte_faellig_machen(p_l bigint, p_einheit bigint, p_lz text, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare k schule.karte_stand;
begin
  select * into k from schule.karte_stand where lernender_id = p_l and einheit_id = p_einheit and lernziel = p_lz for update;
  if k.lernender_id is null or not k.sitzt then return; end if;
  if schule.karte_faellig(k) then return; end if; -- schon fällig: früheren Termin behalten
  update schule.karte_stand set wdh_ab = p_zeit, wdh_lerntage = 1, faellig_am = p_zeit + interval '1 day', zuletzt = p_zeit
   where lernender_id = p_l and einheit_id = p_einheit and lernziel = p_lz;
end $function$;
comment on function schule.karte_faellig_machen(bigint, bigint, text, timestamp with time zone) is 'W176 H8: Etappe am nächsten Lerntag fällig, ohne sitzt/Belege zu ändern (Fehlerweg für Mischkarten und Expeditionen)';

create or replace function schule.misch_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'uebung' then return; end if;
  if not exists (select 1 from schule.karte_stand k where k.lernender_id = p_l and k.einheit_id = a.einheit_id and k.lernziel = a.variante_gruppe and k.sitzt) then
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

create or replace function schule.expedition_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_anlauf smallint, p_zeit timestamp with time zone)
 returns void
 language plpgsql
 set search_path to ''
as $function$
declare a schule.aufgabe;
begin
  select * into a from schule.aufgabe where id = p_aufgabe;
  if a.id is null or a.pool <> 'expedition' then return; end if;
  if p_richtig then
    if coalesce(p_hilfe, 0) = 0 and coalesce(p_anlauf, 1) = 1 then
      update schule.karte_stand set angewandt_am = p_zeit where lernender_id = p_l and einheit_id = a.einheit_id and lernziel = a.variante_gruppe;
    end if;
  else
    perform schule.karte_faellig_machen(p_l, a.einheit_id, a.variante_gruppe, p_zeit); -- H8: nur fällig, nie wieder öffnen
  end if;
  if not exists (select 1 from schule.aufgabe t where t.expedition_id = a.expedition_id and t.freigegeben and not schule.expedition_teil_erledigt(p_l, t.id)) then
    insert into schule.sterne(lernender_id, menge, grund, bezug)
    values (p_l, schule.sterne_regel('sterne_expedition_geschafft'), 'expedition', 'expedition:' || a.expedition_id)
    on conflict do nothing;
  end if;
end $function$;
