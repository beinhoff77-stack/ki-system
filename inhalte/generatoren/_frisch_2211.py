"""Frische Übungen (Auftrag „Aufgaben nachliefern“, 22.11.): je 8 neue Übungen der Stufen 2–3 für Etappen,
deren Kinder fast alle Übungen schon beantwortet haben (zahlen.ganz: zahlengerade, ordnen; gleichungen.linear: waage).

Wird als letzter Schritt der jeweiligen Generatoren aufgerufen. Hängt nur an: Vorhandene Aufgaben bleiben
unverändert (Wiedererkennung beim Einspielen über Frage + Antworten, `schule.einheit_abgleichen`).
Alle Lösungen werden hier berechnet; Texte selbst formuliert, keine Schulbuchaufgaben.
"""
import json
from fractions import Fraction as Fr
from pathlib import Path

THEMEN = Path(__file__).resolve().parent.parent / 'themen'


def z(n):
    """Zahl in Textschreibweise: Minus als −, Dezimalkomma."""
    if isinstance(n, Fr):
        n = int(n) if n.denominator == 1 else float(n)
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    s = str(n).replace('.', ',')
    return s.replace('-', '−')


def k(n):
    """Zahl in Rechnungen: negative geklammert."""
    return f'({z(n)})' if n < 0 else z(n)


def auswahl(richtig, falsch, pos):
    a = list(falsch)
    a.insert(pos, richtig)
    assert len(set(a)) == len(a), a
    return a, {'index': pos}


def ue(l, t, s, g, y, text, h, w, **x):
    a = {'l': l, 't': t, 'p': 'uebung', 's': s, 'y': y, 'f': {'text': text}, 'h': h, 'w': w, 'g': g}
    if 'grafik' in x:
        a['f']['grafik'] = x.pop('grafik')
    a.update(x)
    return a


