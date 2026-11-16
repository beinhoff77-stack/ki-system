-- W150 Umbau D2, Teil 3: Die Zuordnung Thema ↔ Ort steht zusätzlich in schule.block_thema (genutzt von ort_stand, schule_plan_lesen, schule_lehrplan_uebersicht, einheit_importieren).
-- Die Umzüge aus Teil 1 und 2 hatten nur schule.einheit.block_id geändert. Hier nachgezogen; dazu der neue Flug „Winkelsätze“ in Addis Abeba.
-- Reihenfolge im Ort nach Lehrplan: Paris Zehnerpotenzen vor Potenzgesetzen; Kairo Grundbegriffe vor Ortslinien; Samarkand Terme umformen vor linearen Gleichungen; Addis Abeba Winkelsätze vor Konstruktion.
update schule.block_thema bt set block_id = (select id from schule.block where stadt = 'Paris'), reihenfolge = 0
  where bt.thema_id = (select id from schule.thema where schluessel = 'zahlen.potenzen_zehner');
update schule.block_thema bt set block_id = (select id from schule.block where stadt = 'Kairo'), reihenfolge = 9
  where bt.thema_id = (select id from schule.thema where schluessel = 'geometrie.ortslinien');
update schule.block_thema bt set block_id = (select id from schule.block where stadt = 'Samarkand'), reihenfolge = 9
  where bt.thema_id = (select id from schule.thema where schluessel = 'gleichungen.linear');
insert into schule.block_thema (block_id, thema_id, reihenfolge)
select (select id from schule.block where stadt = 'Addis Abeba'), t.id, 0 from schule.thema t
 where t.schluessel = 'geometrie.winkelsaetze' and not exists (select 1 from schule.block_thema x where x.thema_id = t.id);
