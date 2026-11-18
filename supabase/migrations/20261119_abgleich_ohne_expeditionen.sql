-- Fehler aus dem Haupt-Chat (Postfach 18.11. 11:20): schule.einheit_abgleichen(…, 'sperren') sperrte auch Expeditions-Teile (pool = 'expedition') des Flugs,
-- weil sie nicht in der Themendatei stehen (am 18.11. 21 Teile in 14 Expeditionen; durch erneuten Import behoben).
-- Ab jetzt lässt der Abgleich Aufgaben mit pool = 'expedition' ganz unberührt: nicht ändern, nicht als „nicht mehr in der Datei“ zählen, nicht sperren, nicht löschen.
-- Expeditions-Teile pflegt nur schule.expedition_importieren. Sonst unverändert.
-- Nicht ausgeführt – der Haupt-Chat spielt ein. Kein DROP, kein DELETE (die vorhandene Lösch-Option für Entwürfe bleibt, trifft aber keine Expeditions-Teile mehr).

do $$
declare d text; n int;
begin
  d := pg_get_functiondef('schule.einheit_abgleichen(jsonb, text)'::regprocedure);
  n := (length(d) - length(replace(d, 'b.einheit_id = v_e', ''))) / length('b.einheit_id = v_e');
  -- fünf Stellen: Änderungen übernehmen, „schon vorhanden?“, Zählen, Sperren, Löschen
  if n <> 5 then raise exception 'einheit_abgleichen: 5 Stellen „b.einheit_id = v_e“ erwartet, gefunden %', n; end if;
  if position('pool is distinct from ''expedition''' in d) > 0 then raise exception 'einheit_abgleichen ist schon angepasst'; end if;
  d := replace(d, 'b.einheit_id = v_e', 'b.einheit_id = v_e and b.pool is distinct from ''expedition''');
  execute d;
end $$;

comment on function schule.einheit_abgleichen(jsonb, text) is 'Themendatei abgleichen (lassen/sperren/loeschen für Aufgaben, die nicht mehr in der Datei stehen); Expeditions-Teile (pool = expedition) bleiben unberührt';
