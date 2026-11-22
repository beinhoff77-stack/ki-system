-- WD-S 3, nur lesend (für den Haupt-Chat). Keine Namen, nur Nummern.
-- A) je Kind die gelandeten Etappen mit weniger als 3 frischen Aufgaben der Stufen 2–3 (nach dem Einspielen auch: select * from schule.etappen_wenig_frisch();)
select k.lernender_id, k.einheit_id, k.lernziel,
       (select et->>'titel' from schule.einheit e, jsonb_array_elements(e.inhalt->'etappen') et where e.id = k.einheit_id and et->>'lernziel' = k.lernziel limit 1) etappe,
       count(a.id) filter (where not exists (select 1 from schule.versuch v where v.lernender_id = k.lernender_id and v.aufgabe_id = a.id)) frisch,
       count(a.id) gesamt
  from schule.karte_stand k join schule.lernender l on l.id = k.lernender_id and l.aktiv
  left join schule.aufgabe a on a.einheit_id = k.einheit_id and a.variante_gruppe = k.lernziel and a.pool = 'uebung' and a.freigegeben and a.stufe in (2, 3)
 where k.sitzt
 group by 1, 2, 3
having count(a.id) filter (where not exists (select 1 from schule.versuch v where v.lernender_id = k.lernender_id and v.aufgabe_id = a.id)) < 3
 order by 1, 2, 3;

-- B) Gegenprüfung flug_erstabschluss (ChatGPT 919): jede Zeile passt zu Kind, Flug und Sitzung; Flug heute fertig oder Sitzung mit flug_geschafft
select fe.lernender_id, fe.einheit_id, fe.sitzung_id, fe.am,
       (fe.sitzung_id is null or exists (select 1 from schule.testsitzung t where t.id = fe.sitzung_id and t.lernender_id = fe.lernender_id and t.einheit_id = fe.einheit_id
                                           and t.art in ('blocktest', 'korrektur') and t.status = 'abgeschlossen')) sitzung_passt,
       (select bool_or(t.flug_geschafft) from schule.testsitzung t where t.lernender_id = fe.lernender_id and t.einheit_id = fe.einheit_id) mit_flug_geschafft,
       not exists (select 1 from schule.lernziel_stand s where s.lernender_id = fe.lernender_id and s.einheit_id = fe.einheit_id and s.pflicht
                     and s.status not in ('nachgewiesen', 'korrigiert', 'gesichert')) flug_heute_fertig,
       (select count(*) from schule.testsitzung t where t.lernender_id = fe.lernender_id and t.einheit_id = fe.einheit_id and t.flug_geschafft) sitzungen_geschafft
  from schule.flug_erstabschluss fe order by 1, 2;
-- Auffällig wäre: sitzung_passt = false, sitzungen_geschafft > 1, oder weder flug_heute_fertig noch mit_flug_geschafft.
