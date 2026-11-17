-- W150 Inhalte „Lücken laut Lehrplan“ (Entscheidung Sebastian 17.11.): drei fehlende Gymnasium-Flüge bekommen ihre Themen-Einträge, damit die Inhalts-Chats feste Nummern haben.
--  * Klasse 6: Flächen von Parallelogramm, Dreieck und Trapez (LehrplanPLUS M6 2.1) und Volumen (M6 2.2).
--    Im Kontinent „Fläche und Raum“ gibt es keinen Ort der Klasse 6 (Regel seit D2: ein Ort = eine Klasse) → neuer Ort Quito.
--  * Klasse 8: Prismen und Zylinder (M8 7) → Cusco (Klasse 8, „Körper und Netze“).
-- Die Einheiten werden später als Entwurf importiert; bis dahin ist Quito ein Ort ohne Inhalt.
do $$
declare v_b bigint; v_t bigint;
begin
  select id into v_b from schule.block where stadt = 'Quito' and fach = 'Mathematik';
  if v_b is null then
    insert into schule.block (fach, schluessel, titel, ziel_klasse, ziel_begruendung, module, reihenfolge, kontinent_id, stadt, land, lat, lon)
    select 'Mathematik', 'r7', 'Flächen und Volumen', 6, 'LehrplanPLUS Gymnasium M6 2.1 und M6 2.2 (Lücken-Prüfung 14.11., Entscheidung 17.11.)', '{}'::text[], 607, b.kontinent_id, 'Quito', 'Ecuador', -0.18, -78.47
      from schule.block b where b.stadt = 'Lima' returning id into v_b;
  end if;
  if not exists (select 1 from schule.thema where schluessel = 'messen.flaechen_vielecke') then
    insert into schule.thema (fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest)
    values ('Mathematik', 'messen.flaechen_vielecke', 'Flächen & Körper', 'Flächen von Parallelogramm, Dreieck und Trapez',
            'Flächeninhalt von Parallelogramm, Dreieck und Trapez durch Zerlegen und Ergänzen; zusammengesetzte Figuren; Oberfläche einfacher Körper.', 2, 'ungeprueft', '{"gym_by": 6}') returning id into v_t;
    insert into schule.block_thema (block_id, thema_id, reihenfolge) values (v_b, v_t, 1);
  end if;
  if not exists (select 1 from schule.thema where schluessel = 'messen.volumen') then
    insert into schule.thema (fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest)
    values ('Mathematik', 'messen.volumen', 'Flächen & Körper', 'Volumen',
            'Einheitswürfel, Volumen des Quaders, Volumeneinheiten mit Liter und Milliliter umrechnen, zusammengesetzte Körper.', 5, 'ungeprueft', '{"gym_by": 6}') returning id into v_t;
    insert into schule.block_thema (block_id, thema_id, reihenfolge) values (v_b, v_t, 2);
  end if;
  if not exists (select 1 from schule.thema where schluessel = 'messen.prisma_zylinder') then
    insert into schule.thema (fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest)
    values ('Mathematik', 'messen.prisma_zylinder', 'Flächen & Körper', 'Prismen und Zylinder',
            'Volumen und Oberfläche gerader Prismen und Zylinder (V = G · h) mit Begründung; Sachaufgaben.', 6, 'ungeprueft', '{"gym_by": 8}') returning id into v_t;
    insert into schule.block_thema (block_id, thema_id, reihenfolge) values ((select id from schule.block where stadt = 'Cusco'), v_t, 2);
  end if;
end $$;
