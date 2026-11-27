-- W150 Umbau D2, Teil 2 (Entscheidung des Nutzers 16.11.: „A“ und „ja“):
-- „Lineare Gleichungen“ zieht von Delhi nach Samarkand; Delhi wird Klasse 8 („Lineare Ungleichungen“).
-- Wer Samarkand schon abgeschlossen hat, aber den neuen Flug dort noch nicht begonnen hat, bekommt den Ort wieder geöffnet (Sterne bleiben; der Stempel kommt nach dem Flug wieder).
update schule.einheit e set block_id = (select id from schule.block where stadt = 'Samarkand')
  from schule.thema t where t.id = e.thema_id and t.schluessel = 'gleichungen.linear' and e.status <> 'ersetzt';
update schule.block set ziel_klasse = 8, titel = 'Lineare Ungleichungen' where stadt = 'Delhi';
update schule.route r set status = 'offen', revision = r.revision + 1, geaendert_von = 'eltern:Claude (D2 Klassen-Zuordnung 16.11.)', geaendert_am = now()
 where r.block_id = (select id from schule.block where stadt = 'Samarkand') and r.status = 'fertig' and r.art = 'normal';

-- Plan des Kindes der Klasse 8: Cusco („Körper darstellen“, jetzt Klasse 8) ist nicht mehr „kann schon“;
-- Darwin und Brasília (jetzt Klasse 10) rücken hinter die Orte der Klasse 9 (vor die „kann schon“-Orte).
update schule.route r set kann_schon = false, revision = r.revision + 1, geaendert_von = 'eltern:Claude (D2 Klassen-Zuordnung 16.11.)', geaendert_am = now()
 where r.block_id = (select id from schule.block where stadt = 'Cusco') and r.kann_schon and r.status = 'offen'
   and exists (select 1 from schule.lernender l where l.id = r.lernender_id and l.klasse = 8);
update schule.route r set position = r.position + 1000
 where r.art = 'normal' and exists (select 1 from schule.lernender l where l.id = r.lernender_id and l.klasse = 8);
update schule.route r set position = x.neu, geaendert_am = now()
  from (select r2.id, row_number() over (partition by r2.lernender_id order by
            case when r2.status = 'entfernt' then 3 when r2.kann_schon then 2 when b.stadt in ('Darwin', 'Brasília') then 1 else 0 end, r2.position) neu
          from schule.route r2 join schule.block b on b.id = r2.block_id
         where r2.art = 'normal' and exists (select 1 from schule.lernender l where l.id = r2.lernender_id and l.klasse = 8)) x
 where x.id = r.id;