# ---------------------------------------------------------------- zahlen.ganz · zahlengerade
def zahlengerade():
    L, T = 'zahlengerade', 'verstehen'
    A = []
    # 1 · Stufe 2 · einkleidung · markierung
    st, en, ab, ziel = -60, 90, 10, -30
    schritt = (en - st) // ab
    idx = (ziel - st) // schritt
    A.append(ue(L, T, 2, 'einkleidung', 'markierung',
                f'Eine Höhenskala an einer Steilküste reicht von {z(st)} m (Meeresgrund) bis {z(en)} m (Klippe) in {ab} gleichen Abschnitten. '
                f'Tippe an, wo {z(ziel)} m liegt.',
                'Wie viele Meter ist ein Abschnitt wert? Zähle dann vom Meeresgrund aus.',
                f'Von {z(st)} bis {z(en)} sind es {en - st} m, verteilt auf {ab} Abschnitte: {schritt} m je Abschnitt. '
                f'{z(ziel)} m liegt {idx} Abschnitte rechts von {z(st)} m.',
                grafik={'typ': 'zahlenstrahl', 'start': st, 'ende': en, 'abschnitte': ab, 'beschriftet': 'anfang_ende'},
                o={'index': idx}, zahl=ziel))
    # 2 · Stufe 2 · mehrschritt · zahl
    wert, anz, von = 4, 7, 6
    erg = von - anz * wert
    A.append(ue(L, T, 2, 'mehrschritt', 'zahl',
                f'Auf einer Zahlengeraden ist jeder Abschnitt {wert} wert. Der Punkt P liegt {anz} Abschnitte links von {z(von)}. Welche Zahl gehört zu P?',
                'Wie weit ist P insgesamt von der Zahl entfernt? Nach links heißt: kleiner werden.',
                f'{anz} Abschnitte zu je {wert} sind {anz * wert}. {z(von)} − {anz * wert} = {z(erg)}.',
                o={'wert': erg}, c=f'{von} - {anz} * {wert}'))
    # 3 · Stufe 2 · umkehr · zahl
    a, m = -14, -5
    b = 2 * m - a
    A.append(ue(L, T, 2, 'umkehr', 'zahl',
                f'Genau in der Mitte zwischen {z(a)} und einer zweiten Zahl liegt {z(m)}. Wie heißt die zweite Zahl?',
                'Wie weit ist es von der ersten Zahl bis zur Mitte? Genauso weit geht es auf der anderen Seite weiter.',
                f'Von {z(a)} bis {z(m)} sind es {m - a} Schritte nach rechts. Noch einmal {m - a} Schritte: {z(m)} + {m - a} = {z(b)}.',
                o={'wert': b}, c=f'2 * ({m}) - ({a})'))
    # 4 · Stufe 2 · darstellung · auswahl
    st, en, ab = -12, 18, 6
    sch = (en - st) // ab
    reihe = lambda xs: ', '.join(z(x) for x in xs)
    richtig = reihe(range(st, en + 1, sch))
    f1 = reihe(range(st, en + 1, (en - st) // (ab - 1)))          # einen Abschnitt zu wenig gezählt
    f2 = reihe([st + 3 * i for i in range(ab + 1)])               # Schritt 3 statt 5
    f3 = reihe([x if x <= 0 else x - 1 for x in range(st, en + 1, sch)][:-1] + [en])  # Fehler beim Übergang über 0
    a_, o_ = auswahl(richtig, [f1, f2, f3], 2)
    A.append(ue(L, T, 2, 'darstellung', 'auswahl',
                f'Eine Zahlengerade beginnt bei {z(st)} und endet bei {z(en)}. Dazwischen liegen {ab} gleich lange Abschnitte. '
                'Welche Zahlen stehen an den Strichen?',
                'Rechne zuerst aus, wie viel ein Abschnitt wert ist. Zähle dann vom Anfang aus weiter – auch über die 0 hinweg.',
                f'Von {z(st)} bis {z(en)} sind es {en - st}, verteilt auf {ab} Abschnitte: {sch} je Abschnitt. Also {richtig}.',
                a=a_, o=o_))
    # 5 · Stufe 3 · rueckwaerts · zahl
    re_, li, ende = 9, 15, -11
    anf = ende + li - re_
    A.append(ue(L, T, 3, 'rueckwaerts', 'zahl',
                f'Ein Punkt wird auf der Zahlengeraden erst um {re_} nach rechts und danach um {li} nach links geschoben. '
                f'Jetzt liegt er bei {z(ende)}. Wo lag er am Anfang?',
                'Geh die Wege rückwärts: Was zuletzt passiert ist, machst du zuerst rückgängig – in die andere Richtung.',
                f'Rückwärts: von {z(ende)} um {li} nach rechts: {z(ende + li)}. Dann um {re_} nach links: {z(anf)}. '
                f'Probe: {z(anf)} + {re_} − {li} = {z(ende)}.',
                o={'wert': anf}, c=f'({ende}) + {li} - {re_}'))
    # 6 · Stufe 3 · begruenden · auswahl
    a_, o_ = auswahl('Nein. Das Spiegeln an der 0 vertauscht die Seiten: −a liegt dann rechts von −b.',
                     ['Ja, das gilt immer.', 'Nur wenn a und b beide negativ sind.', 'Nur wenn a und b beide positiv sind.'], 1)
    A.append(ue(L, T, 3, 'begruenden', 'auswahl',
                'Stimmt die Aussage? „Liegt a auf der Zahlengeraden links von b, dann liegt auch −a links von −b.“',
                'Probiere es mit zwei Zahlen aus, zum Beispiel a = 2 und b = 5. Wo liegen −2 und −5?',
                '2 liegt links von 5, aber −2 liegt rechts von −5. Gegenzahlen sind an der 0 gespiegelt; dabei werden links und rechts vertauscht.',
                a=a_, o=o_))
    # 7 · Stufe 3 · parameter · zahl
    m = -3
    a_wert = Fr(2 * m, 3)  # (a + 2a) / 2 = m
    assert a_wert.denominator == 1
    a_wert = int(a_wert)
    A.append(ue(L, T, 3, 'parameter', 'zahl',
                f'Für welche Zahl a liegt {z(m)} genau in der Mitte zwischen a und 2 · a?',
                'Die Mitte zweier Zahlen ist ihre Summe geteilt durch 2. Stelle damit eine Gleichung für a auf.',
                f'Mitte: (a + 2a) : 2 = 3a : 2 = {z(m)}. Also 3a = {z(2 * m)} und a = {z(a_wert)}. '
                f'Probe: zwischen {z(a_wert)} und {z(2 * a_wert)} liegt {z(m)} in der Mitte.',
                o={'wert': a_wert}, c=f'2 * ({m}) / 3'))
    # 8 · Stufe 3 · fehler · auswahl
    p, q = -18, 6
    mitte = (p + q) // 2
    a_, o_ = auswahl(f'Das Minus von {z(p)} fehlt. Richtig ist ({z(p)} + {q}) : 2 = {z(mitte)}.',
                     [f'Man muss subtrahieren: ({-p} − {q}) : 2 = {(-p - q) // 2}.', 'Nichts, 12 stimmt.', 'Man muss durch 3 teilen, nicht durch 2.'], 3)
    A.append(ue(L, T, 3, 'fehler', 'auswahl',
                f'Jemand sucht die Mitte zwischen {z(p)} und {q} und rechnet: ({-p} + {q}) : 2 = {(-p + q) // 2}. Was ist falsch?',
                'Kann die Mitte zwischen einer negativen und einer kleineren positiven Zahl größer als beide sein?',
                f'Die Mitte muss zwischen {z(p)} und {q} liegen; 12 liegt rechts von beiden. Mit dem Vorzeichen: ({z(p)} + {q}) : 2 = {z(mitte)}.',
                a=a_, o=o_))
    return A


# ---------------------------------------------------------------- zahlen.ganz · ordnen
def ordnen():
    L, T = 'ordnen', 'ordnen'
    A = []
    # 1 · Stufe 2 · einkleidung · zahl
    st = {'Januar': -35, 'Februar': 12, 'März': -80, 'April': -5}
    tief = min(st.values())
    A.append(ue(L, T, 2, 'einkleidung', 'zahl',
                'Kontostand am Monatsende: ' + ', '.join(f'{m} {z(v)} €' for m, v in st.items()) + '. Wie hoch war der niedrigste Kontostand?',
                'Der niedrigste Stand ist die kleinste Zahl. Bei negativen Zahlen: Je weiter weg von 0, desto kleiner.',
                f'Negativ sind {", ".join(z(v) for v in st.values() if v < 0)}. Am weitesten von 0 entfernt ist {z(tief)}. '
                f'Also ist {z(tief)} € der niedrigste Stand.',
                o={'wert': tief, 'einheit': '€'}, c='min(-35, 12, -80, -5)'))
    # 2 · Stufe 2 · mehrschritt · auswahl
    zs = [-6, 4, -15, 0, -1]
    gr = sorted(zs, reverse=True)
    kette = lambda xs: ' > '.join(z(x) for x in xs)
    nach_betrag = [4, 0] + sorted([x for x in zs if x < 0], key=abs, reverse=True)   # Fehler: negative nach Betrag geordnet
    a_, o_ = auswahl(kette(gr), [kette(nach_betrag), kette(sorted(zs)), kette([4, -1, 0, -6, -15])], 0)
    A.append(ue(L, T, 2, 'mehrschritt', 'auswahl',
                'Ordne ' + ', '.join(z(x) for x in zs) + ' von der größten zur kleinsten Zahl. Welche Reihe stimmt?',
                'Zuerst die positiven Zahlen, dann die 0, dann die negativen: Bei ihnen kommt die mit dem kleinsten Betrag zuerst.',
                f'Positiv: 4. Dann 0. Negativ, von nah an 0 nach weit weg: −1, −6, −15. Also {kette(gr)}.',
                a=a_, o=o_))
    # 3 · Stufe 2 · umkehr · zahl
    a0, n = -14, 5
    b = a0 + n + 1
    A.append(ue(L, T, 2, 'umkehr', 'zahl',
                f'Zwischen {z(a0)} und einer größeren ganzen Zahl b liegen genau {n} ganze Zahlen. Welche Zahl ist b?',
                'Zähle von der ersten Zahl aus nach rechts weiter, ohne sie selbst mitzuzählen.',
                f'Dazwischen liegen {", ".join(z(x) for x in range(a0 + 1, b))} – das sind {n}. Die nächste Zahl ist b = {z(b)}.',
                o={'wert': b}, c=f'({a0}) + {n} + 1'))
    # 4 · Stufe 2 · darstellung · auswahl
    werte = [-2, -11, 5]
    mitte = sorted(werte)[1]
    a_, o_ = auswahl(z(mitte), [z(-11), z(5), 'Das kann man nicht sagen.'], 1)
    A.append(ue(L, T, 2, 'darstellung', 'auswahl',
                'Auf einer Zahlengeraden liegen die Punkte A, B und C von links nach rechts. Zu ihnen gehören die Zahlen '
                + ', '.join(z(x) for x in werte) + ' – nicht unbedingt in dieser Reihenfolge. Welche Zahl gehört zu B?',
                'Links liegt die kleinste Zahl. B ist der mittlere Punkt.',
                f'Geordnet: {" < ".join(z(x) for x in sorted(werte))}. A = {z(sorted(werte)[0])}, B = {z(mitte)}, C = {z(sorted(werte)[2])}.',
                a=a_, o=o_))
    # 5 · Stufe 3 · transfer · zahl
    stand = [-12, -30, 4, -7]
    platz = sorted(stand).index(-7) + 1
    plaetze = [f'Platz {i}' for i in range(1, 5)]
    a_ = plaetze
    o_ = {'index': platz - 1}
    assert plaetze[platz - 1] == 'Platz 3'
    A.append(ue(L, T, 3, 'transfer', 'auswahl',
                'Bei einem Spiel gewinnt, wer am Ende den kleinsten Punktestand hat. Die Endstände sind '
                + ', '.join(z(x) for x in stand) + '. Auf welchem Platz landet der Spieler mit −7 Punkten?',
                'Platz 1 hat die kleinste Zahl. Ordne alle Stände von klein nach groß.',
                f'Von klein nach groß: {" < ".join(z(x) for x in sorted(stand))}. −7 steht an Stelle {platz}, also Platz {platz}.',
                a=a_, o=o_))
    # 6 · Stufe 3 · begruenden · auswahl
    a_, o_ = auswahl('Ja. Negative Zahlen liegen links von 0, positive rechts davon.',
                     ['Nein: −100 ist größer als 1, weil 100 größer ist als 1.', 'Nur wenn die negative Zahl den kleineren Betrag hat.',
                      'Nein: −5 und 5 sind gleich groß, weil sie denselben Betrag haben.'], 2)
    A.append(ue(L, T, 3, 'begruenden', 'auswahl',
                'Stimmt die Aussage? „Jede negative Zahl ist kleiner als jede positive Zahl.“',
                'Denk an die Zahlengerade: Wo liegen negative, wo positive Zahlen – und wo die 0?',
                'Alle negativen Zahlen liegen links von 0, alle positiven rechts. Links bedeutet kleiner. Die Aussage stimmt; der Betrag spielt beim Vergleich mit 0 keine Rolle.',
                a=a_, o=o_))
    # 7 · Stufe 3 · parameter · zahl
    lo, hi = -9, -3
    groesst = hi - 1
    A.append(ue(L, T, 3, 'parameter', 'zahl',
                f'a ist eine ganze Zahl mit {z(lo)} < a < {z(hi)}. Welchen Wert kann a höchstens haben?',
                f'a muss kleiner als {z(hi)} sein. Welche ganze Zahl kommt direkt links von {z(hi)}?',
                f'Möglich sind {", ".join(z(x) for x in range(lo + 1, hi))}. Die größte davon ist {z(groesst)}.',
                o={'wert': groesst}, c=f'({hi}) - 1'))
    # 8 · Stufe 3 · fehler · auswahl
    a_, o_ = auswahl('−12 °C und −7 °C sind vertauscht.',
                     ['4 °C und −1 °C sind vertauscht.', '−1 °C und −12 °C sind vertauscht.', 'Alles ist richtig geordnet.'], 1)
    A.append(ue(L, T, 3, 'fehler', 'auswahl',
                'Eine Liste soll Temperaturen von warm nach kalt ordnen: 4 °C, −1 °C, −12 °C, −7 °C. Wo steckt der Fehler?',
                'Prüfe jedes Paar nebeneinander: Ist die erste Temperatur wirklich wärmer als die zweite?',
                '4 > −1 stimmt, −1 > −12 stimmt, aber −12 > −7 stimmt nicht: −7 °C ist wärmer. Richtig: 4 °C, −1 °C, −7 °C, −12 °C.',
                a=a_, o=o_))
    return A


# ---------------------------------------------------------------- gleichungen.linear · waage
def waage():
    L, T = 'waage', 'umformen'
    A = []
    # 1 · Stufe 2 · einkleidung · zahl
    n, verp, ges = 5, 300, 2300
    x = (ges - verp) // n
    assert n * x + verp == ges
    A.append(ue(L, T, 2, 'einkleidung', 'zahl',
                f'Ein Paket mit {n} gleich schweren Büchern wiegt zusammen mit der Verpackung von {verp} g genau 2,3 kg. Wie viel Gramm wiegt ein Buch?',
                'Rechne 2,3 kg in Gramm um und stelle eine Gleichung auf: Bücher plus Verpackung ergeben das Gesamtgewicht.',
                f'2,3 kg = {ges} g. Gleichung: {n}x + {verp} = {ges}. | − {verp}: {n}x = {ges - verp}. | : {n}: x = {x}. Ein Buch wiegt {x} g.',
                o={'wert': x, 'einheit': 'g'}, c=f'({ges} - {verp}) / {n}'))
    # 2 · Stufe 2 · darstellung · auswahl
    a_, o_ = auswahl('2x + 3 = 11', ['2x = 11 + 3', '2 + 3x = 11', 'x + 3 = 11'], 2)
    A.append(ue(L, T, 2, 'darstellung', 'auswahl',
                'Auf der linken Waagschale liegen 2 gleiche Dosen und 3 Ein-Kilo-Gewichte, auf der rechten 11 Ein-Kilo-Gewichte. '
                'Die Waage ist im Gleichgewicht. Welche Gleichung passt, wenn x das Gewicht einer Dose in kg ist?',
                'Schreibe auf, was links liegt, und setze es gleich dem, was rechts liegt.',
                'Links: 2 Dosen = 2x, dazu 3 kg. Rechts: 11 kg. Also 2x + 3 = 11 (und damit x = 4).',
                a=a_, o=o_))
    # 3 · Stufe 2 · umkehr · zahl
    lsg, plus, rechts = -6, 5, -19
    faktor = Fr(rechts - plus, lsg)
    assert faktor.denominator == 1
    faktor = int(faktor)
    A.append(ue(L, T, 2, 'umkehr', 'zahl',
                f'Die Gleichung □ · x + {plus} = {z(rechts)} hat die Lösung x = {z(lsg)}. Welche Zahl steht im Kästchen?',
                f'Setze x = {z(lsg)} ein. Dann bleibt eine Gleichung, in der nur noch die Zahl im Kästchen fehlt.',
                f'□ · {k(lsg)} + {plus} = {z(rechts)}. | − {plus}: □ · {k(lsg)} = {z(rechts - plus)}. | : {k(lsg)}: □ = {z(faktor)}. '
                f'Probe: {faktor} · {k(lsg)} + {plus} = {z(faktor * lsg + plus)} ✓',
                o={'wert': faktor}, c=f'(({rechts}) - {plus}) / ({lsg})'))
    # 4 · Stufe 2 · mehrschritt · zahl
    x = (5 + 4) / 1.5
    A.append(ue(L, T, 2, 'mehrschritt', 'zahl',
                'Welchen Wert hat x, wenn 1,5x − 4 = 5 gilt?',
                'Erst die Zahl ohne x auf die andere Seite bringen, dann durch die Zahl vor dem x teilen.',
                f'| + 4: 1,5x = 9. | : 1,5: x = {z(x)}. Probe: 1,5 · {z(x)} − 4 = 5 ✓',
                o={'wert': int(x)}, c='(5 + 4) / 1.5'))
    # 5 · Stufe 3 · fehler · auswahl
    a, b, c = 5, 12, -3
    x = Fr(c - b, a)
    a_, o_ = auswahl(f'Falsch gerechnet: {z(c)} − {b} = {z(c - b)}, nicht 9. Richtig ist x = {z(x)}.',
                     ['Man hätte zuerst durch 5 teilen müssen.', '9 : 5 ist nicht 1,8.', 'Es ist kein Fehler drin.'], 0)
    A.append(ue(L, T, 3, 'fehler', 'auswahl',
                f'Jemand löst {a}x + {b} = {z(c)} so: „| − {b}: {a}x = 9. | : {a}: x = 1,8.“ Wo steckt der Fehler?',
                'Mach die Probe mit x = 1,8 in der ursprünglichen Gleichung. Prüfe dann jeden Schritt einzeln.',
                f'Probe: 5 · 1,8 + 12 = 21, nicht −3. Der Fehler: {z(c)} − {b} ist {z(c - b)}. Dann 5x = {z(c - b)} und x = {z(x)}.',
                a=a_, o=o_))
    # 6 · Stufe 3 · verknuepfen · zahl (Prozent aus Klasse 6)
    x = (36 + 4) / Fr(8, 10)
    assert x.denominator == 1
    A.append(ue(L, T, 3, 'verknuepfen', 'zahl',
                'Ein Preis wird um 20 % gesenkt, danach werden noch 4 € abgezogen. Jetzt kostet die Ware 36 €. Wie viel kostete sie vorher?',
                'Nach 20 % Rabatt bleiben 80 % vom Preis, also 0,8 · x. Stelle damit eine Gleichung auf.',
                f'0,8x − 4 = 36. | + 4: 0,8x = 40. | : 0,8: x = {z(x)}. Probe: 80 % von {z(x)} € sind 40 €, minus 4 € = 36 € ✓',
                o={'wert': int(x), 'einheit': '€'}, c='(36 + 4) / 0.8'))
    # 7 · Stufe 3 · begruenden · auswahl
    a_, o_ = auswahl('Nein. Dann steht auf beiden Seiten 0, und jede Zahl würde passen – die Lösung geht verloren.',
                     ['Ja, das ist eine Äquivalenzumformung wie jede andere.', 'Ja, aber nur, wenn x negativ ist.',
                      'Nein, weil man bei Gleichungen nur addieren und subtrahieren darf.'], 3)
    A.append(ue(L, T, 3, 'begruenden', 'auswahl',
                'Darf man beim Lösen einer Gleichung beide Seiten mit 0 multiplizieren?',
                'Probiere es an 2x = 6 aus. Was steht nach dem Multiplizieren mit 0 da, und welche Zahlen erfüllen das?',
                '2x = 6 hat die Lösung 3. Mal 0 ergibt 0 = 0 – das gilt für jede Zahl. Die Umformung verändert also die Lösungsmenge; mit 0 multiplizieren ist keine Äquivalenzumformung.',
                a=a_, o=o_))
    # 8 · Stufe 3 · transfer · zahl
    grund, je, summe = 900, 15, 1440   # in Cent
    x = (summe - grund) // je
    assert grund + je * x == summe
    A.append(ue(L, T, 3, 'transfer', 'zahl',
                'Ein Handytarif kostet 9 € Grundgebühr im Monat und 15 Cent je Minute. Im März waren es 14,40 €. Wie viele Minuten wurde telefoniert?',
                'Stelle eine Gleichung auf: Grundgebühr plus Minuten mal Preis je Minute ergibt den Betrag. Rechne am besten in Cent.',
                f'In Cent: {grund} + {je}x = {summe}. | − {grund}: {je}x = {summe - grund}. | : {je}: x = {x}. Es waren {x} Minuten.',
                o={'wert': x}, c=f'({summe} - {grund}) / {je}'))
    return A


NEU = {'zahlen.ganz': {'zahlengerade': zahlengerade, 'ordnen': ordnen}, 'gleichungen.linear': {'waage': waage}}


def _schluessel(a):
    return (a['f']['text'], json.dumps(a.get('a'), ensure_ascii=False))


def frisch_anhaengen(thema):
    """Hängt die frischen Übungen an die fertige Themen-Datei an (zweiter Lauf hängt nichts doppelt an)."""
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    da = {_schluessel(a) for a in d['aufgaben']}
    neu = 0
    for lz, fn in NEU[thema].items():
        for a in fn():
            if _schluessel(a) in da:
                continue
            d['aufgaben'].append(a)
            da.add(_schluessel(a))
            neu += 1
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'  FRISCH {thema}: {neu} neue Übungen angehängt')
