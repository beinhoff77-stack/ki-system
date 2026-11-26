-- BD-S1 (Fundament, Schritt 2, Teil 1 von 2): Antworttyp „bedingung“ – Rechner und Bewertung.
-- Aufgaben mit vielen richtigen Antworten: mehrere Zahlenfelder, Bedingungen als Datenbaum (feste Rechensprache, kein SQL aus Inhalten).
-- Referenz: tools/bedingung.py; beide Fassungen müssen für tools/tests/bedingung_faelle.json und den Zufallslauf
-- (tools/tests/bedingung_sql_test.py) dasselbe liefern. Format und Grenzen: inhalte/plan/bedingung-format.md.
--
-- Dieser Teil ist ohne Wirkung, solange es keine Aufgabe des Typs gibt: Der Constraint aufgabe_antworttyp_check wird
-- hier NICHT erweitert. Das geschieht erst in Teil 2 (BD-S2), zusammen mit dem Schutz der Prüf-Bäume in allen Ausgaben.
-- Nur neue Funktionen und ein Zweig in schule.antwort_bewerten (Text-Patch, Anker geprüft). Keine Tabelle, kein DROP, kein DELETE.
-- Wiederholbar. Alle Funktionen rechnen rein (IMMUTABLE, kein Tabellenzugriff).
--
-- Zahl      = {"z": Zähler, "n": Nenner}, gekürzt, Nenner > 0.   Wahrheitswert = true/false.   Liste = [Zahl, …]
-- SQLSTATE BG001: Rechnung nicht definiert  -> die Bedingung gilt als verletzt.
-- SQLSTATE BG002: Zwischenwert zu groß      -> die Eingabe wird abgewiesen (format_ok false), nichts wird gewertet.

create or replace function schule.bed_bruch(p_z numeric, p_n numeric)
 returns jsonb language plpgsql immutable set search_path to ''
as $$
declare z numeric := p_z; n numeric := p_n; g numeric;
begin
  if n = 0 then raise exception 'nicht definiert' using errcode = 'BG001'; end if;
  if n < 0 then z := -z; n := -n; end if;
  g := gcd(abs(z), n);
  z := div(z, g); n := div(n, g);
  if abs(z) > 1e30 or n > 1e30 then raise exception 'zu gross' using errcode = 'BG002'; end if;
  return jsonb_build_object('z', z, 'n', n);
end $$;

create or replace function schule.bed_z(p jsonb)
 returns numeric language plpgsql immutable set search_path to ''
as $$
begin
  if jsonb_typeof(p) is distinct from 'object' then raise exception 'bedingung: Zahl erwartet'; end if;
  return (p->>'z')::numeric;
end $$;

create or replace function schule.bed_putzen(p text)
 returns text language sql immutable set search_path to ''
as $$ select replace(replace(regexp_replace(p, E'[ \\t\\n\\r\\f\\v\u00a0\u202f]', '', 'g'), '−', '-'), '–', '-') $$;

-- Liest ein Antwortfeld oder eine Konstante. null = Format falsch.
create or replace function schule.bed_lesen(p_roh text, p_art text)
 returns jsonb language plpgsql immutable set search_path to ''
as $$
declare s text; m text[];
begin
  if p_roh is null or length(p_roh) > 40 then return null; end if;   -- 40: Obergrenze der rohen Eingabe, vor dem Putzen
  s := schule.bed_putzen(p_roh);
  if length(s) > 14 then return null; end if;
  -- genau ein freiwilliges Vorzeichen: „+3“ und „-3“ gelten, „+-3“ nicht
  if s ~ '^[+-]?[0-9]{1,6}$' then return jsonb_build_object('z', s::numeric, 'n', 1); end if;
  if p_art is distinct from 'rational' then return null; end if;
  if s ~ '^[+-]?[0-9]{1,6}(,[0-9]{1,3})?$' then
    return schule.bed_bruch(replace(s, ',', '')::numeric, ('1' || repeat('0', length(split_part(s, ',', 2))))::numeric);
  end if;
  m := regexp_match(s, '^([+-]?[0-9]{1,6})/([0-9]{1,6})$');
  if m is not null and m[2]::numeric <> 0 then return schule.bed_bruch(m[1]::numeric, m[2]::numeric); end if;
  return null;
