#!/usr/bin/env python3
"""Thema gleichungen.ungleichungen – Lineare Ungleichungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, M, Z, baue, bruch, cz, eur, grenze, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.ungleichungen', 'thema_id': 3, 'block_id': 61, 'klasse': {'gym_by': 8, 'rs_by': 7}}

UMKEHR = {'<': '>', '>': '<', '≤': '≥', '≥': '≤'}
ZEICHEN = ['<', '>', '≤', '≥']

ETAPPEN = [
    {'lernziel': 'umformen', 'titel': 'Ungleichungen umformen',
     'regel': 'Eine Ungleichung löst du wie eine Gleichung: Auf beiden Seiten ⟦dasselbe addieren, subtrahieren⟧ oder mit einer ⟦positiven⟧ Zahl multiplizieren bzw. durch sie dividieren. Das Zeichen bleibt dabei gleich.',
     'schritte': ['3x + 5 < 17   | − 5', '3x < 12   | : 3', '⟦x < 4⟧: Alle Zahlen kleiner als 4 sind Lösungen.'],
     'probe': 'x = 0: 3 · 0 + 5 = 5 < 17 ✓  x = 4: 17 < 17 ✗ – 4 gehört nicht dazu.',
     'fehler': 'Aus 3x + 5 < 17 wird nicht 3x < 22: Die 5 wird ⟦subtrahiert⟧, nicht addiert. Richtig ist 3x < 12.',
     'bild': {'typ': 'zahlenstrahl', 'start': -2, 'ende': 8, 'abschnitte': 10, 'beschriftet': 'anfang_ende', 'pfeil': 6},
     '_verbot': ['3x + 5 < 17']},
    {'lernziel': 'umdrehen', 'titel': 'Mal negative Zahl: Zeichen umdrehen',
     'regel': 'Multiplizierst oder dividierst du beide Seiten mit einer ⟦negativen⟧ Zahl, musst du das Zeichen ⟦umdrehen⟧: aus < wird >, aus ≤ wird ≥. Warum? 2 < 3 ist wahr. Mal (−1): −2 und −3. Jetzt ist −2 > −3 – bei −2 °C ist es wärmer als bei −3 °C. Das Minus spiegelt alles an der 0, die Reihenfolge kehrt sich um.',
     'schritte': ['−2x + 1 ≤ 9   | − 1', '−2x ≤ 8   | : (−2), Zeichen umdrehen', '⟦x ≥ −4⟧'],
     'probe': 'x = 0: −2 · 0 + 1 = 1 ≤ 9 ✓ – und 0 ≥ −4 passt.',
     'fehler': '−2x ≤ 8 ergibt nicht x ≤ −4. Prüfe mit x = −5: −2 · (−5) = 10 ≤ 8 ist falsch. Beim Teilen durch (−2) wird das Zeichen ⟦umgedreht⟧: x ≥ −4. Aber Achtung: Beim ⟦Subtrahieren⟧ einer Zahl, z. B. | − 1, dreht sich nichts um.',
     '_verbot': ['−2x + 1 ≤ 9']},
    {'lernziel': 'klammern', 'titel': 'Klammern und x auf beiden Seiten',
     'regel': 'Erst ⟦Klammern auflösen⟧ und zusammenfassen, dann alle x-Glieder auf ⟦eine Seite⟧ bringen. Hat x am Ende einen negativen Faktor, Zeichen beim Teilen umdrehen.',
     'schritte': ['2(x + 3) > 5x − 9', '2x + 6 > 5x − 9   | − 5x − 6', '−3x > −15   | : (−3), Zeichen umdrehen', '⟦x < 5⟧'],
     'probe': 'x = 0: 2 · 3 = 6 > −9 ✓',
     'fehler': '2(x + 3) ist nicht 2x + 3: Die 2 wird mit ⟦jedem⟧ Summanden in der Klammer multipliziert, also 2x + 6.',
     '_verbot': ['2(x + 3) > 5x − 9']},
    {'lernziel': 'intervall', 'titel': 'Lösungsmenge als Intervall angeben',
     'regel': 'Die Lösungsmenge schreibst du als Intervall. Eckige Klammer ⟦nach innen⟧: Grenze gehört dazu (≤, ≥). Klammer ⟦nach außen⟧: Grenze gehört nicht dazu (<, >). Bei ∞ steht immer eine Klammer nach außen.',
     'schritte': ['x ≤ 3 → L = ⟦]−∞; 3]⟧', 'x > −2 → L = ⟦]−2; ∞[⟧'],
     'fehler': 'x < 3 ist nicht ]−∞; 3]: Die 3 erfüllt x < 3 nicht, also muss die Klammer ⟦nach außen⟧ zeigen: ]−∞; 3[.'},
    {'lernziel': 'pruefen', 'titel': 'Lösungen prüfen und Fehler finden',
     'regel': 'Ob eine Zahl eine Lösung ist, prüfst du durch ⟦Einsetzen⟧. Bei einer Rechnung prüfst du jeden Schritt, besonders das ⟦Umdrehen des Zeichens⟧.',
     'schritte': ['Ist 6 eine Lösung von 2x − 3 > 7?', '2 · 6 − 3 = 9 und 9 > 7 ist wahr, also ⟦ja⟧.'],
     'fehler': 'Nur eine Zahl zu testen reicht nicht, um eine ganze Lösungsmenge zu bestätigen. Teste auch eine Zahl ⟦nahe der Grenze⟧ auf der anderen Seite.',
     '_verbot': ['2x − 3 > 7']},
    {'lernziel': 'grafisch', 'titel': 'Ungleichung am Graphen lösen',
     'regel': 'Zeichne jede Seite als Gerade. Bei „links < rechts“ suchst du die x-Werte, bei denen die linke Gerade ⟦unterhalb⟧ der rechten liegt. Die Grenze ist der ⟦Schnittpunkt⟧.',
     'schritte': ['3x + 5 < 17. Links: y = 3x + 5. Rechts: y = 17, eine waagrechte Gerade.', 'Die Geraden schneiden sich bei x = 4.',
                  'Links vom Schnittpunkt liegt y = 3x + 5 unter der 17: ⟦x < 4⟧.'],
     'probe': 'x = 2: 3 · 2 + 5 = 11 < 17 ✓',
     'fehler': 'Die falsche Seite nehmen: Rechts vom Schnittpunkt liegt die Gerade y = 3x + 5 ⟦über⟧ der 17. Bei „<“ gehört der Bereich ⟦unterhalb⟧ dazu, also links von x = 4.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [0, 22],
              'graphen': [{'art': 'linear', 'm': 3, 't': 5, 'name': 'y = 3x + 5'}, {'art': 'linear', 'm': 0, 't': 17, 'name': 'y = 17'}],
              'senkrecht': [4], 'punkte': [{'x': 4, 'y': 17, 'offen': True}]}},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit Ungleichungen',
     'regel': 'Wörter wie ⟦höchstens⟧ (≤), ⟦mindestens⟧ (≥), ⟦mehr als⟧ (>) oder ⟦weniger als⟧ (<) führen zu einer Ungleichung. Bei Stückzahlen ist nur eine ⟦ganze Zahl⟧ als Antwort sinnvoll.',
     'schritte': ['Eintritt 4 €, jede Fahrt 2,50 €, höchstens 20 € ausgeben.', '4 + 2,5x ≤ 20  →  2,5x ≤ 16  →  x ≤ 6,4', 'Man kann ⟦höchstens 6⟧ Fahrten machen.'],
     'fehler': 'Aus x ≤ 6,4 folgt nicht „7 Fahrten“ durch Aufrunden: 7 Fahrten kosten 4 + 17,50 = 21,50 €, das ist zu viel. Bei „höchstens“ wird ⟦abgerundet⟧.'},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'umformen': {
  'einstieg': 'Im Freizeitpark kostet der Eintritt 5 €, jede Fahrt kostet 3 €. Du hast 17 € dabei und willst danach noch etwas Geld übrig haben. Wie viele Fahrten sind drin? Es muss nicht genau aufgehen – du musst nur unter 17 € bleiben. Eine Rechenfrage mit „weniger als“ statt „gleich“ heißt ⟦Ungleichung⟧.',
  'woerter': [['Ungleichung', 'wie eine Gleichung, aber mit <, >, ≤ oder ≥ statt mit ='], ['<', '„kleiner als“, z. B. 3 < 5'], ['>', '„größer als“, z. B. 5 > 3'],
              ['x', 'die gesuchte Zahl – hier die Anzahl der Fahrten'], ['Lösung', 'jede Zahl für x, mit der die Aussage stimmt'],
              ['| − 5', 'Randnotiz: Im nächsten Schritt wird auf beiden Seiten 5 abgezogen']],
  'schritte': ['Die Frage als Ungleichung: 5 € Eintritt plus 3 € je Fahrt soll weniger als 17 € sein, also 3x + 5 < 17.',
               'Auf beiden Seiten 5 abziehen, denn der Eintritt ist schon bezahlt: 3x < 12.',
               'Beide Seiten durch 3 teilen, den Preis einer Fahrt: x < 4.',
               'Alle Zahlen kleiner als 4 sind Lösungen: ⟦x < 4⟧. Fahrten gibt es nur ganz, also höchstens 3.'],
  'regel': 'So löst du eine ⟦Ungleichung⟧: wie eine Gleichung umformen. Auf beiden Seiten ⟦dasselbe addieren oder abziehen⟧ oder mit derselben ⟦positiven⟧ Zahl malnehmen bzw. durch sie teilen – das Zeichen bleibt dabei gleich.',
  'fehler': 'Aus 3x + 5 < 17 wird nicht 3x < 22. Das wäre, als würdest du den bezahlten Eintritt noch einmal zu deinem Geld dazulegen. Die 5 wird auf beiden Seiten ⟦abgezogen⟧: 3x < 12.'},
 'umdrehen': {
  'einstieg': 'Schau aufs Thermometer: 2 °C ist kälter als 3 °C, also 2 < 3. Jetzt dieselben Zahlen mit Minus: Bei −3 °C ist es kälter als bei −2 °C, also −2 > −3. Das Minus hat die Reihenfolge umgekehrt. Darum muss man beim Malnehmen oder Teilen mit einer ⟦negativen Zahl⟧ das Zeichen umdrehen.',
  'woerter': [['negative Zahl', 'eine Zahl unter 0 mit Minus davor, z. B. −2 oder −3,5'], ['≤', '„kleiner oder gleich“, also höchstens'], ['≥', '„größer oder gleich“, also mindestens'],
              ['Zeichen umdrehen', 'aus < wird >, aus ≤ wird ≥ – und umgekehrt']],
  'schritte': ['Aufgabe: −2x + 1 ≤ 9.', 'Auf beiden Seiten 1 abziehen: −2x ≤ 8. Beim Abziehen bleibt das Zeichen, wie es ist.',
               'Beide Seiten durch (−2) teilen. Weil −2 negativ ist, wird aus ≤ ein ≥.', 'Ergebnis: ⟦x ≥ −4⟧. Alle Zahlen ab −4 aufwärts sind Lösungen.'],
  'regel': 'So gehst du vor: Teilst du beide Seiten durch eine ⟦negative Zahl⟧ oder nimmst du sie damit mal, ⟦drehst du das Zeichen um⟧: < wird >, ≤ wird ≥. Beim Addieren und Abziehen bleibt es, wie es ist.',
  'fehler': '−2x ≤ 8 ergibt nicht x ≤ −4. Prüfe mit x = −5: −2 · (−5) = 10, und 10 ≤ 8 ist falsch. Ohne Umdrehen wäre es wie beim Thermometer, auf dem −3 °C plötzlich wärmer als −2 °C sein soll. Richtig: ⟦x ≥ −4⟧. Beim Abziehen, z. B. | − 1, dreht sich nichts um.'},
 'klammern': {
  'einstieg': 'Zwei Freunde gehen ins Kino. Jeder zahlt den Eintritt x € und eine Cola für 3 €. Zusammen zahlen sie 2 · (x + 3) € – die 2 gilt für den Eintritt und für die Cola. Will man das mit einem anderen Preis vergleichen, muss man zuerst die ⟦Klammer auflösen⟧ und dann alle x auf eine Seite bringen.',
  'woerter': [['Klammer auflösen', 'die Zahl vor der Klammer mit jedem Teil darin malnehmen: 2(x + 3) = 2x + 6'], ['2(x + 3)', 'kurz für 2 · (x + 3)'],
              ['x-Glied', 'ein Teil mit x, z. B. 5x'], ['Faktor vor x', 'die Zahl, mit der x malgenommen wird: in −3x ist es −3']],
  'schritte': ['Aufgabe: 2(x + 3) > 5x − 9.', 'Klammer auflösen: 2 mal x und 2 mal 3 ergibt 2x + 6 > 5x − 9.',
               'Alle x nach links, alle Zahlen nach rechts: Auf beiden Seiten 5x und 6 abziehen ergibt −3x > −15.',
               'Durch −3 teilen. −3 ist negativ, also Zeichen umdrehen: ⟦x < 5⟧.'],
  'regel': 'So gehst du vor: zuerst ⟦Klammern auflösen⟧ und zusammenfassen, dann alle ⟦x-Glieder auf eine Seite⟧ und alle Zahlen auf die andere. Ist der Faktor vor x am Ende negativ, beim Teilen das Zeichen umdrehen.',
  'fehler': '2(x + 3) ist nicht 2x + 3. Das wäre, als hätten die beiden Freunde zwei Eintritte, aber nur eine Cola bezahlt. Die 2 gilt für ⟦jeden⟧ Teil in der Klammer: 2x + 6.'},
 'intervall': {
  'einstieg': 'An einer Achterbahn steht: „Mitfahren ab 1,20 m Körpergröße.“ Erlaubt sind also 1,20 m und alle Größen darüber – ein ganzer Bereich ohne Lücken. Statt „alle Zahlen ab 1,2“ schreibt man kurz [1,2; ∞[. So ein lückenloser Zahlenbereich heißt ⟦Intervall⟧.',
  'woerter': [['Lösungsmenge L', 'alle Lösungen zusammen'], ['Intervall', 'ein lückenloser Zahlenbereich, z. B. alle Zahlen von 2 bis 5'],
              ['[ … ]', 'zeigt die eckige Klammer zur Zahl hin (nach innen), gehört die Grenze dazu'], ['] … [', 'zeigt sie von der Zahl weg (nach außen), gehört die Grenze nicht dazu'],
              ['∞', '„unendlich“: ohne Ende nach oben; −∞: ohne Ende nach unten']],
  'schritte': ['x ≤ 3 heißt: die 3 und alle Zahlen darunter.', 'Nach unten gibt es kein Ende, also beginnt der Bereich bei −∞. Dort zeigt die Klammer immer nach außen.',
               'Die 3 gehört dazu, also zeigt die Klammer bei der 3 nach innen: L = ⟦]−∞; 3]⟧.',
               'Genauso: x > −2 heißt „alles über −2, aber nicht −2 selbst“: L = ⟦]−2; ∞[⟧.'],
  'regel': 'So schreibst du die Lösungsmenge als ⟦Intervall⟧: Gehört die Grenze dazu (≤, ≥), zeigt die Klammer ⟦nach innen⟧. Gehört sie nicht dazu (<, >), zeigt sie ⟦nach außen⟧. Bei ∞ und −∞ zeigt sie immer nach außen.',
  'fehler': 'x < 3 ist nicht ]−∞; 3]. Das wäre wie das Schild „Eintritt frei unter 3 Jahren“, an der Kasse aber auch Dreijährige frei durchlassen. Die 3 erfüllt x < 3 nicht, also Klammer ⟦nach außen⟧: ]−∞; 3[.'},
 'pruefen': {
  'einstieg': 'Du hast ausgerechnet, dass im Freizeitpark höchstens 3 Fahrten drin sind. Bevor du an der Kasse stehst, rechnest du lieber nach: 5 € Eintritt und 3 Fahrten zu 3 € sind 14 € – das passt. So ein Nachrechnen mit einer eingesetzten Zahl heißt ⟦Probe⟧.',
  'woerter': [['einsetzen', 'für x eine Zahl hinschreiben und ausrechnen'], ['Probe', 'Nachrechnen, ob eine Zahl wirklich passt'], ['Aussage stimmt', 'z. B. 9 > 7 – das ist wahr']],
  'schritte': ['Frage: Ist 6 eine Lösung von 2x − 3 > 7?', 'Setze 6 für x ein: 2 · 6 − 3 = 12 − 3 = 9.', 'Vergleiche mit der rechten Seite: Ist 9 > 7? Ja, das stimmt.',
               'Also: ⟦Ja, 6 ist eine Lösung.⟧'],
  'regel': 'So prüfst du: Zahl für x ⟦einsetzen⟧, ausrechnen und schauen, ob die Aussage ⟦stimmt⟧. Bei einer fremden Rechnung jeden Schritt nachrechnen – besonders, ob beim Teilen durch eine negative Zahl das Zeichen umgedreht wurde.',
  'fehler': 'Eine passende Zahl bestätigt noch nicht die ganze Lösung. Wer nur „0 Fahrten“ testet, merkt nicht, ob 4 Fahrten auch noch gingen. Teste auch eine Zahl ⟦nahe der Grenze⟧, auf beiden Seiten.'},
 'grafisch': {
  'einstieg': 'Statt zu rechnen kannst du auch zeichnen: eine Linie für deine Ausgaben im Freizeitpark (5 € Eintritt plus 3 € je Fahrt) und eine waagrechte Linie bei 17 € für dein Geld. Solange die Ausgaben-Linie unter der Geld-Linie liegt, reicht das Geld. Wo sich die Linien treffen, liegt die Grenze – am ⟦Schnittpunkt⟧.',
  'woerter': [['Gerade', 'eine gerade Linie im Koordinatensystem, z. B. y = 3x + 5'], ['y = 17', 'eine waagrechte Gerade: überall auf der Höhe 17'],
              ['unterhalb', 'die Linie liegt tiefer, ihre Werte sind kleiner'], ['Schnittpunkt', 'die Stelle, an der sich zwei Linien treffen']],
  'schritte': ['Aufgabe: 3x + 5 < 17.', 'Zeichne die linke Seite als Gerade y = 3x + 5 und die rechte Seite als waagrechte Gerade y = 17.',
               'Die Geraden schneiden sich bei x = 4, denn 3 · 4 + 5 = 17.', 'Links von x = 4 liegt y = 3x + 5 unterhalb der 17. Also ⟦x < 4⟧.'],
  'regel': 'So löst du eine Ungleichung am Bild: Jede Seite als ⟦Gerade⟧ zeichnen. Bei „links < rechts“ die x-Werte suchen, bei denen die linke Gerade ⟦unterhalb⟧ der rechten liegt. Die Grenze ist die x-Stelle des ⟦Schnittpunkts⟧.',
  'fehler': 'Die falsche Seite nehmen: Rechts vom Schnittpunkt liegt y = 3x + 5 ⟦über⟧ der 17 – dort wären die Ausgaben höher als dein Geld. Bei „<“ gehört der Bereich ⟦unterhalb⟧ dazu, also links von x = 4.'},
 'sachaufgabe': {
  'einstieg': 'In einem anderen Park kostet der Eintritt 4 €, jede Fahrt 2,50 €, und du willst höchstens 20 € ausgeben. Wörter wie „höchstens“, „mindestens“, „mehr als“ oder „weniger als“ verraten: Gesucht ist kein einzelner Wert, sondern ein ganzer Bereich. Solche Texte übersetzt du in eine Ungleichung – das ist eine ⟦Sachaufgabe⟧.',
  'woerter': [['höchstens', 'nicht mehr als: ≤'], ['mindestens', 'nicht weniger als: ≥'], ['mehr als / weniger als', '> bzw. < – die Grenze selbst zählt nicht'],
              ['abrunden', 'zur nächstkleineren ganzen Zahl gehen, z. B. 6,4 → 6']],
  'schritte': ['Übersetzen: 4 € Eintritt plus 2,50 € je Fahrt dürfen höchstens 20 € sein, also 4 + 2,5x ≤ 20.', 'Auf beiden Seiten 4 abziehen: 2,5x ≤ 16.',
               'Beide Seiten durch 2,5 teilen: x ≤ 6,4.', 'Fahrten gibt es nur ganz, und 7 wären zu viel. Also abrunden: ⟦höchstens 6 Fahrten⟧.'],
  'regel': 'So übersetzt du: ⟦höchstens⟧ → ≤, ⟦mindestens⟧ → ≥, ⟦mehr als⟧ → >, ⟦weniger als⟧ → <. Dann die Ungleichung lösen und prüfen, ob nur ⟦ganze Zahlen⟧ sinnvoll sind.'},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def loese(p, q, z, r, s):
    """p·x + q  z  r·x + s  ->  (Zeichen, Grenze)."""
    k = p - r
    g = Fr(s - q, k)
    return (z if k > 0 else UMKEHR[z]), g


def falsch_loesungen(z, g):
    return [f'x {UMKEHR[z]} {zt(g)}', f'x {z} {zt(-g)}' if g != 0 else f'x {z} 1', f'x {UMKEHR[z]} {zt(-g)}' if g != 0 else f'x {UMKEHR[z]} 1',
            f'x {z.replace("≤", "<").replace("≥", ">") if z in "≤≥" else {"<": "≤", ">": "≥"}[z]} {zt(g)}']


def text_ug(p, q, z, r, s):
    return f'{lin(p, q)} {z} {lin(r, s)}'


def g_umformen(R, st):
    z = R.choice(ZEICHEN)
    if st == 1:
        a, g = R.randint(2, 9), R.randint(-6, 9)
        if R.random() < .5:
            b = R.randint(1, 15) * R.choice([-1, 1])
            lhs, c = f'x {"+" if b > 0 else "−"} {abs(b)}', g + b
            weg = f'{"−" if b > 0 else "+"} {abs(b)} auf beiden Seiten: x {z} {zt(g)}'
        else:
            lhs, c = f'{a}x', a * g
            weg = f': {a} auf beiden Seiten: x {z} {zt(g)}'
        if R.random() < .35 and -10 <= g <= 10:
            return M(f'Löse {lhs} {z} {zt(c)}. Markiere die Grenze der Lösungsmenge am Zahlenstrahl.', -10, 10, 20, g + 10,
                     f'{weg}. Die Grenze ist {zt(g)}.', 'Rechne zuerst die Grenze aus, dann suche sie auf dem Zahlenstrahl.')
        return A(R, f'Löse die Ungleichung {lhs} {z} {zt(c)}.', f'x {z} {zt(g)}', falsch_loesungen(z, g), weg + '.',
                 'Forme wie bei einer Gleichung um. Das Zeichen bleibt gleich.')
    if st == 2:
        a, g, b = R.randint(2, 9), R.randint(-8, 10), R.randint(1, 20) * R.choice([-1, 1])
        c = a * g + b
        txt = f'{lin(a, b)} {z} {zt(c)}'
        weg = f'{lin(a, b)} {z} {zt(c)} | {"−" if b > 0 else "+"} {abs(b)} → {a}x {z} {zt(a * g)} | : {a} → x {z} {zt(g)}'
        if R.random() < .5:
            return Z(f'Löse {txt}. Die Lösung hat die Form x {z} □. Gib die Zahl an.', g, f'({c} - ({b})) / {a}', weg + '.',
                     'Erst den Summanden ohne x wegbringen, dann durch die Zahl vor x teilen.')
        return A(R, f'Löse die Ungleichung {txt}.', f'x {z} {zt(g)}', falsch_loesungen(z, g) + [f'x {z} {zt(Fr(c + b, a))}'], weg + '.',
                 'Erst den Summanden ohne x wegbringen, dann durch die Zahl vor x teilen.')
    # Stufe 3: x auf beiden Seiten, Koeffizient bleibt positiv; Grenze darf Dezimalzahl sein
    if R.random() < .3:
        # Sonderfall: x fällt weg → alle Zahlen oder keine Zahl
        a = R.randint(2, 6)
        b1, b2 = R.sample([x for x in range(-12, 13) if x], 2)
        wahr = {'<': b1 < b2, '>': b1 > b2, '≤': b1 <= b2, '≥': b1 >= b2}[z]
        rl, kl_ = 'L = ℝ (jede Zahl)', 'L = { } (keine Zahl)'
        return A(R, f'Löse {lin(a, b1)} {z} {lin(a, b2)}.', rl if wahr else kl_,
                 [kl_ if wahr else rl, f'x {z} {zt(b2 - b1)}', f'x {z} 0'],
                 f'| − {a}x: {zt(b1)} {z} {zt(b2)}. Das x ist weggefallen; die Aussage ist {"immer wahr, also ist jede Zahl eine Lösung" if wahr else "immer falsch, also gibt es keine Lösung"}.',
                 'Bringe die x-Glieder auf eine Seite. Was bleibt übrig?')
    while True:
        r = R.randint(1, 6); p = r + R.randint(1, 5)
        g = Fr(R.randint(-20, 30), R.choice([1, 2, 4, 5])) if R.random() < .4 else Fr(R.randint(-9, 9))
        q = R.randint(-15, 15)
        s = (p - r) * g + q
        if s.denominator == 1 and q != 0: break
    txt = text_ug(p, q, z, r, s)
    weg = f'| − {lin(r, 0)} → {lin(p - r, q)} {z} {zt(s)} | {"−" if q > 0 else "+"} {abs(q)} → {lin(p - r, 0)} {z} {zt(s - q)} | : {p - r} → x {z} {zt(g)}'
    if g.denominator in (1, 2, 4, 5) and R.random() < .5:
        return Z(f'Löse {txt}. Die Lösung hat die Form x {z} □. Gib die Zahl an.', g, f'({cz(s)} - ({q})) / ({p} - {r})', weg + '.',
                 'Bringe alle x-Glieder auf die linke Seite, alle Zahlen auf die rechte.')
    return A(R, f'Löse die Ungleichung {txt}.', f'x {z} {zt(g)}', falsch_loesungen(z, g) + [f'x {z} {zt(Fr(s + q, p - r))}'], weg + '.',
             'Bringe alle x-Glieder auf die linke Seite, alle Zahlen auf die rechte.')


def g_umdrehen(R, st):
    z = R.choice(ZEICHEN)
    if st <= 2 and R.random() < .3:
        # Begründen: was passiert mit einer wahren Ungleichung, wenn man mit einer negativen Zahl rechnet?
        u, v = sorted(R.sample(range(-9, 10), 2))
        k = -R.randint(1, 5)
        if st == 2 and R.random() < .5:
            u, v = k * R.randint(-4, 0), k * R.randint(1, 4)
            u, v = min(u, v), max(u, v)
            if u == v: u -= abs(k)
            op, uu, vv = f'Teile beide Seiten durch {kl(k)}', Fr(u, k), Fr(v, k)
        else:
            op, uu, vv = f'Multipliziere beide Seiten mit {kl(k)}', u * k, v * k
        return A(R, f'Es gilt {zt(u)} < {zt(v)}. {op}. Was stimmt dann?', f'{zt(uu)} > {zt(vv)}',
                 [f'{zt(uu)} < {zt(vv)}', f'{zt(uu)} = {zt(vv)}', f'{zt(-uu)} < {zt(-vv)}'],
                 f'{zt(u)} → {zt(uu)} und {zt(v)} → {zt(vv)}. {zt(uu)} liegt rechts von {zt(vv)} auf dem Zahlenstrahl, also {zt(uu)} > {zt(vv)}. Das Zeichen hat sich umgedreht.',
                 'Rechne beide Zahlen aus und vergleiche sie auf dem Zahlenstrahl.')
    while True:
        if st == 1:
            a, g = (-1 if R.random() < .35 else -R.randint(2, 9)), Fr(R.randint(-9, 9)); q = 0; p, r = a, 0
        elif st == 2:
            a, g, q = (-1 if R.random() < .25 else -R.randint(2, 9)), Fr(R.randint(-9, 9)), R.randint(-15, 15); p, r = a, 0
        else:
            p = R.randint(1, 6); r = p + R.randint(1, 5); g = Fr(R.randint(-9, 12)); q = R.randint(-15, 15)
        s = (p - r) * g + q
        if g != 0 and (st == 1 or q != 0): break
    z2, g2 = loese(p, q, z, r, s)
    assert g2 == g and z2 == UMKEHR[z]
    txt = text_ug(p, q, z, r, s)
    k = p - r
    if st == 3:
        weg = f'| − {r}x → {lin(k, q)} {z} {zt(s)} | {"−" if q > 0 else "+"} {abs(q)} → {lin(k, 0)} {z} {zt(s - q)} | : {kl(k)}, Zeichen umdrehen → x {z2} {zt(g)}'
        h = 'Alle x nach links bringen. Ist der Faktor vor x negativ, beim Teilen das Zeichen umdrehen.'
    elif q:
        weg = f'| {"−" if q > 0 else "+"} {abs(q)} → {lin(k, 0)} {z} {zt(s - q)} | : {kl(k)}, Zeichen umdrehen → x {z2} {zt(g)}'
        h = 'Teilst du durch eine negative Zahl, drehst du das Zeichen um.'
    else:
        weg = f': {kl(k)} auf beiden Seiten, Zeichen umdrehen → x {z2} {zt(g)}'
        h = 'Teilst du durch eine negative Zahl, drehst du das Zeichen um.'
    richtig = f'x {z2} {zt(g)}'
    falsch = [f'x {z} {zt(g)}', f'x {z2} {zt(-g)}', f'x {z} {zt(-g)}']
    if st >= 2 and R.random() < .4:
        return Z(f'Löse {txt}. Die Lösung hat die Form x {z2} □. Gib die Zahl an.', g, f'({cz(s)} - ({q})) / ({p} - ({r}))', weg + '.', h)
    return A(R, f'Löse die Ungleichung {txt}.', richtig, falsch, weg + '.', h)


def g_klammern(R, st):
    z = R.choice(ZEICHEN)
    while True:
        a, b = R.choice([2, 3, 4, 5] if st == 1 else [2, 3, 4, 5, -2, -3]), R.randint(-6, 6)
        if st == 1:
            g = Fr(R.randint(-8, 8)); r, s0 = 0, None
            p, q = a, a * b
            s = p * g + q
            txt = f'{a if a > 0 else "−" + str(-a)}(x {"+" if b >= 0 else "−"} {abs(b)}) {z} {zt(s)}'
        elif st == 2:
            g = Fr(R.randint(-8, 8)); r = R.randint(-4, 6)
            p, q = a, a * b
            if p == r: continue
            d = R.randint(-10, 10)
            s = (p - r) * g + q   # rechte Seite r·x + s
            txt = f'{a if a > 0 else "−" + str(-a)}(x {"+" if b >= 0 else "−"} {abs(b)}) {z} {lin(r, s)}'
        else:
            c, d = R.randint(2, 5), R.randint(-5, 5)
            g = Fr(R.randint(-8, 8)); r = R.randint(-3, 3)
            p, q = a - c, a * b + c * d          # a(x+b) − c(x−d) = (a−c)x + ab + cd
            if p == r: continue
            s = (p - r) * g + q
            txt = (f'{a if a > 0 else "−" + str(-a)}(x {"+" if b >= 0 else "−"} {abs(b)}) − {c}(x {"−" if d >= 0 else "+"} {abs(d)}) {z} {lin(r, s)}')
        if b != 0 and p != 0 and q != 0 and s.denominator == 1: break
    z2, g2 = loese(p, q, z, r, s)
    assert g2 == g
    k = p - r
    weg = (f'Klammern auflösen: {lin(p, q)} {z} {lin(r, s)}. ' + ((f'− {lin(r, 0)}: ' if r > 0 else f'+ {lin(-r, 0)}: ') + f'{lin(k, q)} {z} {zt(s)}. ' if r else '') +
           f'{"−" if q > 0 else "+"} {abs(q)}: {lin(k, 0)} {z} {zt(s - q)}' +
           ('.' if k == 1 else f'. : {kl(k)}' + (', Zeichen umdrehen' if k < 0 else '') + f' → x {z2} {zt(g)}.'))
    h = 'Löse zuerst die Klammern auf. Achte am Ende auf das Vorzeichen vor x.'
    if st >= 2 and R.random() < .4:
        return Z(f'Löse {txt}. Die Lösung hat die Form x {z2} □. Gib die Zahl an.', g, f'({cz(s)} - ({q})) / (({p}) - ({r}))', weg, h)
    return A(R, f'Löse die Ungleichung {txt}.', f'x {z2} {zt(g)}', [f'x {UMKEHR[z2]} {zt(g)}', f'x {z2} {zt(-g)}' if g else f'x {z2} 1',
             f'x {z2} {zt(Fr(s + q, k))}', f'x {UMKEHR[z2]} {zt(-g)}' if g else f'x {UMKEHR[z2]} 1'], weg, h)


def intervall(z, g):
    G = zt(g)
    return {'<': f']−∞; {G}[', '≤': f']−∞; {G}]', '>': f']{G}; ∞[', '≥': f'[{G}; ∞['}[z]


def g_intervall(R, st):
    if st <= 2 and R.random() < .35:
        z = R.choice(ZEICHEN)
        g = Fr(R.randint(-9, 9)) if st == 1 else Fr(R.choice([x for x in range(-19, 20) if x % 2]), 2)
        iv = intervall(z, g)
        return A(R, f'Welche Ungleichung gehört zur Lösungsmenge L = {iv}?', f'x {z} {zt(g)}',
                 [f'x {x} {zt(g)}' for x in ZEICHEN if x != z],
                 f'{"Bis −∞: x ist kleiner" if z in "<≤" else "Bis ∞: x ist größer"}; die Klammer bei {zt(g)} zeigt {"nach innen, die Grenze gehört dazu" if z in "≤≥" else "nach außen, die Grenze gehört nicht dazu"}. Also x {z} {zt(g)}.',
                 'Wohin reicht das Intervall (−∞ oder ∞)? Gehört die Grenze dazu?')
    if st == 1:
        z, g = R.choice(ZEICHEN), Fr(R.randint(-9, 9))
        r = intervall(z, g)
        andere = [intervall(x, g) for x in ZEICHEN if x != z]
        return A(R, f'Schreibe die Lösungsmenge von x {z} {zt(g)} als Intervall.', f'L = {r}', [f'L = {x}' for x in andere],
                 f'{"Die Grenze gehört dazu" if z in "≤≥" else "Die Grenze gehört nicht dazu"}, und x ist {"kleiner" if z in "<≤" else "größer"} als {zt(g)}: L = {r}.',
                 'Zeigt das Zeichen nach links (<, ≤), reicht das Intervall bis −∞. Gehört die Grenze dazu?')
    if st == 2:
        z = R.choice(ZEICHEN)
        while True:
            a, g, b = R.choice([2, 3, 4, 5, -2, -3, -4]), Fr(R.randint(-8, 8)), R.randint(-12, 12)
            if b: break
        c = a * g + b
        z2, _ = loese(a, b, z, 0, c)
        r = intervall(z2, g)
        return A(R, f'Löse {lin(a, b)} {z} {zt(c)} und gib die Lösungsmenge als Intervall an.', f'L = {r}',
                 [f'L = {intervall(x, g)}' for x in ZEICHEN if x != z2] + [f'L = {intervall(z2, -g)}'],
                 f'{lin(a, b)} {z} {zt(c)} → {lin(a, 0)} {z} {zt(c - b)} → x {z2} {zt(g)}' + (' (Zeichen umgedreht, da durch eine negative Zahl geteilt)' if a < 0 else '') + f'. L = {r}.',
                 'Erst lösen, dann das Intervall aufschreiben. Achte auf negative Faktoren vor x.')
    # Doppelungleichung
    while True:
        a, b = R.choice([2, 3, 4, 5]), R.randint(-9, 9)
        u, o = sorted(R.sample(range(-8, 9), 2))
        if b: break
    z1, z2 = R.choice(['<', '≤']), R.choice(['<', '≤'])
    lo, hi = a * u + b, a * o + b
    r = ('[' if z1 == '≤' else ']') + f'{zt(u)}; {zt(o)}' + (']' if z2 == '≤' else '[')
    falsch = [('[' if z1 == '<' else ']') + f'{zt(u)}; {zt(o)}' + (']' if z2 == '<' else '['),
              ('[' if z1 == '≤' else ']') + f'{zt(lo)}; {zt(hi)}' + (']' if z2 == '≤' else '['),
              ('[' if z1 == '≤' else ']') + f'{zt(Fr(lo + b, a))}; {zt(Fr(hi + b, a))}' + (']' if z2 == '≤' else '[')]
    return A(R, f'Löse {zt(lo)} {z1} {lin(a, b)} {z2} {zt(hi)} und gib die Lösungsmenge als Intervall an.', f'L = {r}', [f'L = {x}' for x in falsch],
             f'Auf allen drei Teilen {"−" if b > 0 else "+"} {abs(b)}: {zt(lo - b)} {z1} {a}x {z2} {zt(hi - b)}. Durch {a}: {zt(u)} {z1} x {z2} {zt(o)}. L = {r}.',
             'Rechne auf allen drei Teilen gleichzeitig. Dann gibt es eine linke und eine rechte Grenze.')


def g_pruefen(R, st):
    z = R.choice(ZEICHEN)
    if st == 1:
        while True:
            a, b, g = R.randint(2, 6), R.randint(-10, 10), R.randint(-6, 6)
            if b: break
        c = a * g + b
        txt = f'{lin(a, b)} {z} {zt(c)}'
        ok = {'<': lambda x: x < g, '≤': lambda x: x <= g, '>': lambda x: x > g, '≥': lambda x: x >= g}[z]
        kand = [g - 3, g - 1, g, g + 1, g + 3]
        rich = [x for x in kand if ok(x)]; fal = [x for x in kand if not ok(x)]
        if len(rich) >= len(fal) and len(fal) >= 1:
            # Frage nach der Zahl, die KEINE Lösung ist
            x0 = R.choice(fal)
            return A(R, f'Welche Zahl ist KEINE Lösung von {txt}?', zt(x0), [zt(x) for x in R.sample(rich, min(3, len(rich)))],
                     f'Einsetzen: {a} · {kl(x0)} {"+" if b > 0 else "−"} {abs(b)} = {zt(a * x0 + b)}, und {zt(a * x0 + b)} {z} {zt(c)} ist falsch. Lösung ist x {z} {zt(g)}.',
                     'Setze jede Zahl ein oder löse die Ungleichung zuerst.')
        x0 = R.choice(rich)
        return A(R, f'Welche Zahl ist eine Lösung von {txt}?', zt(x0), [zt(x) for x in R.sample(fal, min(3, len(fal)))],
                 f'Einsetzen: {a} · {kl(x0)} {"+" if b > 0 else "−"} {abs(b)} = {zt(a * x0 + b)}, und {zt(a * x0 + b)} {z} {zt(c)} ist wahr. Lösung ist x {z} {zt(g)}.',
                 'Setze jede Zahl ein oder löse die Ungleichung zuerst.')
    if st == 2:
        # größte/kleinste ganze Zahl, die die Ungleichung erfüllt
        while True:
            a, b = R.choice([2, 3, 4, 5, -2, -3, -4]), R.randint(-12, 12)
            c = R.randint(-20, 20)
            if b and (c - b) % a != 0: break
        g = Fr(c - b, a)
        z2 = z if a > 0 else UMKEHR[z]
        # Grenze ist nicht ganzzahlig: abrunden bzw. aufrunden
        if z2 in '<≤':
            frage, wert = 'größte', g.numerator // g.denominator
        else:
            frage, wert = 'kleinste', -((-g.numerator) // g.denominator)
        p, qn = g.numerator, g.denominator
        c_ausdr = f'{p} // {qn}' if frage == 'größte' else f'-((-{p}) // {qn})'
        return Z(f'Gib die {frage} ganze Zahl an, die {lin(a, b)} {z} {zt(c)} erfüllt.', wert, c_ausdr,
                 f'Lösen: x {z2} {zt(g)}' + (' (Zeichen umgedreht)' if a < 0 else '') + f'. Die {frage} ganze Zahl ist {zt(wert)}.',
                 'Löse zuerst die Ungleichung. Liegt die Grenze zwischen zwei ganzen Zahlen, überlege, welche noch passt.')
    # Stufe 3: Fehler in einer Rechnung finden
    while True:
        a, g, b = -R.randint(2, 6), R.randint(-6, 6), R.randint(1, 12) * R.choice([-1, 1])
        if g: break
    c = a * g + b
    art = R.choice(['umdrehen', 'subtraktion', 'richtig', 'teilen'])
    s1 = c - b
    if art == 'subtraktion': s1 = c + b
    gg = Fr(s1, a)
    zf = z if art == 'umdrehen' else UMKEHR[z]
    if art == 'teilen': gg = -gg
    text = (f'Jemand löst {lin(a, b)} {z} {zt(c)} so: {"−" if b > 0 else "+"} {abs(b)} ergibt {lin(a, 0)} {z} {zt(s1)}; '
            f'durch {kl(a)} ergibt x {zf} {zt(gg)}. Was stimmt?')
    opts = {'umdrehen': 'Beim Teilen durch die negative Zahl wurde das Zeichen nicht umgedreht.',
            'subtraktion': (f'Im ersten Schritt wurde falsch gerechnet: richtig ist {lin(a, 0)} {z} {zt(c - b)}.' if art == 'subtraktion' else
                            f'Im ersten Schritt hätte man {"+" if b > 0 else "−"} {abs(b)} statt {"−" if b > 0 else "+"} {abs(b)} rechnen müssen.'),
            'teilen': 'Beim Teilen wurde das Vorzeichen des Ergebnisses falsch bestimmt.',
            'richtig': 'Die Rechnung ist richtig.'}
    richtig = opts[art]
    loes = f'Richtig: {lin(a, 0)} {z} {zt(c - b)}, durch {kl(a)} mit Umdrehen: x {UMKEHR[z]} {zt(g)}.'
    return A(R, text, richtig, [v for k, v in opts.items() if k != art], loes,
             'Rechne jeden Schritt selbst nach und vergleiche.')


def _fenster(fs, x0):
    xa, xb = x0 - 5, x0 + 5
    ys = [f(x) for f in fs for x in (xa, xb)] + [0]
    ya, yb = min(ys), max(ys)
    ya, yb = max(ya, -14), min(yb, 14)
    return [xa, xb], [int(ya) - 1, int(yb) + 1]


def g_grafisch(R, st):
    z = R.choice(ZEICHEN)
    while True:
        x0 = R.randint(-4, 4)
        if st == 1:
            m1 = R.choice([1, 2, 3, -1, -2]); c = R.choice([0, 0, R.randint(-6, 8)])
            t1 = c - m1 * x0; m2, t2 = 0, c
        else:
            m1, m2 = R.sample([-2, -1, Fr(-1, 2), Fr(1, 2), 1, 2, 3], 2)
            t1 = R.randint(-6, 6); t2 = m1 * x0 + t1 - m2 * x0
        if Fr(t1).denominator == 1 and Fr(t2).denominator == 1 and abs(t1) <= 12 and abs(t2) <= 12: break
    z2, g = loese(m1, t1, z, m2, t2)
    assert g == x0
    f1 = lambda x: float(m1 * x + t1)
    f2 = lambda x: float(m2 * x + t2)
    X, Y = _fenster([f1, f2], x0)
    links, rechts = lin(m1, t1), (lin(m2, t2) if m2 else zt(t2))
    zeigen = st < 3
    gr = {'typ': 'koordinaten', 'x': X, 'y': Y,
          'graphen': [{'art': 'linear', 'm': float(m1) if Fr(m1).denominator != 1 else int(m1), 't': int(t1), 'name': f'y = {links}' if zeigen else 'f'},
                      {'art': 'linear', 'm': float(m2) if Fr(m2).denominator != 1 else int(m2), 't': int(t2), 'name': f'y = {rechts}' if zeigen else 'g'}]}
    if st == 1: gr['senkrecht'] = [x0]
    lage = 'unterhalb' if z in '<≤' else 'oberhalb'
    weg = (f'Die Geraden schneiden sich bei x = {zt(x0)}. Für x {z2} {zt(x0)} liegt {"die erste" if zeigen else "f"} {lage} {"der zweiten" if zeigen else "von g"}'
           + (' (am Schnittpunkt sind beide gleich, er gehört bei ' + z + ' dazu)' if z in '≤≥' else '') + f'. Lösung: x {z2} {zt(x0)}.')
    h = 'Suche den Schnittpunkt. Auf welcher Seite davon liegt die linke Gerade ' + lage + ' der rechten?'
    falsch = [f'x {UMKEHR[z2]} {zt(x0)}', f'x {z2} {zt(t1)}' if t1 != x0 else f'x {z2} {zt(x0 + 1)}', f'x {z2} {zt(-x0)}' if x0 else f'x {z2} 1',
              f'x {UMKEHR[z2]} {zt(-x0)}' if x0 else f'x {UMKEHR[z2]} 1']
    if st == 3:
        if R.random() < .5:
            iv = intervall(z2, Fr(x0))
            return mit_bild(A(R, f'Die Abbildung zeigt die Geraden f und g. Gib die Lösungsmenge von f(x) {z} g(x) an.', f'L = {iv}',
                              [f'L = {intervall(UMKEHR[z2], Fr(x0))}', f'L = {intervall({"<": "≤", "≤": "<", ">": "≥", "≥": ">"}[z2], Fr(x0))}',
                               f'L = {intervall(z2, Fr(-x0) if x0 else Fr(1))}'],
                              weg + f' Als Intervall: L = {iv}.', h.replace('linke Gerade', 'Gerade f').replace('der rechten', 'von g')), gr)
        return mit_bild(A(R, f'Die Abbildung zeigt die Geraden f und g. Für welche x liegt f {lage} von g{", Schnittpunkt eingeschlossen" if z in "≤≥" else ""}?',
                          f'x {z2} {zt(x0)}', falsch[:1] + falsch[2:] + [f'x {({"<": "≤", "≤": "<", ">": "≥", "≥": ">"})[z2]} {zt(x0)}'],
                          weg, h.replace('linke Gerade', 'Gerade f').replace('der rechten', 'von g')), gr)
    if st == 2 and R.random() < .3:
        return mit_bild(Z(f'Löse {links} {z} {rechts} mit den Graphen. Die Lösung hat die Form x {z2} □. Gib die Zahl an.', x0,
                          f'(({cz(Fr(t2))}) - ({cz(Fr(t1))})) / (({cz(Fr(m1))}) - ({cz(Fr(m2))}))', weg, h), gr)
    frage = f'Löse {links} {z} {rechts} mithilfe der Graphen.' if R.random() < .5 or m2 != 0 else \
        f'Für welche x liegt der Graph von y = {links} {lage} {"der x-Achse" if t2 == 0 else f"der Geraden y = {zt(t2)}"}?'
    return mit_bild(A(R, frage, f'x {z2} {zt(x0)}', falsch, weg, h), gr)


def gx(p):
    """Geldbetrag als Faktor vor x: 1 → x."""
    return 'x' if p == 1 else f'{eur(p)}x'


TARIF = {'n': 0}


def g_aufstellen(R):
    art = R.choice(['paket', 'verein', 'rad', 'koffer'])
    if art == 'paket':
        H, k, b = R.choice([10, 20, 31]), Fr(R.choice([5, 10, 15, 20]), 10), Fr(R.choice([4, 5, 6, 8, 12]), 10)
        t = f'Ein Paket darf höchstens {H} kg wiegen. Der Karton wiegt {zt(k)} kg, jedes Buch {zt(b)} kg. Welche Ungleichung passt (x = Anzahl Bücher)?'
        ri, fa = f'{zt(k)} + {zt(b)}x ≤ {H}', [f'{zt(k)} + {zt(b)}x ≥ {H}', f'{zt(k)}x + {zt(b)} ≤ {H}', f'{zt(b)}x ≤ {H}']
        w = f'Gesamtgewicht = Karton + Bücher = {zt(k)} + {zt(b)}x; „höchstens“ heißt ≤: {ri}.'
    elif art == 'verein':
        Zl, h, p = R.choice([300, 400, 500, 600]), R.choice([80, 120, 150, 200]), R.choice([Fr(3, 2), Fr(2), Fr(5, 2), Fr(3)])
        t = f'Ein Verein braucht mehr als {Zl} € für einen Ausflug. Er hat schon {h} € und verkauft Kuchen zu {eur(p)} € pro Stück. Welche Ungleichung passt (x = Anzahl verkaufter Kuchenstücke)?'
        ri, fa = f'{h} + {eur(p)}x > {Zl}', [f'{h} + {eur(p)}x ≥ {Zl}', f'{h} + {eur(p)}x < {Zl}', f'{h}x + {eur(p)} > {Zl}']
        w = f'Geld = vorhanden + Verkauf = {h} + {eur(p)}x; „mehr als“ heißt >: {ri}.'
    elif art == 'rad':
        Zl, h, p = R.choice([350, 420, 480, 600]), R.choice([60, 90, 110, 150]), R.choice([15, 20, 25, 30])
        t = f'Für ein Fahrrad (Preis {Zl} €) hat jemand {h} € gespart und legt jede Woche {p} € dazu. Welche Ungleichung beschreibt: „Das Geld reicht mindestens für das Fahrrad“ (x = Anzahl Wochen)?'
        ri, fa = f'{h} + {p}x ≥ {Zl}', [f'{h} + {p}x ≤ {Zl}', f'{h} + {p}x > {Zl}', f'{p} + {h}x ≥ {Zl}']
        w = f'Erspartes nach x Wochen: {h} + {p}x; „mindestens“ heißt ≥: {ri}.'
    else:
        H, k, b = R.choice([20, 23]), Fr(R.choice([30, 35, 40, 45]), 10), Fr(R.choice([3, 4, 5]), 10)
        t = f'Ein Koffer darf beim Flug höchstens {H} kg wiegen. Er wiegt leer {zt(k)} kg und schon gepackt 12 kg Kleidung. Dazu kommen Bücher zu je {zt(b)} kg. Welche Ungleichung passt (x = Anzahl Bücher)?'
        ri, fa = f'{zt(k + 12)} + {zt(b)}x ≤ {H}', [f'{zt(k + 12)} + {zt(b)}x ≥ {H}', f'{zt(k)} + {zt(b)}x ≤ {H}', f'{zt(k + 12)} + {zt(b)}x < {H}']
        w = f'Koffer + Kleidung = {zt(k)} + 12 = {zt(k + 12)} kg, dazu {zt(b)}x; „höchstens“ heißt ≤: {ri}.'
    return A(R, t, ri, fa, w, 'Was wird zusammengezählt? Welches Zeichen passt zu „höchstens“, „mindestens“, „mehr als“?')


def g_sachaufgabe(R, st):
    arten = {1: ['aufzug', 'tarif', 'regal', 'aufstellen'], 2: ['tarif', 'taxi', 'sparen', 'aufzug', 'aufstellen'], 3: ['kino', 'sparen', 'vergleich']}[st]
    if TARIF['n'] >= 4: arten = [a for a in arten if a != 'tarif']
    art = R.choice(arten)
    if art == 'tarif': TARIF['n'] += 1
    if art == 'aufstellen':
        return g_aufstellen(R)
    if art == 'aufzug':
        while True:
            L, p, k = R.choice([300, 400, 450, 500]), R.randint(65, 95), R.choice([25, 30, 35, 40, 45, 50])
            n = (L - p) // k
            if 3 <= n <= 10 and (L - p) % k: break
        return Z(f'Ein Aufzug darf höchstens {L} kg tragen. Eine Person ({p} kg) will Kisten zu je {k} kg mitnehmen. Wie viele Kisten darf sie höchstens einladen?',
                 n, f'({L} - {p}) // {k}', f'{p} + {k}x ≤ {L} → {k}x ≤ {L - p} → x ≤ {grenze(Fr(L - p, k))}. Bei „höchstens“ wird abgerundet: höchstens {n} Kisten.',
                 'Stelle eine Ungleichung mit „≤“ auf. Nur ganze Kisten sind möglich.')
    if art == 'regal':
        L, k = R.choice([40, 50, 60, 75, 80]), R.choice([3, 4, 6, 7, 8, 9])
        if L % k == 0: L += 1
        n = L // k
        return Z(f'Ein Regalbrett trägt höchstens {L} kg. Ein Karton wiegt {k} kg. Wie viele Kartons passen höchstens darauf?',
                 n, f'{L} // {k}', f'{k}x ≤ {L} → x ≤ {grenze(Fr(L, k))}. Abrunden: höchstens {n} Kartons.', 'Teile und runde ab.')
    if art == 'tarif':
        g, p, B = R.choice([5, 8, 10, 12]), R.choice([Fr(3, 2), Fr(2), Fr(5, 2), Fr(3), Fr(7, 2)]), R.choice([20, 25, 30, 35, 40])
        n = int((B - g) / p)
        return Z(f'Ein Handytarif kostet im Monat {eur(g)} € Grundgebühr und {eur(p)} € je zusätzliches Datenpaket. Man will höchstens {B} € zahlen. Wie viele Datenpakete kann man höchstens kaufen?',
                 n, f'({B} - {g}) * {p.denominator} // {p.numerator}', f'{eur(g)} + {gx(p)} ≤ {B} → {gx(p)} ≤ {B - g} → x ≤ {grenze(Fr(B - g) / p)}. Höchstens {n} Pakete.',
                 'Grundgebühr + Preis · Anzahl ≤ Höchstbetrag.')
    if art == 'taxi':
        g, p, B = R.choice([Fr(7, 2), Fr(4), Fr(9, 2)]), R.choice([Fr(2), Fr(11, 5), Fr(12, 5), Fr(5, 2)]), R.choice([20, 25, 30, 40, 50])
        n = int((B - g) / p)
        return Z(f'Eine Taxifahrt kostet {eur(g)} € Grundpreis und {eur(p)} € je angefangenen Kilometer. Wie viele Kilometer kann man mit {B} € höchstens fahren?',
                 n, f'(({B}) - {cz(g)}) * {p.denominator} // {p.numerator}' if g.denominator == 1 else f'({B} * {g.denominator} - {g.numerator}) * {p.denominator} // ({p.numerator} * {g.denominator})',
                 f'{eur(g)} + {gx(p)} ≤ {B} → {gx(p)} ≤ {eur(B - g)} → x ≤ {grenze((B - g) / p)}. Ab dem {n + 1}. angefangenen Kilometer wird es zu teuer, also höchstens {n} km.',
                 'Stelle die Ungleichung auf und runde passend.')
    if art == 'sparen':
        s, w, Zl = R.randint(10, 60), R.choice([4, 5, 6, 7, 8, 12, 15]), R.choice([150, 200, 250, 300, 400])
        n = (Zl - s) // w + 1
        return Z(f'Auf einem Sparbuch sind {s} €. Jede Woche kommen {w} € dazu. Nach wie vielen Wochen sind zum ersten Mal mehr als {Zl} € darauf?',
                 n, f'({Zl} - {s}) // {w} + 1', f'{s} + {w}x > {Zl} → x > {grenze(Fr(Zl - s, w))}. Kleinste ganze Zahl: {n} Wochen.',
                 '„Mehr als“ bedeutet >. Gesucht ist die kleinste passende ganze Zahl.')
    if art == 'kino':
        e, r = R.choice([Fr(9), Fr(19, 2), Fr(10), Fr(21, 2), Fr(12)]), R.choice([Fr(4), Fr(9, 2), Fr(5), Fr(6)])
        j = R.choice([45, 50, 60, 70, 80, 90])
        n = int(j / (e - r)) + 1
        return Z(f'Ein Kinobesuch kostet {eur(e)} €. Mit einer Jahreskarte für {j} € zahlt man pro Besuch nur {eur(r)} €. Ab wie vielen Besuchen ist man mit der Jahreskarte billiger?',
                 n, f'{j} * {(e - r).denominator} // {(e - r).numerator} + 1', f'{j} + {gx(r)} < {gx(e)} → {gx(e - r)} > {j} → x > {grenze(j / (e - r))}. Ab {n} Besuchen.',
                 'Kosten mit Karte < Kosten ohne Karte. Gesucht ist die kleinste ganze Zahl.')
    # vergleich zweier Tarife
    g1, p1 = R.choice([0, 2, 3]), R.choice([Fr(3, 2), Fr(2), Fr(5, 2)])
    g2, p2 = g1 + R.choice([6, 8, 10, 12]), p1 - R.choice([Fr(1, 2), Fr(1)])
    n = int((g2 - g1) / (p1 - p2)) + 1
    return Z(f'Fitness-Studio A: {g1} € Grundbetrag, {eur(p1)} € je Besuch. Studio B: {g2} € Grundbetrag, {eur(p2)} € je Besuch. Ab wie vielen Besuchen im Monat ist B billiger?',
             n, f'({g2} - {g1}) * {(p1 - p2).denominator} // {(p1 - p2).numerator} + 1',
             f'{g2} + {gx(p2)} < {g1} + {gx(p1)} → {gx(p1 - p2)} > {g2 - g1} → x > {grenze((g2 - g1) / (p1 - p2))}. Ab {n} Besuchen.',
             'Stelle „Kosten B < Kosten A“ auf und löse nach x.')


GEN = {'umformen': g_umformen, 'umdrehen': g_umdrehen, 'klammern': g_klammern, 'intervall': g_intervall, 'pruefen': g_pruefen,
       'grafisch': g_grafisch, 'sachaufgabe': g_sachaufgabe}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Ungleichungen lösen', ['umformen', 'umdrehen', 'klammern']), ('Lösungsmenge', ['intervall', 'pruefen', 'grafisch']), ('Anwenden', ['sachaufgabe'])],
         'Lineare Ungleichungen lösen, beim Multiplizieren oder Dividieren mit einer negativen Zahl das Zeichen umdrehen und die Lösungsmenge als Intervall angeben.',
         ['Wie bei Gleichungen umformen – aber: Mal oder geteilt durch eine negative Zahl dreht das Zeichen um.',
          '< und > : Grenze gehört nicht dazu, Klammer nach außen. ≤ und ≥ : Grenze gehört dazu, Klammer nach innen.',
          'Höchstens = ≤, mindestens = ≥.'],
         offen=['Lernkarte „umformen“: Lösungsmenge als markierter Bereich auf dem Zahlenstrahl (offener/geschlossener Kreis, Schraffur) kann die App nicht zeichnen; der Pfeil zeigt nur die Grenze.',
                'Prüfpunkt „Ablesen am Zahlenstrahl“ (Karte intervall) nicht umgesetzt: ohne gezeichneten Bereich gibt es nichts abzulesen. Stattdessen „Intervall → Ungleichung“ eingebaut; das grafische Lösen steht in der neuen Karte „grafisch“.'])
