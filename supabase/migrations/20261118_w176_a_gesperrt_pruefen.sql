-- Fehler aus dem Betrieb (18.11.): Eine Bordkarte wurde gesperrt, während ein Kind sie offen hatte (neue Fassung eingespielt, alte freigegeben = false).
-- Beim „Prüfen“ kam „Diese Aufgabe ist noch nicht freigegeben“, die Antwort wurde nicht gewertet, das Kind hing fest.
-- Regel jetzt: Die Sperre (freigegeben = false) greift nur bei der AUSWAHL neuer Bordkarten (Übung, Wiederholung, Mischkarten, Knobel, Tests). Beim PRÜFEN wird eine gesperrte Bordkarte
-- noch normal gewertet, wenn ihr Flug geprüft oder freigegeben ist. Entwurfs-Flüge bleiben für echte Kinder gesperrt (das prüft api.schule_uebung_pruefen vorher über
-- schule.einheit_pruefen_sichtbar; hier zusätzlich: gesperrte Bordkarte in einem Entwurf nur für das Testkind wie bisher).
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Läuft auf dem heutigen Stand und vor/nach den Migrationen W176 Teil 1/3/4 (Teil 3 fasst diese Stelle nicht mehr an).
-- Kein DROP, kein DELETE.
do $$
declare d text; v_alt text := 'if not a.freigegeben and not exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test) then';
  v_alt2 text := 'if not a.freigegeben then';
  v_neu text := 'if not a.freigegeben and not exists (select 1 from schule.einheit e where e.id = a.einheit_id and e.status in (''geprueft'', ''freigegeben''))
     and not exists (select 1 from schule.lernender l where l.id = p_lernender and l.ist_test) then -- gesperrt nach dem Laden: in geprüften/freigegebenen Flügen trotzdem werten (18.11.)';
begin
  d := pg_get_functiondef('schule.uebung_pruefen_intern(bigint, jsonb)'::regprocedure);
  if position(v_alt in d) > 0 then d := replace(d, v_alt, v_neu);
  elsif position(v_alt2 in d) > 0 then d := replace(d, v_alt2, v_neu);
  elsif position('gesperrt nach dem Laden' in d) > 0 then return; -- schon eingespielt
  else raise exception 'Stelle in uebung_pruefen_intern nicht gefunden';
  end if;
  execute d;
end $$;
