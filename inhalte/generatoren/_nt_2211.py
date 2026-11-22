"""NT-D (22.11.2026): fehlende Sicherungs-Aufgaben für die Nachtests kleiner Flüge (Fehlliste NT-S)
und Thema 57 „verzerrte Diagramme berichtigen/verbessern“ (Rückläufer ChatGPT 947–950).

Hängt nur Aufgaben an bestehende Etappen an (keine neuen Lernkarten). Texte selbst formuliert, Lösungen hier berechnet.
Zweiter Lauf hängt nichts doppelt an. Aufruf am Ende der Generatoren (nach dem LK-Haken) oder direkt:
  python3 _nt_2211.py [thema …]          – Aufgaben anhängen
  python3 _nt_2211.py --sql              – inhalte/pruefung/lehrplan/nt_einspiel_2211.sql schreiben
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lk_etappen_2211 import auf, wahl, z, _schluessel

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
SQL = Path(__file__).resolve().parent.parent / 'pruefung' / 'lehrplan' / 'nt_einspiel_2211.sql'


def S(l, y, text, w, **x):
    return auf(l, 'sicherung', 2, None, y, text, w, **x)


def luecken(text, schablone, hinweis, werte):
    return {'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis}, 'o': {'werte': werte}}


def L_(l, s, y, text, w, schablone, hinweis, werte, p='sicherung', g=None, h=None):
    a = auf(l, p, s, g, y, text, w, h)
    a.update(luecken(text, schablone, hinweis, werte))
    return a


# ------------------------------------------------------------------ 46 punktspiegelung (Gym 46 Teil 3: 6 von 15 → +9)
def punktspiegelung():
    l = 'punktspiegelung'
    A = []
    for (px, py, zx, zy) in ((5, 1, 2, 3), (-3, 4, 1, -1), (0, -5, -2, 0), (7, -2, 3, 1), (-6, -3, -1, -2)):
        bx, by = 2 * zx - px, 2 * zy - py
        A.append(L_(l, 2, 'luecken', f'Spiegle den Punkt P({z(px)} | {z(py)}) am Zentrum Z({z(zx)} | {z(zy)}).',
                    f'Z ist die Mitte von P und P\': x = 2 · {z(zx)} − {z(px)} = {z(bx)}, y = 2 · {z(zy)} − {z(py)} = {z(by)}. Also P\'({z(bx)} | {z(by)}).',
                    "P'(□ | □)", 'x-Koordinate, dann y-Koordinate', [bx, by]))
    A.append(S(l, 'zahl', 'P(2 | 5) wird an Z gespiegelt und landet bei P\'(8 | −1). Welche x-Koordinate hat Z?',
               'Z ist die Mitte von P und P\': x = (2 + 8) : 2 = 5.', o={'wert': 5}, c='(2 + 8) / 2'))
    A.append(S(l, 'zahl', 'P(−4 | 3) und P\'(6 | −7) liegen punktsymmetrisch zu Z. Welche y-Koordinate hat Z?',
               'Z ist die Mitte: y = (3 + (−7)) : 2 = −2.', o={'wert': -2}, c='(3 - 7) / 2'))
    A.append(S(l, 'auswahl', 'Eine Strecke AB wird an einem Punkt Z gespiegelt. Wie liegt die Bildstrecke A\'B\' zu AB?',
               'Die Punktspiegelung ist eine Drehung um 180°: Die Bildstrecke ist gleich lang und parallel zu AB, sie zeigt nur in die Gegenrichtung.',
               **wahl('parallel und gleich lang', ['senkrecht und gleich lang', 'parallel und doppelt so lang', 'auf derselben Geraden, halb so lang'], 0)))
    A.append(S(l, 'auswahl', 'Welche dieser Figuren ist immer punktsymmetrisch?',
               'Beim Parallelogramm halbieren sich die Diagonalen; ihr Schnittpunkt ist das Symmetriezentrum. Drachen und gleichschenkliges Trapez sind nur achsensymmetrisch.',
               **wahl('Parallelogramm', ['Drachenviereck', 'gleichschenkliges Trapez', 'gleichschenkliges Dreieck'], 2)))
    return A


# ------------------------------------------------------------------ 91 rotation, axialschnitt (Gym 91 Teil 2: je 6 von 9 → je +3)
def rotation():
    l = 'rotation'
    return [
        S(l, 'zahl', 'Ein Rechteck mit den Seiten 5 cm und 8 cm dreht sich um die 5-cm-Seite. Welchen Radius hat der entstehende Zylinder?',
          'Die 5-cm-Seite liegt auf der Achse und wird zur Höhe; die 8-cm-Seite steht senkrecht dazu und wird zum Radius: r = 8 cm.', o={'wert': 8, 'einheit': 'cm'}, c='8'),
        S(l, 'auswahl', 'Ein Halbkreis dreht sich um seinen Durchmesser. Welcher Körper entsteht?',
          'Jeder Punkt des Bogens beschreibt einen Kreis um die Achse; zusammen ergibt das eine Kugel.',
          **wahl('eine Kugel', ['ein Kegel', 'ein Zylinder', 'eine Halbkugel'], 1)),
        L_(l, 2, 'luecken', 'Ein rechtwinkliges Dreieck mit den Katheten 4 cm und 10 cm dreht sich um die 10-cm-Kathete. Gib Radius und Höhe des Kegels an.',
           'Die Kathete auf der Achse (10 cm) wird zur Höhe, die andere (4 cm) zum Radius.', 'r = □ cm; h = □ cm', 'je eine ganze Zahl', [4, 10]),
    ]


def axialschnitt():
    l = 'axialschnitt'
    return [
        S(l, 'zahl', 'Ein Zylinder hat r = 6 cm und h = 10 cm. Wie groß ist der Flächeninhalt seines Axialschnitts?',
          'Der Axialschnitt ist ein Rechteck aus Durchmesser und Höhe: 12 cm · 10 cm = 120 cm².', o={'wert': 120, 'einheit': 'cm²'}, c='2 * 6 * 10'),
        S(l, 'auswahl', 'Welche Form hat der Axialschnitt eines geraden Kreiskegels?',
          'Der Schnitt durch die Achse trifft die Spitze und einen Durchmesser der Grundfläche: ein gleichschenkliges Dreieck.',
          **wahl('ein gleichschenkliges Dreieck', ['ein Rechteck', 'ein Kreis', 'ein Trapez'], 0)),
        L_(l, 2, 'luecken', 'Ein Zylinder hat r = 3 cm und h = 7 cm. Welche Seitenlängen hat das Rechteck des Axialschnitts?',
           'Eine Seite ist der Durchmesser 2 · 3 = 6 cm, die andere die Höhe 7 cm.', '□ cm × □ cm', 'erst die Breite (Durchmesser), dann die Höhe', [6, 7]),
    ]


# ------------------------------------------------------------------ 101 cavalieri (101 Teil 2, 1 Pflicht-Etappe: 6 von 15 → +9)
def cavalieri():
    l = 'cavalieri'
    A = []
    for g, h in ((18, 4), (25, 6), (9, 11)):
        A.append(S(l, 'zahl', f'Ein schiefes Prisma hat die Grundfläche G = {g} cm² und die Höhe h = {h} cm. Berechne sein Volumen.',
                   f'Nach Cavalieri gilt auch für schiefe Prismen V = G · h = {g} · {h} = {g * h} cm³.', o={'wert': g * h, 'einheit': 'cm³'}, c=f'{g} * {h}'))
    for v, g in ((96, 12), (150, 25)):
        A.append(S(l, 'zahl', f'Ein schiefer Zylinder hat das Volumen {v} cm³ und die Grundfläche {g} cm². Wie hoch ist er?',
                   f'V = G · h, also h = V : G = {v} : {g} = {v // g} cm.', o={'wert': v // g, 'einheit': 'cm'}, c=f'{v} / {g}'))
    A.append(S(l, 'auswahl', 'Zwei Körper haben in jeder Höhe gleich große Querschnittsflächen und sind gleich hoch. Was folgt nach Cavalieri?',
               'Das Prinzip von Cavalieri: gleiche Querschnitte in jeder Höhe und gleiche Höhe ergeben gleiches Volumen – die Form darf verschieden sein.',
               **wahl('Sie haben das gleiche Volumen.', ['Sie haben die gleiche Oberfläche.', 'Sie sind deckungsgleich.', 'Der schiefere Körper hat mehr Volumen.'], 0)))
    A.append(S(l, 'auswahl', 'Ein Stapel Münzen wird schräg geschoben. Was bleibt gleich?',
               'Jede Münze behält ihre Fläche und die Stapelhöhe ändert sich nicht. Deshalb bleibt das Volumen gleich, auch wenn der Stapel schief steht.',
               **wahl('das Volumen', ['die Oberfläche', 'die Länge der Seitenkante', 'die Form der Seitenfläche'], 3)))
    A.append(L_(l, 2, 'luecken', 'Ein gerades und ein schiefes Prisma haben beide G = 14 cm² und die Höhe 5 cm. Berechne beide Volumen.',
                'Beide: V = G · h = 14 · 5 = 70 cm³. Die Schräge ändert das Volumen nicht.', 'gerade: □ cm³; schief: □ cm³', 'je eine ganze Zahl', [70, 70]))
    A.append(L_(l, 2, 'luecken', 'Ein schiefer Zylinder hat den Radius 2 cm und die Höhe 9 cm. Schreibe sein Volumen als Vielfaches von π.',
                'G = π · 2² = 4π cm². V = G · h = 4π · 9 = 36π cm³.', 'V = □ · π cm³', 'eine ganze Zahl', [36]))
    return A


# ------------------------------------------------------------------ 44 vierecke, vierecke_konstruieren (RS I 44 Teil 2: je +3)
def vierecke():
    l = 'vierecke'
    return [
        S(l, 'zahl', 'In einem Parallelogramm ist α = 70°. Wie groß ist β?',
          'Benachbarte Winkel im Parallelogramm ergänzen sich zu 180°: β = 180° − 70° = 110°.', o={'wert': 110, 'einheit': '°'}, c='180 - 70'),
        S(l, 'auswahl', 'In welchem Viereck stehen die Diagonalen immer senkrecht aufeinander und halbieren sich?',
          'In der Raute halbieren sich die Diagonalen (wie im Parallelogramm) und stehen senkrecht aufeinander (wie im Drachen).',
          **wahl('Raute', ['Rechteck', 'Parallelogramm', 'Trapez'], 1)),
        L_(l, 2, 'luecken', 'In einem Parallelogramm ABCD ist α = 65°. Berechne β und γ.',
           'β = 180° − 65° = 115° (benachbart), γ = α = 65° (gegenüber).', 'β = □°; γ = □°', 'je eine ganze Zahl', [115, 65]),
    ]


def vierecke_konstruieren():
    l = 'vierecke_konstruieren'
    return [
        S(l, 'zahl', 'Ein Viereck hat die Winkel 100°, 75° und 80°. Berechne den vierten Winkel.',
          'Die Winkelsumme im Viereck ist 360°: 360° − 100° − 75° − 80° = 105°.', o={'wert': 105, 'einheit': '°'}, c='360 - 100 - 75 - 80'),
        S(l, 'zahl', 'Ein Trapez ABCD hat AB ∥ CD und α = 70°. Wie groß ist δ?',
          'α und δ liegen am selben Schenkel AD zwischen den Parallelen und ergänzen sich zu 180°: δ = 110°.', o={'wert': 110, 'einheit': '°'}, c='180 - 70'),
        S(l, 'auswahl', 'Welche Angaben legen ein Rechteck eindeutig fest?',
          'Alle Winkel eines Rechtecks sind 90°. Mit zwei benachbarten Seitenlängen ist es eindeutig konstruierbar.',
          **wahl('zwei benachbarte Seitenlängen', ['ein Winkel', 'eine Seitenlänge', 'zwei gegenüberliegende Seitenlängen'], 2)),
    ]


# ------------------------------------------------------------------ 30 potenz_begriff (+3), negativer_exponent (+2)
def potenz_begriff():
    l = 'potenz_begriff'
    return [
        S(l, 'zahl', 'Berechne (−3)³.', '(−3)³ = (−3) · (−3) · (−3) = −27. Drei Minuszeichen: ungerade Anzahl, also negativ.', o={'wert': -27}, c='(-3) ** 3'),
        S(l, 'auswahl', 'Was bedeutet 5⁴?', 'Die Hochzahl gibt an, wie oft die Basis mit sich selbst malgenommen wird: 5⁴ = 5 · 5 · 5 · 5 = 625.',
          **wahl('5 · 5 · 5 · 5', ['5 · 4', '4 · 4 · 4 · 4 · 4', '5 + 5 + 5 + 5'], 0)),
        L_(l, 2, 'luecken', 'Berechne (3/4)².', 'Zähler und Nenner quadrieren: 3² / 4² = 9/16.', '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.', [9, 16]),
    ]


def negativer_exponent():
    l = 'negativer_exponent'
    return [
        S(l, 'zahl', 'Schreibe 2⁻³ als Dezimalzahl.', '2⁻³ = 1/2³ = 1/8 = 0,125.', o={'wert': 0.125}, c='2 ** -3'),
        L_(l, 2, 'luecken', 'Berechne 4⁻².', '4⁻² = 1/4² = 1/16.', '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.', [1, 16]),
    ]


# ------------------------------------------------------------------ 57 irrefuehrend: verzerrte Diagramme berichtigen/verbessern (RS 5 6/k3, RS 7 8/K4 bzw. 6/K4)
def irrefuehrend():
    l = 'irrefuehrend'
    U = lambda s, g, y, text, w, h, **x: auf(l, 'uebung', s, g, y, text, w, h, **x)
    return [
        U(1, 'direkt', 'zahl', 'Du zeichnest ein Säulendiagramm richtig neu: Die Hochachse beginnt bei 0, 1 cm steht für 10 Stimmen. Wie hoch wird die Säule für 40 Stimmen?',
          '40 : 10 = 4, also 4 cm. Weil die Achse bei 0 beginnt, sind die Höhen echt vergleichbar.', 'Teile den Wert durch 10.', o={'wert': 4, 'einheit': 'cm'}, c='40 / 10'),
        U(1, 'erkennen', 'auswahl', 'Die Hochachse eines Säulendiagramms beginnt bei 90, die Werte sind 92 und 98. Wie verbesserst du das Diagramm?',
          'Damit die Säulenhöhen den Werten entsprechen, muss die Achse bei 0 beginnen – oder die Lücke muss deutlich mit einem Achsenbruch markiert werden.', 'Wo muss eine Hochachse beginnen?',
          **wahl('Die Achse bei 0 beginnen lassen.', ['Die Säulen breiter machen.', 'Die Werte runden.', 'Die Säulen farbig machen.'], 0)),
        L_(l, 2, 'luecken', 'Zeichne ehrlich neu: Die Achse beginnt bei 0, 1 cm steht für 30 Stück. Wie hoch werden die Säulen für 120 und 150 Stück?',
           '120 : 30 = 4 cm und 150 : 30 = 5 cm. Jetzt ist die zweite Säule nur 1/4 höher – genau wie die Werte.',
           '□ cm und □ cm', 'je eine ganze Zahl', [4, 5], p='uebung', g='mehrschritt', h='Teile jeden Wert durch 30.'),
        U(2, 'einkleidung', 'zahl', 'Auf einer Zeitachse stehen 2010, 2015, 2016 und 2020 in gleichen Abständen von 5 cm. Richtig wäre 1 cm pro Jahr. Wie lang muss der Abstand von 2015 bis 2016 werden?',
          'Zwischen 2015 und 2016 liegt ein Jahr, also 1 cm (statt 5 cm). Gleiche Abstände für ungleiche Zeiträume verzerren den Verlauf.', 'Wie viele Jahre liegen dazwischen?', o={'wert': 1, 'einheit': 'cm'}, c='2016 - 2015'),
        U(2, 'darstellung', 'auswahl', 'In einem Bilddiagramm soll Laden B doppelt so viel verkaufen wie Laden A. Wie stellst du das ehrlich dar?',
          'Doppelt so viele gleich große Symbole verdoppeln die Fläche genau. Ein Symbol mit doppelter Höhe und Breite hätte die vierfache Fläche.', 'Achte auf die Fläche der Bilder.',
          **wahl('B bekommt doppelt so viele gleich große Symbole.', ['Das Symbol von B wird doppelt so hoch und doppelt so breit.', 'Das Symbol von B wird dreimal so groß.', 'B bekommt eine andere Farbe.'], 1)),
        U(3, 'fehler', 'zahl', 'Lea verbessert ein Diagramm: Achse ab 0, Säule A (80 Punkte) ist 4 cm hoch. Säule B (90 Punkte) zeichnet sie 6 cm hoch. Wie hoch muss B richtig sein?',
          '4 cm stehen für 80, also 1 cm für 20. 90 : 20 = 4,5 cm. Leas 6 cm übertreiben den Unterschied.', 'Wie viele Punkte stehen für 1 cm?', o={'wert': 4.5, 'einheit': 'cm'}, c='90 / (80 / 4)'),
        U(3, 'transfer', 'zahl', 'In einem Kreisdiagramm ist ein Anteil von 25 % als Sektor mit 120° gezeichnet. Mit welchem Winkel ist er richtig?',
          '25 % von 360° sind 90°. Der gezeichnete Sektor mit 120° ist zu groß.', 'Der ganze Kreis hat 360°.', o={'wert': 90, 'einheit': '°'}, c='360 * 25 / 100'),
        U(3, 'begruenden', 'auswahl', 'Warum ist ein schräg gekipptes 3D-Kreisdiagramm oft irreführend, und wie verbesserst du es?',
          'Durch das Kippen wirken die vorderen Stücke größer als die hinteren. Ein flaches Kreisdiagramm zeigt die Anteile unverzerrt.', 'Welche Stücke sieht man größer?',
          **wahl('Vordere Stücke wirken größer – besser flach zeichnen.', ['Es hat zu viele Farben – besser grau zeichnen.', 'Es ist zu klein – besser größer zeichnen.', 'Es fehlt eine Hochachse – besser eine ergänzen.'], 2)),
        U(3, 'rueckwaerts', 'zahl', 'In einem ehrlich gezeichneten Säulendiagramm steht 1 cm für 20 €. Eine Säule ist 7,5 cm hoch. Welchen Wert zeigt sie?',
          '7,5 · 20 € = 150 €.', 'Multipliziere die Höhe mit dem Wert für 1 cm.', o={'wert': 150, 'einheit': '€'}, c='7.5 * 20'),
    ]


NT = {'abbildungen.kongruenz': [punktspiegelung], 'raum.schraegbilder': [rotation, axialschnitt],
      'messen.prisma_zylinder': [cavalieri], 'geometrie.konstruktion': [vierecke, vierecke_konstruieren],
      'terme.potenzgesetze': [potenz_begriff, negativer_exponent], 'daten.darstellen': [irrefuehrend]}
# thema_id, Einheit (echte DB 22.11.) – nach TL-S sucht das SQL die Einheit über teil_stamm und den Etappen-Katalog
TID = {'abbildungen.kongruenz': 46, 'raum.schraegbilder': 91, 'messen.prisma_zylinder': 101, 'geometrie.konstruktion': 44,
       'terme.potenzgesetze': 30, 'daten.darstellen': 57}


def nt_anhaengen(thema):
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    lz = [e['lernziel'] for e in d['inhalt']['etappen']]
    da = {_schluessel(a) for a in d['aufgaben']}
    n = 0
    for fn in NT[thema]:
        for a in fn():
            assert a['l'] in lz, (thema, a['l'])
            if _schluessel(a) in da:
                continue
            d['aufgaben'].append(a); da.add(_schluessel(a)); n += 1
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'  NT {thema}: {n} neue Aufgaben')


def sql():
    teile, soll = [], []
    for thema, fns in NT.items():
        t = TID[thema]
        for fn in fns:
            A = [{k: v for k, v in a.items() if k not in ('c', 'zahl')} for a in fn()]
            l = A[0]['l']; n = len(A); pools = sorted({a['p'] for a in A})
            s = json.dumps(A, ensure_ascii=False, separators=(', ', ': ')); assert '$j$' not in s
            soll.append((t, l, n, [a['f']['text'] for a in A]))
            teile.append(f"""
