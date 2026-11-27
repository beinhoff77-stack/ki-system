-- W150 Umbau D2-Folge (Entscheidung des Nutzers 16.11.): neuer Flug „Winkelsätze“ (Gymnasium Klasse 7, LehrplanPLUS M7 2.2) in Addis Abeba.
-- Nur der Themen-Eintrag; die Einheit wird als Entwurf importiert und erst nach Freigabe des Nutzers für Kinder sichtbar.
do $$
declare v_id bigint;
begin
  if exists (select 1 from schule.thema where schluessel = 'geometrie.winkelsaetze') then return; end if;
  insert into schule.thema (fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest)
  values ('Mathematik', 'geometrie.winkelsaetze', 'Ebene Geometrie', 'Winkelsätze',
          'Scheitel-, Neben-, Stufen- und Wechselwinkel; Winkelsumme im Dreieck und Vieleck; Außenwinkel; Winkel in Figuren begründen.', 3, 'ungeprueft', '{"gym_by": 7}'::jsonb)
  returning id into v_id;
  if v_id <> 98 then raise exception 'Thema bekam id % statt 98 – Themendatei erwartet 98', v_id; end if;
end $$;