end $$;

-- Zahl für den Hinweis: Minuszeichen, Dezimalkomma, sonst Bruch.
create or replace function schule.bed_deutsch(p jsonb)
 returns text language plpgsql immutable set search_path to ''
as $$
declare z numeric; n numeric; t numeric; s text;
begin
  if jsonb_typeof(p) = 'boolean' then return case when p::boolean then 'ja' else 'nein' end; end if;
  z := schule.bed_z(p); n := (p->>'n')::numeric;
  if n = 1 then s := abs(z)::text;
  elsif mod(1000::numeric, n) = 0 then
    t := abs(z) * div(1000::numeric, n);
    s := rtrim(div(t, 1000)::text || ',' || lpad(mod(t, 1000)::text, 3, '0'), '0');
  else s := abs(z)::text || '/' || n::text;
  end if;
  return case when z < 0 then '−' else '' end || s;
end $$;

-- Rechnet einen Baum mit den Feldwerten aus (p_werte = Liste von Zahlen).
create or replace function schule.bed_wert(p_baum jsonb, p_werte jsonb)
 returns jsonb language plpgsql immutable set search_path to ''
as $$
declare t text := jsonb_typeof(p_baum); op text; s text; r jsonb; x jsonb; a jsonb[] := '{}';
  i int; j int; k int; c int; z numeric; n numeric; z1 numeric; n1 numeric; z2 numeric; n2 numeric;
  zs numeric[] := '{}'; ns numeric[] := '{}'; b boolean;