-- Thema {t} ({thema}), Etappe {l}: {n} Aufgaben ({', '.join(pools)})
do $nt$
declare v_e bigint; v_max int; v_auf jsonb; v_n int; v_stamm boolean;
begin
  v_stamm := exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm');
  -- Einheit mit dieser Etappe im Katalog: vor der Teilung die Einheit des Themas, danach die des richtigen Teils
  execute format('select e.id from schule.einheit e join schule.thema t on t.id = e.thema_id
                   where e.status <> %L and (t.id = $1 %s)
                     and exists (select 1 from jsonb_array_elements(coalesce(e.inhalt->%L, %L::jsonb)) x where x->>%L = $2)
                   order by e.id limit 1', 'ersetzt', case when v_stamm then 'or t.teil_stamm = $1' else '' end, 'etappen', '[]', 'lernziel')
    into v_e using {t}::bigint, '{l}'::text;
  if v_e is null then raise exception 'Thema {t}: keine Einheit mit Etappe {l} – zuerst lk_einspiel_2211.sql einspielen'; end if;
  if (select schluessel from schule.thema where id = {t}) <> '{thema}' then raise exception 'Thema {t} ist nicht {thema}'; end if;
  select coalesce(max(reihenfolge), 0) into v_max from schule.aufgabe where einheit_id = v_e;
  select jsonb_agg(x.a || jsonb_build_object('r', v_max + x.nr)) into v_auf
    from jsonb_array_elements($j${s}$j$::jsonb) with ordinality x(a, nr);
  v_n := schule.aufgaben_einfuegen(v_e, v_auf);
  raise notice 'Einheit % ({l}): % von {n} Aufgaben eingefügt (0 = schon vorhanden)', v_e, v_n;
  if v_n not in (0, {n}) then raise exception 'Etappe {l}: nur % von {n} eingefügt – teilweise vorhanden, bitte prüfen', v_n; end if;
end $nt$;
""")
    def q(x): return "'" + x.replace("'", "''") + "'"
    bed = ' or '.join(f"(a.variante_gruppe = '{l}' and a.thema_id in (select x.id from schule.thema x where x.id = {t} or x.%1$I = {t}) and a.frage->>'text' in ({', '.join(q(x) for x in tx)}))" for t, l, n, tx in soll)
    bed = bed.replace('%', '%%').replace('%%1$I', '%1$I')   # format(): Prozentzeichen im Text schützen
    ges = sum(n for t, l, n, tx in soll)
    sich = sum(1 for thema, fns in NT.items() for fn in fns for a in fn() if a['p'] == 'sicherung')
    kopf = f"""-- NT-D (22.11.2026): fehlende Sicherungs-Aufgaben für Nachtests kleiner Flüge (Fehlliste NT-S) und Thema 57 „verzerrte Diagramme berichtigen/verbessern“.
-- Quelle: inhalte/generatoren/_nt_2211.py (Texte selbst formuliert, Lösungen berechnet), Dateien inhalte/themen/*.json. {ges} Aufgaben, davon {sich} Sicherung.
-- Nur für den Haupt-Chat; NICHT von lehrplan-lb ausgeführt. In EINER Transaktion einspielen (psql -1). Wiederholt ausführbar.
-- Nur INSERT über schule.aufgaben_einfuegen; Einheiten werden nicht verändert. Kein DELETE, kein DROP.
-- Reihenfolge: NACH lk_einspiel_2211.sql (cavalieri und vierecke_konstruieren gibt es erst dann; sonst Abbruch mit Hinweis).
--   Vor oder nach TL-S möglich: Das SQL sucht die Einheit, deren Etappen-Katalog die Etappe enthält (Thema oder Teil über teil_stamm).
--   Empfohlen vor TL-S, dann ziehen die Aufgaben mit ihrer Etappe in den Teil (gleiche Ids).
-- Die neuen Aufgaben sind sofort sichtbar (aufgabe.freigegeben Standard true).
"""
    pruef = f"""
-- Rauchtest (liest nur)
do $pruef$
declare v int; v_f text := 'id';
begin
  -- nur Aufgaben der eigenen Themen (bzw. ihrer Teile nach TL-S) zählen – gleiche Texte in anderen Themen sind erlaubt
  if exists (select 1 from information_schema.columns where table_schema = 'schule' and table_name = 'thema' and column_name = 'teil_stamm') then
    v_f := 'teil_stamm';
  end if;
  execute format($q$select count(*) from schule.aufgabe a where {bed}$q$, v_f) into v;
  if v <> {ges} then raise exception 'Rauchtest NT-D: % von {ges} Aufgaben', v; end if;
  raise notice 'Rauchtest NT-D bestanden: {ges} Aufgaben ({sich} Sicherung)';
end $pruef$;
"""
    SQL.write_text(kopf + ''.join(teile) + pruef, encoding='utf-8')
    print(SQL, ges, 'Aufgaben')


if __name__ == '__main__':
    import sys
    if '--sql' in sys.argv:
        sql()
    else:
        for t in (sys.argv[1:] or list(NT)):
            nt_anhaengen(t)
