-- Potenz 1 (Sechsundzwanzigste bis Neunundzwanzigste Runde, 21.11.): zwei neue Flüge als Themen anlegen und ihren Orten zuordnen.
-- terme.potenzgesetze_natuerlich (102, Samarkand) und terme.potenzgesetze_ganzzahlig (103, Mumbai). Erzeugt vom Haupt-Chat aus inhalte/themenliste.json und inhalte/kann/.
-- Kein DROP, kein DELETE. Wiederholt ausführbar. Die Inhalte (Einheiten als Entwurf) spielt der Haupt-Chat danach mit schule.einheit_importieren ein.
do $$
declare v_a bigint; v_b bigint;
begin
  select id into v_a from schule.thema where schluessel = 'terme.potenzgesetze_natuerlich';
  if v_a is null then
    insert into schule.thema (id, fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest, lehrplan_reihenfolge, lernbereich, lehrplan, kurz)
    overriding system value values (102, 'Mathematik', 'terme.potenzgesetze_natuerlich', 'Terme & Potenzen', 'Potenzgesetze',
            'Potenzen mit natürlichen Exponenten zusammenfassen: bei gleicher Basis malnehmen und teilen, bei gleichem Exponenten die Basen zusammenfassen, Potenzen von Potenzen vereinfachen, die Gesetze geschickt nutzen.', 2, 'ungeprueft', '{"gym_by": 7, "rs_by": 7, "ib_myp": 3}'::jsonb, '{"gym_by": 2, "rs_by": 2, "ib_myp": 2}'::jsonb,
            '{"gym_by": "M7 1 Terme mit Variablen", "rs_by": "M7 1 Potenzen", "ib_myp": "MYP 3 Numerical and abstract reasoning (Zahl und Algebra)"}'::jsonb,
            '{"gym_by": "M7 1.2 Produkte von Potenzen mit natürlichen Exponenten bei gleicher Basis oder gleichem Exponenten zusammenfassen · M7 1.2 Potenzen von Potenzen mit natürlichen Exponenten zusammenfassen", "rs_by": "Potenzgesetze anwenden, zuerst mit natürlichen Exponenten (Aufteilung auf zwei Flüge: Annahme)", "ib_myp": "Annahme: MYP 3 wie im Gymnasium vor terme.umformen, das die Gesetze benutzt; im Framework stehen Potenzgesetze unter MYP 4–5 Standard"}'::jsonb,
            'Du lernst, Potenzen mit gleicher Basis oder gleichem Exponenten geschickt zusammenzufassen.') returning id into v_a;
  end if;
  if v_a <> 102 then raise exception 'erwartet thema_id 102, bekommen %', v_a; end if;
  insert into schule.etappe_text (thema_id, lernziel, kann) values (102, 'mal_gleiche_basis', 'bei gleicher Basis Potenzen malnehmen, indem du die Exponenten addierst') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (102, 'gleicher_exponent', 'bei gleichem Exponenten die Basen zusammenfassen und so geschickt rechnen') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (102, 'potenz_von_potenz', 'eine Potenz einer Potenz wie (2³)⁴ vereinfachen, indem du die Exponenten malnimmst') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (102, 'geteilt_gleiche_basis', 'bei gleicher Basis Potenzen teilen, indem du die Exponenten subtrahierst') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (102, 'anwenden', 'erkennen, welches Potenzgesetz passt, und Zahlen dafür als Potenz schreiben') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  select id into v_b from schule.thema where schluessel = 'terme.potenzgesetze_ganzzahlig';
  if v_b is null then
    insert into schule.thema (id, fach, schluessel, block, unterthema, beschreibung, reihenfolge, pruefstatus, klasse_fest, lehrplan_reihenfolge, lernbereich, lehrplan, kurz)
    overriding system value values (103, 'Mathematik', 'terme.potenzgesetze_ganzzahlig', 'Terme & Potenzen', 'Potenzgesetze mit ganzzahligen Exponenten',
            'Potenzgesetze für ganzzahlige Exponenten plausibel machen und anwenden: gleiche Basis malnehmen und teilen, gleicher Exponent, Potenz einer Potenz, Terme mit Variablen vereinfachen und als Bruch schreiben.', 4, 'ungeprueft', '{"gym_by": 8, "rs_by": 7, "ib_myp": 4}'::jsonb, '{"gym_by": 8, "rs_by": 3, "ib_myp": 1}'::jsonb,
            '{"gym_by": "M8 4 Bruchterme und Bruchgleichungen", "rs_by": "M7 1 Potenzen", "ib_myp": "MYP 4 Numerical and abstract reasoning (Zahl und Algebra)"}'::jsonb,
            '{"gym_by": "M8 4 Rechengesetze für Potenzen mit ganzzahligen Exponenten plausibel machen und in einfachen Fällen anwenden", "rs_by": "Potenzen mit negativen ganzzahligen Exponenten; Potenzgesetze auch mit negativen Exponenten anwenden", "ib_myp": "MYP 4–5 Standard: Potenzgesetze mit ganzzahligen und negativen Exponenten"}'::jsonb,
            'Du lernst, warum die Regeln für Potenzen auch mit negativen Hochzahlen gelten, und rechnest damit.') returning id into v_b;
  end if;
  if v_b <> 103 then raise exception 'erwartet thema_id 103, bekommen %', v_b; end if;
  insert into schule.etappe_text (thema_id, lernziel, kann) values (103, 'warum_gilt', 'mit Zahlenproben zeigen, dass die Potenzgesetze auch für negative Exponenten gelten') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (103, 'gleiche_basis_ganz', 'Potenzen mit gleicher Basis malnehmen und teilen, auch mit negativen Exponenten') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (103, 'exponent_und_potenz', 'Potenzen mit gleichem Exponenten zusammenfassen und Potenzen von Potenzen vereinfachen') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (103, 'terme_vereinfachen', 'Terme wie 6x³ · x⁻⁵ vereinfachen und ohne negativen Exponenten als Bruch schreiben') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  insert into schule.etappe_text (thema_id, lernziel, kann) values (103, 'fehler_ganz', 'Fehler mit negativen Exponenten finden und mit einer Zahlenprobe prüfen') on conflict (thema_id, lernziel) do update set kann = excluded.kann, geaendert_am = now();
  perform setval(pg_get_serial_sequence('schule.thema', 'id'), (select max(id) from schule.thema)); -- feste IDs 102/103, Zähler nachziehen
  -- Samarkand (62): Flug A vor terme.umformen (Reihenfolge 1)
  insert into schule.block_thema (block_id, thema_id, reihenfolge) values (62, 102, 0) on conflict (block_id, thema_id) do nothing;
  -- Mumbai (60): Flug B hinter terme.bruchterme (1), vor gleichungen.bruch
  if not exists (select 1 from schule.block_thema where block_id = 60 and thema_id = 103) then
    if (select array_agg(thema_id order by reihenfolge) from schule.block_thema where block_id = 60) <> array[31, 5, 4]::bigint[] then raise exception 'Mumbai: unerwartete Flüge'; end if;
    update schule.block_thema set reihenfolge = 4 where block_id = 60 and thema_id = 4;
    update schule.block_thema set reihenfolge = 3 where block_id = 60 and thema_id = 5;
    insert into schule.block_thema (block_id, thema_id, reihenfolge) values (60, 103, 2);
  end if;
end $$;