begin
  if t = 'number' then
    z := (p_baum#>>'{}')::numeric;
    if z <> trunc(z) then raise exception 'bedingung: nur ganze Zahlen als Konstante'; end if;
    return jsonb_build_object('z', trunc(z), 'n', 1);
  elsif t = 'string' then
    s := p_baum#>>'{}';
    if s = '$alle' then return p_werte; end if;
    if s ~ '^\$[1-6]$' then
      r := p_werte->(substr(s, 2)::int - 1);
      if r is null then raise exception 'bedingung: Feld % gibt es nicht', s; end if;
      return r;
    end if;
    r := schule.bed_lesen(s, 'rational');
    if r is null then raise exception 'bedingung: Konstante nicht lesbar'; end if;
    return r;
  elsif t is distinct from 'array' or jsonb_array_length(p_baum) < 2 or jsonb_typeof(p_baum->0) <> 'string' then
    raise exception 'bedingung: Baum nicht erlaubt';
  end if;
  op := p_baum->>0;
  c := jsonb_array_length(p_baum) - 1;
  if c > 6 then raise exception 'bedingung: zu viele Argumente'; end if;
  for i in 1 .. c loop a := array_append(a, schule.bed_wert(p_baum->i, p_werte)); end loop;

  -- Operationen mit genau einer Liste
  if op in ('summe','produkt','min','max','median','mittelwert','anzahl','anzahl_positiv','anzahl_negativ','verschieden') then
    if c <> 1 or jsonb_typeof(a[1]) <> 'array' or jsonb_array_length(a[1]) = 0 then raise exception 'bedingung: Liste erwartet'; end if;
    k := jsonb_array_length(a[1]);
    for i in 1 .. k loop zs[i] := schule.bed_z(a[1]->(i - 1)); ns[i] := (a[1]->(i - 1)->>'n')::numeric; end loop;
    if op in ('summe', 'mittelwert') then
      z := 0; n := 1;
      for i in 1 .. k loop z := z * ns[i] + zs[i] * n; n := n * ns[i]; end loop;
      return schule.bed_bruch(z, case when op = 'summe' then n else n * k end);
    elsif op = 'produkt' then
      r := jsonb_build_object('z', 1, 'n', 1);
      for i in 1 .. k loop r := schule.bed_bruch((r->>'z')::numeric * zs[i], (r->>'n')::numeric * ns[i]); end loop;
      return r;
    elsif op in ('min', 'max') then
      j := 1;
      for i in 2 .. k loop
        if (op = 'min' and zs[i] * ns[j] < zs[j] * ns[i]) or (op = 'max' and zs[i] * ns[j] > zs[j] * ns[i]) then j := i; end if;
      end loop;
      return jsonb_build_object('z', zs[j], 'n', ns[j]);
    elsif op = 'median' then
      for i in 1 .. k - 1 loop
        for j in 1 .. k - i loop
          if zs[j] * ns[j + 1] > zs[j + 1] * ns[j] then
            z := zs[j]; n := ns[j]; zs[j] := zs[j + 1]; ns[j] := ns[j + 1]; zs[j + 1] := z; ns[j + 1] := n;
          end if;
        end loop;
      end loop;
      if k % 2 = 1 then return jsonb_build_object('z', zs[k / 2 + 1], 'n', ns[k / 2 + 1]); end if;
      i := k / 2;
      return schule.bed_bruch(zs[i] * ns[i + 1] + zs[i + 1] * ns[i], 2 * ns[i] * ns[i + 1]);
    elsif op = 'anzahl' then return jsonb_build_object('z', k, 'n', 1);
    elsif op = 'anzahl_positiv' then return jsonb_build_object('z', (select count(*) from unnest(zs) q where q > 0), 'n', 1);
    elsif op = 'anzahl_negativ' then return jsonb_build_object('z', (select count(*) from unnest(zs) q where q < 0), 'n', 1);
    else
      for i in 1 .. k - 1 loop
        for j in i + 1 .. k loop
          if zs[i] = zs[j] and ns[i] = ns[j] then return to_jsonb(false); end if;
        end loop;
      end loop;
      return to_jsonb(true);
    end if;
  end if;

  if op = 'liste' then
    for i in 1 .. c loop perform schule.bed_z(a[i]); end loop;
    return to_jsonb(a);
  elsif op in ('und', 'oder') then
    if c < 2 then raise exception 'bedingung: % braucht mindestens zwei Argumente', op; end if;
    b := (op = 'und');
    for i in 1 .. c loop
      if jsonb_typeof(a[i]) <> 'boolean' then raise exception 'bedingung: Wahrheitswert erwartet'; end if;
      if op = 'und' then b := b and a[i]::boolean; else b := b or a[i]::boolean; end if;
    end loop;
    return to_jsonb(b);
  elsif op = 'nicht' then
    if c <> 1 or jsonb_typeof(a[1]) <> 'boolean' then raise exception 'bedingung: Wahrheitswert erwartet'; end if;
    return to_jsonb(not a[1]::boolean);
  elsif op = '+' then
    if c < 2 then raise exception 'bedingung: + braucht mindestens zwei Argumente'; end if;
    z := 0; n := 1;
    for i in 1 .. c loop z1 := schule.bed_z(a[i]); n1 := (a[i]->>'n')::numeric; z := z * n1 + z1 * n; n := n * n1; end loop;
    return schule.bed_bruch(z, n);
  elsif op = '*' then
    if c < 2 then raise exception 'bedingung: * braucht mindestens zwei Argumente'; end if;
    r := jsonb_build_object('z', 1, 'n', 1);
    for i in 1 .. c loop r := schule.bed_bruch((r->>'z')::numeric * schule.bed_z(a[i]), (r->>'n')::numeric * (a[i]->>'n')::numeric); end loop;
    return r;
  end if;

  z1 := schule.bed_z(a[1]); n1 := (a[1]->>'n')::numeric;
  if op in ('neg', 'betrag', 'ganzzahlig') then
    if c <> 1 then raise exception 'bedingung: % braucht ein Argument', op; end if;
    if op = 'neg' then return jsonb_build_object('z', -z1, 'n', n1);
    elsif op = 'betrag' then return jsonb_build_object('z', abs(z1), 'n', n1);
    else return to_jsonb(n1 = 1);
    end if;
  end if;
  if c <> 2 then raise exception 'bedingung: % nicht erlaubt oder falsche Zahl von Argumenten', op; end if;
  z2 := schule.bed_z(a[2]); n2 := (a[2]->>'n')::numeric;
  case op
    when '-' then return schule.bed_bruch(z1 * n2 - z2 * n1, n1 * n2);
    when '/' then
      if z2 = 0 then raise exception 'nicht definiert' using errcode = 'BG001'; end if;
      return schule.bed_bruch(z1 * n2, n1 * z2);
    when 'hoch' then
      if n2 <> 1 or abs(z2) > 6 then raise exception 'Exponent nicht erlaubt' using errcode = 'BG001'; end if;
      if z2 < 0 and z1 = 0 then raise exception 'nicht definiert' using errcode = 'BG001'; end if;
      z := 1; n := 1;
      for i in 1 .. abs(z2)::int loop z := z * z1; n := n * n1; end loop;
      if z2 >= 0 then return schule.bed_bruch(z, n); else return schule.bed_bruch(n, z); end if;
    when 'teilbar' then
      if n1 <> 1 or n2 <> 1 or z2 = 0 then raise exception 'Teilbarkeit nicht definiert' using errcode = 'BG001'; end if;
      return to_jsonb(mod(z1, z2) = 0);
    when '='  then return to_jsonb(z1 * n2 =  z2 * n1);
    when '!=' then return to_jsonb(z1 * n2 <> z2 * n1);
    when '<'  then return to_jsonb(z1 * n2 <  z2 * n1);
    when '<=' then return to_jsonb(z1 * n2 <= z2 * n1);
    when '>'  then return to_jsonb(z1 * n2 >  z2 * n1);
    when '>=' then return to_jsonb(z1 * n2 >= z2 * n1);
    else raise exception 'bedingung: % nicht erlaubt', op;
  end case;
end $$;

-- Bewertung einer Antwort: {format_ok, richtig, verletzt?, hinweis?} – wie tools/bedingung.py: bewerte.
create or replace function schule.bed_bewerten(p_felder jsonb, p_bedingungen jsonb, p_antwort jsonb)
 returns jsonb language plpgsql immutable set search_path to ''
as $$
declare v_roh jsonb; v_f jsonb; v_b jsonb; v_w jsonb; v_e jsonb; v_werte jsonb := '[]'; v_r jsonb; v_ok boolean; v_text text; v_aus jsonb; i int; s text; z numeric;
  v_gross constant jsonb := jsonb_build_object('format_ok', false, 'hinweis', 'Mit diesen Zahlen wird die Rechnung zu groß. Nimm kleinere Zahlen.');
  v_leer constant jsonb := jsonb_build_object('format_ok', false, 'hinweis', 'Bitte fülle alle Felder aus.');
begin
  -- Inhaltsfehler, kein „richtig“: Eine Aufgabe ohne Felder oder ohne Bedingungen wird nicht bewertet.
  if jsonb_typeof(p_felder) is distinct from 'array' or jsonb_array_length(p_felder) not between 1 and 6
     or jsonb_typeof(p_bedingungen) is distinct from 'array' or jsonb_array_length(p_bedingungen) not between 1 and 8 then
    raise exception 'bedingung: Aufgabe ungültig (1 bis 6 Felder und 1 bis 8 Bedingungen nötig)';
  end if;
  if jsonb_typeof(p_antwort) is distinct from 'object' then return v_leer; end if;
  v_roh := p_antwort->'werte';
  if jsonb_typeof(v_roh) is distinct from 'array' or jsonb_array_length(v_roh) <> jsonb_array_length(p_felder) then return v_leer; end if;
  for i in 0 .. jsonb_array_length(p_felder) - 1 loop
    v_f := p_felder->i;
    -- Erlaubt: Text und JSON-Zahl mit ganzem Wert (es zählt der Wert, nicht die Schreibweise). Alles andere ist Format falsch.
    v_e := v_roh->i; v_w := null;
    if jsonb_typeof(v_e) = 'null' then return v_leer;
    elsif jsonb_typeof(v_e) = 'string' then
      s := v_e#>>'{}';
      if schule.bed_putzen(s) = '' then return v_leer; end if;
      v_w := schule.bed_lesen(s, v_f->>'art');
    elsif jsonb_typeof(v_e) = 'number' then
      z := (v_e#>>'{}')::numeric;
      if z = trunc(z) then v_w := schule.bed_lesen(trunc(z)::text, v_f->>'art'); end if;
    end if;
    if v_w is null then
      return jsonb_build_object('format_ok', false, 'hinweis', case when v_f->>'art' = 'ganz'
        then 'In dieses Feld gehört eine ganze Zahl, zum Beispiel −3.' else 'Bitte gib eine Zahl ein, zum Beispiel −3, 2,5 oder 3/4.' end);
    end if;
    if (v_w->>'z')::numeric < coalesce((v_f->>'min')::numeric, -999999) * (v_w->>'n')::numeric
       or (v_w->>'z')::numeric > coalesce((v_f->>'max')::numeric, 999999) * (v_w->>'n')::numeric then
      return jsonb_build_object('format_ok', false, 'hinweis', 'Diese Zahl liegt außerhalb des erlaubten Bereichs.');
    end if;
    v_werte := v_werte || jsonb_build_array(v_w);
  end loop;
  for i in 0 .. jsonb_array_length(p_bedingungen) - 1 loop
    v_b := p_bedingungen->i;
    begin
      v_r := schule.bed_wert(v_b->'pruefe', v_werte);
      if jsonb_typeof(v_r) <> 'boolean' then raise exception 'bedingung: pruefe muss wahr oder falsch liefern'; end if;
      v_ok := v_r::boolean;
    exception when sqlstate 'BG001' then v_ok := false;
              when sqlstate 'BG002' then return v_gross;
    end;
    if not v_ok then
      v_aus := jsonb_build_object('format_ok', true, 'richtig', false, 'verletzt', v_b->>'name');
      v_text := nullif(v_b->>'hinweis', '');
      if v_text is not null and position('{}' in v_text) > 0 then
        begin
          v_text := replace(v_text, '{}', schule.bed_deutsch(schule.bed_wert(v_b->'zeige', v_werte)));
        exception when sqlstate 'BG001' then v_text := null;
                  when sqlstate 'BG002' then return v_gross;
        end;
      end if;
      if nullif(v_text, '') is not null then v_aus := v_aus || jsonb_build_object('hinweis', v_text); end if;
      return v_aus;
    end if;
  end loop;
  return jsonb_build_object('format_ok', true, 'richtig', true);
end $$;

-- Prüft einen Baum, ohne ihn auszurechnen: Namen, Argumentzahl, Tiefe, Feldnummern, Konstanten und die Typen in JEDEM Ast.
-- Rückgabe {"n": Knoten, "t": 'zahl' | 'wahr' | 'liste'}. Fehler: SQLSTATE BG003 mit Text.
create or replace function schule.bed_baum(p_baum jsonb, p_felder int, p_tiefe int)
 returns jsonb language plpgsql immutable set search_path to ''
as $$
declare t text := jsonb_typeof(p_baum); s text; op text; c int; lo int; hi int; soll text; erg text; n int := 1; r jsonb; z numeric; m text[]; i int;
begin
  if p_tiefe > 8 then raise exception 'Baum zu tief' using errcode = 'BG003'; end if;
  if t = 'number' then
    z := (p_baum#>>'{}')::numeric;
    if z <> trunc(z) or abs(z) > 999999 then raise exception 'Konstante muss eine ganze Zahl bis 999 999 sein' using errcode = 'BG003'; end if;
    return jsonb_build_object('n', 1, 't', 'zahl');
  elsif t = 'string' then
    s := p_baum#>>'{}';
    if s = '$alle' then return jsonb_build_object('n', 1, 't', 'liste'); end if;
    if s ~ '^\$[1-6]$' then
      if substr(s, 2)::int > p_felder then raise exception '%: so viele Felder gibt es nicht', s using errcode = 'BG003'; end if;
      return jsonb_build_object('n', 1, 't', 'zahl');
    end if;
    if s ~ '^[+-]?[0-9]{1,6}(,[0-9]{1,3})?$' then return jsonb_build_object('n', 1, 't', 'zahl'); end if;
    m := regexp_match(s, '^([+-]?[0-9]{1,6})/([0-9]{1,6})$');
    if m is not null and m[2]::numeric <> 0 then return jsonb_build_object('n', 1, 't', 'zahl'); end if;
    raise exception 'unbekannter Name' using errcode = 'BG003';
  elsif t is distinct from 'array' or jsonb_array_length(p_baum) = 0 or jsonb_typeof(p_baum->0) <> 'string' then
    raise exception 'nicht erlaubt' using errcode = 'BG003';
  end if;
  op := p_baum->>0; c := jsonb_array_length(p_baum) - 1;
  if op in ('+', '*') then lo := 2; hi := 6; soll := 'zahl'; erg := 'zahl';
  elsif op in ('-', '/', 'hoch') then lo := 2; hi := 2; soll := 'zahl'; erg := 'zahl';
  elsif op in ('neg', 'betrag') then lo := 1; hi := 1; soll := 'zahl'; erg := 'zahl';
  elsif op = 'liste' then lo := 1; hi := 6; soll := 'zahl'; erg := 'liste';
  elsif op in ('summe','produkt','min','max','median','mittelwert','anzahl','anzahl_positiv','anzahl_negativ') then lo := 1; hi := 1; soll := 'liste'; erg := 'zahl';
  elsif op = 'verschieden' then lo := 1; hi := 1; soll := 'liste'; erg := 'wahr';
  elsif op = 'ganzzahlig' then lo := 1; hi := 1; soll := 'zahl'; erg := 'wahr';
  elsif op in ('teilbar', '=', '!=', '<', '<=', '>', '>=') then lo := 2; hi := 2; soll := 'zahl'; erg := 'wahr';
  elsif op in ('und', 'oder') then lo := 2; hi := 6; soll := 'wahr'; erg := 'wahr';
  elsif op = 'nicht' then lo := 1; hi := 1; soll := 'wahr'; erg := 'wahr';
  else raise exception 'unbekannte Operation' using errcode = 'BG003';
  end if;
  if c < lo or c > hi then raise exception '%: falsche Zahl von Argumenten', op using errcode = 'BG003'; end if;
  for i in 1 .. c loop
    r := schule.bed_baum(p_baum->i, p_felder, p_tiefe + 1);
    if r->>'t' <> soll then raise exception '%: Operand muss % sein', op, soll using errcode = 'BG003'; end if;
    n := n + (r->>'n')::int;
  end loop;
  return jsonb_build_object('n', n, 't', erg);
end $$;

-- Ist die Aufgabe zulässig? null = ja, sonst der Grund. Dasselbe Urteil wie tools/bedingung.py: pruefe_aufgabe(a, nur_form=True).
-- Teil 2 hängt diese Prüfung als Constraint an schule.aufgabe; damit gilt sie für jeden Schreibweg, nicht nur für den Python-Prüfer.
create or replace function schule.bed_gueltig(p_frage jsonb, p_loesung jsonb)
 returns text language plpgsql immutable set search_path to ''
as $$
declare v_felder jsonb := p_frage->'felder'; v_beds jsonb := p_loesung->'bedingungen'; v_f jsonb; v_b jsonb; v_r jsonb;
  v_namen text[] := '{}'; v_name text; i int; k int; n int; mn numeric; mx numeric;
begin
  if jsonb_typeof(v_felder) is distinct from 'array' or jsonb_array_length(v_felder) not between 1 and 6 then return 'felder: 1 bis 6 Felder nötig'; end if;
  k := jsonb_array_length(v_felder);
  for i in 0 .. k - 1 loop
    v_f := v_felder->i;
    if jsonb_typeof(v_f) <> 'object' or coalesce(v_f->>'art', '') not in ('ganz', 'rational') or jsonb_typeof(v_f->'art') <> 'string' then return 'Feld ' || (i + 1) || ': art muss ganz oder rational sein'; end if;
    mn := -999999; mx := 999999;
    if v_f ? 'min' then
      if jsonb_typeof(v_f->'min') <> 'number' or (v_f->>'min')::numeric <> trunc((v_f->>'min')::numeric) then return 'Feld ' || (i + 1) || ': min/max müssen ganze Zahlen sein'; end if;
      mn := (v_f->>'min')::numeric;
    end if;
    if v_f ? 'max' then
      if jsonb_typeof(v_f->'max') <> 'number' or (v_f->>'max')::numeric <> trunc((v_f->>'max')::numeric) then return 'Feld ' || (i + 1) || ': min/max müssen ganze Zahlen sein'; end if;
      mx := (v_f->>'max')::numeric;
    end if;
    if not (-999999 <= mn and mn <= mx and mx <= 999999) then return 'Feld ' || (i + 1) || ': min/max außerhalb der Grenzen'; end if;
  end loop;
  if jsonb_typeof(v_beds) is distinct from 'array' or jsonb_array_length(v_beds) not between 1 and 8 then return 'bedingungen: 1 bis 8 nötig'; end if;
  for i in 0 .. jsonb_array_length(v_beds) - 1 loop
    v_b := v_beds->i;
    v_name := case when jsonb_typeof(v_b) = 'object' then nullif(v_b->>'name', '') end;
    if v_name is null or v_name = any (v_namen) then return 'Bedingung ohne eigenen Namen'; end if;
    v_namen := v_namen || v_name;
    begin
      v_r := schule.bed_baum(v_b->'pruefe', k, 1);
      if v_r->>'t' <> 'wahr' then return v_name || ': pruefe muss wahr oder falsch liefern'; end if;
      n := (v_r->>'n')::int;
      if position('{}' in coalesce(v_b->>'hinweis', '')) > 0 then
        v_r := schule.bed_baum(v_b->'zeige', k, 1);
        if v_r->>'t' <> 'zahl' then return v_name || ': zeige muss eine Zahl liefern'; end if;
        n := n + (v_r->>'n')::int;
      elsif v_b ? 'zeige' then return v_name || ': zeige ohne {} im hinweis';
      end if;
      if n > 60 then return v_name || ': mehr als 60 Knoten'; end if;
    exception when sqlstate 'BG003' then return v_name || ': ' || sqlerrm;
    end;
  end loop;
  if jsonb_typeof(p_loesung->'beispiel') is distinct from 'array' then return 'beispiel fehlt'; end if;
  v_r := schule.bed_bewerten(v_felder, v_beds, jsonb_build_object('werte', p_loesung->'beispiel'));
  if not ((v_r->>'format_ok')::boolean and coalesce((v_r->>'richtig')::boolean, false)) then return 'beispiel besteht nicht'; end if;
  return null;
end $$;

-- Zweig in schule.antwort_bewerten (Text-Patch). Drei Zustände, sonst Abbruch:
--   fertig     = der vollständige neue Zweig steht genau einmal da und bed_bewerten kommt sonst nicht vor -> nichts tun
--   alt        = der alte Anfang steht genau einmal da und bed_bewerten kommt nicht vor               -> einbauen
--   Mischstand = alles andere                                                                       -> Abbruch
do $$
declare d text;
  anker constant text := E'begin\n  if p_aufgabe.antworttyp = ''luecken'' then';
  neu constant text := E'begin\n  if p_aufgabe.antworttyp = ''bedingung'' then\n    return schule.bed_bewerten(p_aufgabe.frage->''felder'', p_aufgabe.loesung->''bedingungen'', p_antwort);\n  end if;\n  if p_aufgabe.antworttyp = ''luecken'' then';
  n_alt int; n_neu int; n_wort int;
begin
  d := pg_get_functiondef('schule.antwort_bewerten(schule.aufgabe, jsonb)'::regprocedure);
  n_alt := (length(d) - length(replace(d, anker, ''))) / length(anker);
  n_neu := (length(d) - length(replace(d, neu, ''))) / length(neu);
  n_wort := (length(d) - length(replace(d, 'bed_bewerten', ''))) / length('bed_bewerten');
  if n_neu = 1 and n_wort = 1 and n_alt = 0 then return; end if;
  if not (n_alt = 1 and n_wort = 0) then raise exception 'BD-S1: antwort_bewerten ist weder im alten noch im fertigen Zustand (alt %, neu %, bed_bewerten %)', n_alt, n_neu, n_wort; end if;
  execute replace(d, anker, neu);
end $$;

revoke all on function schule.bed_bruch(numeric, numeric), schule.bed_z(jsonb), schule.bed_putzen(text), schule.bed_lesen(text, text),
  schule.bed_deutsch(jsonb), schule.bed_wert(jsonb, jsonb), schule.bed_bewerten(jsonb, jsonb, jsonb),
  schule.bed_baum(jsonb, int, int), schule.bed_gueltig(jsonb, jsonb) from public, anon, authenticated;
