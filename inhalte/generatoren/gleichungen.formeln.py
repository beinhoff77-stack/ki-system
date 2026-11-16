#!/usr/bin/env python3
"""Thema gleichungen.formeln – Formeln umstellen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import re
from _bausatz import A, Z, baue, cz, eur, ist_endlich, kl, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.formeln', 'thema_id': 4, 'block_id': 60, 'klasse': {'gym_by': 8}}

ETAPPEN = [
    {'lernziel': 'ein_schritt', 'titel': 'Formeln in einem Schritt umstellen',
     'regel': 'Eine Formel stellst du um wie eine Gleichung: Mit der ⟦Umkehrrechnung⟧ isolierst du die gesuchte Größe. Mal wird zu ⟦geteilt⟧, plus wird zu ⟦minus⟧.',
     'schritte': ['W = F · s nach s umstellen.', 's ist mit F multipliziert, also beide Seiten durch F teilen.', '⟦s = W : F⟧'],
     'probe': 'F = 5, s = 4 → W = 20. Und 20 : 5 = 4 ✓',
     'fehler': 'Aus W = F · s wird nicht s = W · F. Wer mit F ⟦multipliziert⟧ ist, wird durch F ⟦geteilt⟧.',
     '_verbot': ['W = F · s']},
    {'lernziel': 'zwei_schritte', 'titel': 'Formeln in zwei Schritten umstellen',
     'regel': 'Gehe ⟦rückwärts⟧ vor – wie beim Ausziehen: Socken zuerst an, Schuhe zuletzt an, also Schuhe ⟦zuerst⟧ wieder aus. In der Formel wird mal zuerst gerechnet und plus zuletzt. Also entfernst du zuerst das ⟦Plus⟧, dann das Mal.',
     'schritte': ['Taxipreis: K = G + p · s (K Kosten, G Grundgebühr, p Preis pro km, s Strecke). Gesucht ist s.',
                  'Zuletzt wurde G addiert, also zuerst | − G: K − G = p · s.', 'Dann | : p: ⟦s = (K − G) : p⟧.'],
     'probe': 'G = 4 €, p = 2 € pro km, s = 8 km: K = 4 + 16 = 20 €. Rückwärts: (20 − 4) : 2 = 8 ✓',
     'fehler': 'Aus K = G + p · s wird nicht s = K : p − G. Mit Zahlen: 20 : 2 − 4 = 6 km statt 8 km. Zuerst muss das ⟦+ G⟧ weg, sonst wird die Grundgebühr auch durch p geteilt. Richtig: s = (K − G) : p.'},
    {'lernziel': 'pruefen', 'titel': 'Ist die Umstellung richtig?',
     'regel': 'Eine Umstellung prüfst du mit ⟦Zahlen⟧: Wähle Werte, rechne mit der Originalformel und setze in die umgestellte Formel ein. Es muss ⟦dasselbe⟧ herauskommen. Nimm keine 0 und keine 1 – mit ihnen fallen viele Fehler nicht auf.',
     'schritte': ['Behauptung: Aus u = 4 · a folgt a = u − 4.', 'Test: a = 3 → u = 12. Dann u − 4 = 8, nicht 3.', 'Also ⟦falsch⟧. Richtig: a = u : 4.'],
     'fehler': 'Ein passendes Zahlenbeispiel beweist noch nichts. Jemand stellt u = 4 · a um zu a = u − 12 und testet a = 4: u = 16, und 16 − 12 = 4 ✓ – reiner Zufall! Mit a = 5: u = 20, aber 20 − 12 = 8 ≠ 5. Teste deshalb ⟦zwei verschiedene⟧ Zahlen.',
     '_verbot': ['u = 4 · a']},
    {'lernziel': 'einsetzen', 'titel': 'Umstellen und Werte einsetzen',
     'regel': 'Stelle zuerst die Formel nach der ⟦gesuchten Größe⟧ um, dann setze die Werte ⟦mit Einheiten⟧ ein und rechne aus.',
     'schritte': ['Ein Radfahrer fährt 45 km mit 18 km/h. Wie lange dauert es?', 'v = s : t umstellen: t = s : v', 't = 45 km : 18 km/h = ⟦2,5 h⟧'],
     'fehler': 't = v : s = 18 : 45 = 0,4 h ist falsch: Die Formel wurde falsch umgestellt. Prüfe mit den ⟦Einheiten⟧: km/h : km ergibt keine Zeit.',
     '_verbot': ['45 km mit 18 km/h']},
    {'lernziel': 'geometrie', 'titel': 'Fehlende Maße aus Formeln',
     'regel': 'Kennst du die ⟦Fläche⟧ oder das ⟦Volumen⟧, kannst du eine fehlende Länge berechnen: Formel aufschreiben, nach der Länge ⟦umstellen⟧, einsetzen.',
     'schritte': ['Ein Dreieck hat A = 24 cm² und g = 8 cm. Wie hoch ist es?', 'A = g · h : 2 → h = 2 · A : g', 'h = 48 cm² : 8 cm = ⟦6 cm⟧'],
     'fehler': 'h = A : g = 3 cm ist falsch: Beim Dreieck steht in der Formel noch ⟦: 2⟧. Beim Umstellen wird daraus · 2.',
     '_verbot': ['A = 24 cm² und g = 8 cm']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'ein_schritt': {
  'einstieg': 'An der Obsttheke gilt: Preis = Kilopreis · Menge. Damit rechnest du aus, was 3 kg Äpfel zu 2 € pro kg kosten: 6 €. Oft willst du es andersherum wissen: Wie viele kg bekomme ich für 5 €? Dann drehst du die Rechnung um. Eine Rechenvorschrift mit Buchstaben heißt ⟦Formel⟧, das Umdrehen heißt ⟦umstellen⟧.',
  'woerter': [['Formel', 'eine Rechenvorschrift mit Buchstaben, z. B. W = F · s'], ['Größe', 'ein Buchstabe in der Formel für eine messbare Sache (Kraft, Weg, Preis …)'],
              ['W = F · s', 'aus der Physik: Arbeit W = Kraft F mal Weg s'], ['umstellen', 'die Formel so umformen, dass die gesuchte Größe allein auf einer Seite steht'],
              ['Umkehrrechnung', 'die Rechnung, die eine andere rückgängig macht: mal ↔ geteilt, plus ↔ minus']],
  'schritte': ['Formel: W = F · s. Gesucht ist s.', 's wird mit F malgenommen. Die Umkehrrechnung dazu ist: durch F teilen.', 'Beide Seiten durch F teilen: W : F = s.',
               'Andersherum geschrieben: ⟦s = W : F⟧.'],
  'regel': 'So stellst du eine ⟦Formel⟧ um: Schau, was mit der gesuchten Größe gerechnet wird, und mach es mit der ⟦Umkehrrechnung⟧ auf beiden Seiten rückgängig. Mal wird zu ⟦geteilt⟧, plus wird zu ⟦minus⟧.',
  'fehler': 'Aus W = F · s wird nicht s = W · F. Das wäre, als würdest du an der Obsttheke für 6 € bei 2 € pro kg nicht 6 : 2 = 3 kg, sondern 6 · 2 = 12 kg erwarten. Wer mit F ⟦malgenommen⟧ ist, wird durch F ⟦geteilt⟧.'},
 'zwei_schritte': {
  'einstieg': 'Eine Taxifahrt kostet 4 € Grundgebühr und 2 € pro Kilometer. Für 8 km zahlst du 4 + 2 · 8 = 20 €. Jetzt andersherum: Du hast 20 € bezahlt – wie weit bist du gefahren? Dafür musst du zwei Rechenschritte rückgängig machen, und zwar in der ⟦umgekehrten Reihenfolge⟧.',
  'woerter': [['K = G + p · s', 'Taxi-Formel: Kosten K = Grundgebühr G plus Preis p pro km mal Strecke s'], ['| − G', 'Randnotiz: Auf beiden Seiten wird G abgezogen.'],
              ['(K − G) : p', 'erst die Klammer ausrechnen, dann teilen']],
  'schritte': ['Taxi-Formel: K = G + p · s. Gesucht ist die Strecke s.',
               'Beim Ausrechnen kam zuletzt „+ G“ dazu. Das machst du zuerst rückgängig: Auf beiden Seiten G abziehen ergibt K − G = p · s.',
               'Jetzt wird s nur noch mit p malgenommen. Beide Seiten durch p teilen.', 'Ergebnis: ⟦s = (K − G) : p⟧. Mit den Zahlen: (20 − 4) : 2 = 8 km.']},
 'pruefen': {
  'einstieg': 'Du hast eine Formel umgestellt und bist dir unsicher? Dann probier sie mit erfundenen Zahlen aus – so, wie man ein neues Rezept erst einmal probekocht. Passt das Ergebnis zur ursprünglichen Formel, war die Umstellung wahrscheinlich richtig. Dieses Ausprobieren heißt ⟦Probe mit Zahlen⟧.',
  'woerter': [['u = 4 · a', 'Umfang u eines Quadrats mit der Seitenlänge a'], ['Probe mit Zahlen', 'Werte erfinden, in beide Formeln einsetzen und vergleichen'],
              ['Behauptung', 'eine Aussage, die noch geprüft werden muss']],
  'schritte': ['Behauptung: Aus u = 4 · a folgt a = u − 4.', 'Erfinde eine Zahl: a = 3. Dann ist u = 4 · 3 = 12.',
               'Setze u = 12 in die Umstellung ein: 12 − 4 = 8. Herauskommen müsste aber 3.', 'Also ist die Umstellung ⟦falsch⟧. Richtig ist a = u : 4.']},
 'einsetzen': {
  'einstieg': 'Du planst eine Radtour über 45 km und schaffst im Schnitt 18 km pro Stunde. Wie lange bist du unterwegs? Die Formel v = s : t kennt man aus der Physik, gesucht ist hier aber t. Also erst ⟦umstellen⟧, dann die Zahlen mit ihren ⟦Einheiten⟧ einsetzen.',
  'woerter': [['v = s : t', 'Geschwindigkeit v = Strecke s geteilt durch Zeit t'], ['km/h', 'Kilometer pro Stunde'], ['Einheit', 'die Maßangabe hinter der Zahl: km, h, €, cm²'],
              ['h', 'Stunde (vom lateinischen hora)']],
  'schritte': ['Gesucht ist die Zeit t. Die Formel heißt v = s : t.', 't steht unter dem Bruchstrich. Beide Seiten mit t malnehmen und dann durch v teilen ergibt t = s : v.',
               'Werte einsetzen: t = 45 km : 18 km/h.', 'Ausrechnen: 45 : 18 = 2,5, und km : km/h ergibt h. Also ⟦t = 2,5 h⟧, zweieinhalb Stunden.'],
  'regel': 'So gehst du vor: zuerst die Formel nach der ⟦gesuchten Größe⟧ umstellen, dann die Werte ⟦mit Einheiten⟧ einsetzen und ausrechnen. Die Einheit des Ergebnisses verrät, ob du richtig umgestellt hast.',
  'fehler': 't = v : s = 18 : 45 = 0,4 h ist falsch – 45 km in 24 Minuten schafft kein Radfahrer. Prüfe mit den ⟦Einheiten⟧: km/h : km ergibt keine Zeit.'},
 'geometrie': {
  'einstieg': 'Ein dreieckiges Beet soll 24 m² groß werden. Die Seite am Zaun ist 8 m lang. Wie weit muss das Beet in den Garten hineinreichen? Die Flächenformel für Dreiecke kennst du – du musst sie nach der fehlenden Länge ⟦umstellen⟧.',
  'woerter': [['A = g · h : 2', 'Flächeninhalt eines Dreiecks: Grundseite g mal Höhe h, geteilt durch 2'], ['Höhe h', 'der senkrechte Abstand von der Grundseite zur gegenüberliegenden Ecke'],
              ['m², cm²', 'Quadratmeter, Quadratzentimeter – Einheiten für Flächen']],
  'schritte': ['Das Beet ist ein Dreieck mit A = 24 m² und g = 8 m. Gesucht ist die Höhe h.', 'Formel: A = g · h : 2. Zuerst das „: 2“ rückgängig machen: 2 · A = g · h.',
               'Dann beide Seiten durch g teilen: h = 2 · A : g.', 'Einsetzen: h = 48 m² : 8 m = ⟦6 m⟧.'],
  'regel': 'So berechnest du eine fehlende Länge: die Formel für ⟦Fläche⟧ oder ⟦Volumen⟧ aufschreiben, nach der Länge ⟦umstellen⟧, Werte einsetzen.'},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----

# Formel: (Anzeige, linke Seite, rechte Seite, {Variable: [(Anzeige, Python) – erste richtig]})
EIN = [
    ('v = s : t', 'v', 's/t', {'s': [('s = v · t', 'v*t'), ('s = v : t', 'v/t'), ('s = t : v', 't/v'), ('s = v + t', 'v+t')],
                               't': [('t = s : v', 's/v'), ('t = v · s', 'v*s'), ('t = v : s', 'v/s'), ('t = s − v', 's-v')]}),
    ('A = a · b', 'A', 'a*b', {'b': [('b = A : a', 'A/a'), ('b = A · a', 'A*a'), ('b = a : A', 'a/A'), ('b = A − a', 'A-a')]}),
    ('U = R · I', 'U', 'R*I', {'R': [('R = U : I', 'U/I'), ('R = U · I', 'U*I'), ('R = I : U', 'I/U')],
                               'I': [('I = U : R', 'U/R'), ('I = R : U', 'R/U'), ('I = U · R', 'U*R')]}),
    ('ρ = m : V', 'rho', 'm/V', {'m': [('m = ρ · V', 'rho*V'), ('m = ρ : V', 'rho/V'), ('m = V : ρ', 'V/rho')],
                                 'V': [('V = m : ρ', 'm/rho'), ('V = ρ : m', 'rho/m'), ('V = m · ρ', 'm*rho')]}),
    ('F = m · a', 'F', 'm*a', {'m': [('m = F : a', 'F/a'), ('m = F · a', 'F*a'), ('m = a : F', 'a/F'), ('m = F − a', 'F-a')]}),
    ('P = W : t', 'P', 'W/t', {'W': [('W = P · t', 'P*t'), ('W = P : t', 'P/t'), ('W = t : P', 't/P')],
                               't': [('t = W : P', 'W/P'), ('t = P : W', 'P/W'), ('t = W · P', 'W*P')]}),
    ('u = 4 · a', 'u', '4*a', {'a': [('a = u : 4', 'u/4'), ('a = u − 4', 'u-4'), ('a = 4 : u', '4/u'), ('a = 4 · u', '4*u')]}),
    ('V = G · h', 'V', 'G*h', {'h': [('h = V : G', 'V/G'), ('h = G : V', 'G/V'), ('h = V − G', 'V-G')],
                               'G': [('G = V : h', 'V/h'), ('G = V · h', 'V*h'), ('G = h : V', 'h/V')]}),
    ('p = F : A', 'p', 'F/A', {'F': [('F = p · A', 'p*A'), ('F = p : A', 'p/A'), ('F = A : p', 'A/p')],
                               'A': [('A = F : p', 'F/p'), ('A = p : F', 'p/F'), ('A = F · p', 'F*p')]}),
    ('d = 2 · r', 'd', '2*r', {'r': [('r = d : 2', 'd/2'), ('r = d − 2', 'd-2'), ('r = 2 · d', '2*d'), ('r = 2 : d', '2/d')]}),
    ('k = y : x', 'k', 'y/x', {'y': [('y = k · x', 'k*x'), ('y = k : x', 'k/x'), ('y = x : k', 'x/k')],
                               'x': [('x = y : k', 'y/k'), ('x = k : y', 'k/y'), ('x = k · y', 'k*y')]}),
    ('G = E − K', 'G', 'E-K', {'E': [('E = G + K', 'G+K'), ('E = G − K', 'G-K'), ('E = K − G', 'K-G')],
                               'K': [('K = E − G', 'E-G'), ('K = G − E', 'G-E'), ('K = E + G', 'E+G')]}),
]
ZWEI = [
    ('y = m · x + t', 'y', 'm*x+t', {'x': [('x = (y − t) : m', '(y-t)/m'), ('x = (y + t) : m', '(y+t)/m'), ('x = y : m − t', 'y/m-t'), ('x = (y − t) · m', '(y-t)*m')],
                                     't': [('t = y − m · x', 'y-m*x'), ('t = y + m · x', 'y+m*x'), ('t = m · x − y', 'm*x-y')]}),
    ('U = 2 · a + 2 · b', 'U', '2*a+2*b', {'a': [('a = (U − 2 · b) : 2', '(U-2*b)/2'), ('a = U : 2 − 2 · b', 'U/2-2*b'), ('a = (U − b) : 2', '(U-b)/2'), ('a = U − 2 · b', 'U-2*b')]}),
    ('A = g · h : 2', 'A', 'g*h/2', {'h': [('h = 2 · A : g', '2*A/g'), ('h = A : (2 · g)', 'A/(2*g)'), ('h = A : g', 'A/g'), ('h = 2 · g : A', '2*g/A')],
                                     'g': [('g = 2 · A : h', '2*A/h'), ('g = A : (2 · h)', 'A/(2*h)'), ('g = A · h : 2', 'A*h/2')]}),
    ('A = (a + c) · h : 2', 'A', '(a+c)*h/2', {'h': [('h = 2 · A : (a + c)', '2*A/(a+c)'), ('h = (a + c) : (2 · A)', '(a+c)/(2*A)'), ('h = 2 · A − (a + c)', '2*A-(a+c)'), ('h = A : (2 · (a + c))', 'A/(2*(a+c))')],
                                               'c': [('c = 2 · A : h − a', '2*A/h-a'), ('c = 2 · A − a : h', '2*A-a/h'), ('c = (2 · A − a) : h', '(2*A-a)/h'), ('c = A : (2 · h) − a', 'A/(2*h)-a')],
                                               'a': [('a = 2 · A : h − c', '2*A/h-c'), ('a = 2 · A : h + c', '2*A/h+c'), ('a = A : h − c', 'A/h-c'), ('a = 2 · A : (h − c)', '2*A/(h-c)')]}),
    ('V = G · h : 3', 'V', 'G*h/3', {'h': [('h = 3 · V : G', '3*V/G'), ('h = V : (3 · G)', 'V/(3*G)'), ('h = V : G', 'V/G'), ('h = 3 · G : V', '3*G/V')]}),
    ('F = 1,8 · C + 32', 'F', 'Fr(9,5)*C+32', {'C': [('C = (F − 32) : 1,8', '(F-32)/Fr(9,5)'), ('C = F : 1,8 − 32', 'F/Fr(9,5)-32'), ('C = (F + 32) : 1,8', '(F+32)/Fr(9,5)'), ('C = (F − 32) · 1,8', '(F-32)*Fr(9,5)')]}),
    ('Z = K · p : 100', 'Z', 'K*p/100', {'p': [('p = 100 · Z : K', '100*Z/K'), ('p = Z : (100 · K)', 'Z/(100*K)'), ('p = K · Z : 100', 'K*Z/100'), ('p = Z − K : 100', 'Z-K/100')],
                                         'K': [('K = 100 · Z : p', '100*Z/p'), ('K = Z : (100 · p)', 'Z/(100*p)'), ('K = p · Z : 100', 'p*Z/100')]}),
    ('K = G + n · p', 'K', 'G+n*p', {'n': [('n = (K − G) : p', '(K-G)/p'), ('n = K : p − G', 'K/p-G'), ('n = (K + G) : p', '(K+G)/p'), ('n = (K − G) · p', '(K-G)*p')],
                                     'p': [('p = (K − G) : n', '(K-G)/n'), ('p = K : n − G', 'K/n-G'), ('p = (K − n) : G', '(K-n)/G')]}),
    ('E = m · g · h', 'E', 'm*g*h', {'h': [('h = E : (m · g)', 'E/(m*g)'), ('h = E · m · g', 'E*m*g'), ('h = m · g : E', 'm*g/E'), ('h = E − m · g', 'E-m*g')]}),
    ('u = 2 · (a + b)', 'u', '2*(a+b)', {'a': [('a = u : 2 − b', 'u/2-b'), ('a = (u − b) : 2', '(u-b)/2'), ('a = u − 2 · b', 'u-2*b'), ('a = u : 2 + b', 'u/2+b')],
                                         'b': [('b = u : 2 − a', 'u/2-a'), ('b = (u − a) : 2', '(u-a)/2'), ('b = u − 2 · a', 'u-2*a'), ('b = u : 2 + a', 'u/2+a')]}),
    ('M = (a + b) : 2', 'M', '(a+b)/2', {'a': [('a = 2 · M − b', '2*M-b'), ('a = M : 2 − b', 'M/2-b'), ('a = 2 · (M − b)', '2*(M-b)'), ('a = M − 2 · b', 'M-2*b')]}),
]
NAMEN = {'rho': 'ρ'}

# Umformungsschritte je (Formel, gesuchte Größe)
WEG = {
    ('v = s : t', 's'): 'v = s : t | · t → s = v · t', ('v = s : t', 't'): 'v = s : t | · t → v · t = s | : v → t = s : v',
    ('A = a · b', 'b'): 'A = a · b | : a → b = A : a',
    ('U = R · I', 'R'): 'U = R · I | : I → R = U : I', ('U = R · I', 'I'): 'U = R · I | : R → I = U : R',
    ('ρ = m : V', 'm'): 'ρ = m : V | · V → m = ρ · V', ('ρ = m : V', 'V'): 'ρ = m : V | · V → ρ · V = m | : ρ → V = m : ρ',
    ('F = m · a', 'm'): 'F = m · a | : a → m = F : a',
    ('P = W : t', 'W'): 'P = W : t | · t → W = P · t', ('P = W : t', 't'): 'P = W : t | · t → P · t = W | : P → t = W : P',
    ('u = 4 · a', 'a'): 'u = 4 · a | : 4 → a = u : 4',
    ('V = G · h', 'h'): 'V = G · h | : G → h = V : G', ('V = G · h', 'G'): 'V = G · h | : h → G = V : h',
    ('p = F : A', 'F'): 'p = F : A | · A → F = p · A', ('p = F : A', 'A'): 'p = F : A | · A → p · A = F | : p → A = F : p',
    ('d = 2 · r', 'r'): 'd = 2 · r | : 2 → r = d : 2',
    ('k = y : x', 'y'): 'k = y : x | · x → y = k · x', ('k = y : x', 'x'): 'k = y : x | · x → k · x = y | : k → x = y : k',
    ('G = E − K', 'E'): 'G = E − K | + K → E = G + K', ('G = E − K', 'K'): 'G = E − K | + K → G + K = E | − G → K = E − G',
    ('y = m · x + t', 'x'): 'y = m · x + t | − t → y − t = m · x | : m → x = (y − t) : m', ('y = m · x + t', 't'): 'y = m · x + t | − m · x → t = y − m · x',
    ('U = 2 · a + 2 · b', 'a'): 'U = 2 · a + 2 · b | − 2 · b → U − 2 · b = 2 · a | : 2 → a = (U − 2 · b) : 2',
    ('A = g · h : 2', 'h'): 'A = g · h : 2 | · 2 → 2 · A = g · h | : g → h = 2 · A : g', ('A = g · h : 2', 'g'): 'A = g · h : 2 | · 2 → 2 · A = g · h | : h → g = 2 · A : h',
    ('A = (a + c) · h : 2', 'h'): 'A = (a + c) · h : 2 | · 2 → 2 · A = (a + c) · h | : (a + c) → h = 2 · A : (a + c)',
    ('A = (a + c) · h : 2', 'a'): 'A = (a + c) · h : 2 | · 2 → 2 · A = (a + c) · h | : h → 2 · A : h = a + c | − c → a = 2 · A : h − c',
    ('A = (a + c) · h : 2', 'c'): 'A = (a + c) · h : 2 | · 2 → 2 · A = (a + c) · h | : h → 2 · A : h = a + c | − a → c = 2 · A : h − a',
    ('V = G · h : 3', 'h'): 'V = G · h : 3 | · 3 → 3 · V = G · h | : G → h = 3 · V : G',
    ('F = 1,8 · C + 32', 'C'): 'F = 1,8 · C + 32 | − 32 → F − 32 = 1,8 · C | : 1,8 → C = (F − 32) : 1,8',
    ('Z = K · p : 100', 'p'): 'Z = K · p : 100 | · 100 → 100 · Z = K · p | : K → p = 100 · Z : K',
    ('Z = K · p : 100', 'K'): 'Z = K · p : 100 | · 100 → 100 · Z = K · p | : p → K = 100 · Z : p',
    ('K = G + n · p', 'n'): 'K = G + n · p | − G → K − G = n · p | : p → n = (K − G) : p', ('K = G + n · p', 'p'): 'K = G + n · p | − G → K − G = n · p | : n → p = (K − G) : n',
    ('E = m · g · h', 'h'): 'E = m · g · h | : (m · g) → h = E : (m · g)',
    ('u = 2 · (a + b)', 'a'): 'u = 2 · (a + b) | : 2 → u : 2 = a + b | − b → a = u : 2 − b',
    ('u = 2 · (a + b)', 'b'): 'u = 2 · (a + b) | : 2 → u : 2 = a + b | − a → b = u : 2 − a',
    ('M = (a + b) : 2', 'a'): 'M = (a + b) : 2 | · 2 → 2 · M = a + b | − b → a = 2 · M − b',
}
VARS = [*'vstAabUIRrmVFPWGhpdkyxEKCZnMugc', 'rho']


def probe(R, anz, lhs, rhs, var, richtig_anz, richtig_py):
    """Zahlenprobe: Werte wählen, mit der Formel rechnen, in die Umstellung einsetzen."""
    namen = sorted({n for n in VARS if re.search(rf'(?<![A-Za-z]){n}(?![A-Za-z])', rhs)} - {lhs})
    for _ in range(200):
        env = {n: Fr(R.randint(2, 9)) for n in namen}
        if anz.startswith('F = 1,8'): env['C'] = Fr(R.choice([5, 10, 15, 20, 25, 30]))
        env['Fr'] = Fr
        env[lhs] = eval(rhs, {}, env)
        ws = [env[n] for n in namen] + [env[lhs]]
        if ist_endlich(env[lhs]) and len(zt(env[lhs]).split(',')[-1]) <= 2 and env[lhs] > 1 and len(set(ws)) == len(ws): break
    zeig = lambda n: NAMEN.get(n, n)
    werte = ', '.join(f'{zeig(n)} = {zt(env[n])}' for n in namen)
    rechte = richtig_anz.split(' = ', 1)[1]
    eingesetzt = re.sub(r'(?<![A-Za-zρ])([A-Za-zρ])(?![A-Za-zρ])', lambda m: kl(env['rho' if m.group(1) == 'ρ' else m.group(1)]), rechte)
    assert eval(richtig_py, {}, env) == env[var]
    return f'Probe: {werte} → {zeig(lhs)} = {zt(env[lhs])}; {eingesetzt} = {zt(env[var])} ✓'


def tipp(anz, var):
    v = NAMEN.get(var, var)
    if '+' in anz or '−' in anz:
        return f'Was wurde mit {v} gerechnet? Mache zuerst das Plus/Minus rückgängig, dann das Mal/Geteilt.'
    return f'Was wurde mit {v} gemacht? Mache es mit der Umkehrrechnung rückgängig – das zuletzt Gerechnete zuerst.'


def pruefe_bank():
    """Richtige Umstellung erfüllt die Formel, falsche nicht (an Zufallswerten nachgerechnet)."""
    import random
    Rp = random.Random(4)
    for anz, lhs, rhs, ziele in EIN + ZWEI:
        for var, opts in ziele.items():
            unterschied = {t: False for t, _ in opts[1:]}
            for k in range(5):
                env = {n: Fr(Rp.randint(2, 40), Rp.randint(1, 7)) + Fr(1, 11) for n in [*'vstAabUIRrmVFPWGhpdkyxEKCZnMugc', 'rho']}
                env['Fr'] = Fr
                env[lhs] = eval(rhs, {}, env)                     # passende Werte erzeugen
                soll = env[var]
                assert eval(opts[0][1], {}, env) == soll, (anz, var, opts[0])
                for t, py in opts[1:]:
                    if eval(py, {}, env) != soll: unterschied[t] = True
            assert all(unterschied.values()), (anz, unterschied)


pruefe_bank()


def umstell_aufgabe(R, bank, st, h=None, nur=None):
    anz, lhs, rhs, ziele = R.choice(bank)
    var = nur if nur in ziele else R.choice(list(ziele))
    opts = ziele[var]
    v = NAMEN.get(var, var)
    return A(R, f'Stelle {anz} nach {v} um.', opts[0][0], [t for t, _ in opts[1:]],
             f'{WEG[(anz, var)]}. {probe(R, anz, lhs, rhs, var, *opts[0])}', tipp(anz, var))


# Gleiche Umkehrrechnung erst mit Zahlen, dann mit Buchstaben
ZAHL_BUCHSTABE = [('A = a · b', 'b', lambda a, b: f'{a * b} = {a} · b', lambda a, b: f'{a * b} : {a}', lambda a, b: b),
                  ('v = s : t', 't', lambda a, b: f'{a} = {a * b} : t', lambda a, b: f'{a * b} : {a}', lambda a, b: b),
                  ('U = R · I', 'I', lambda a, b: f'{a * b} = {a} · I', lambda a, b: f'{a * b} : {a}', lambda a, b: b),
                  ('p = F : A', 'F', lambda a, b: f'{a} = F : {b}', lambda a, b: f'{a} · {b}', lambda a, b: a * b),
                  ('G = E − K', 'E', lambda a, b: f'{a} = E − {b}', lambda a, b: f'{a} + {b}', lambda a, b: a + b)]


def g_ein_schritt(R, st):
    if st <= 2 and R.random() < .35:
        anz, var, gl, rech, erg = R.choice(ZAHL_BUCHSTABE)
        a, b = R.randint(2, 9), R.randint(2, 9)
        if st == 1:
            return Z(f'Aus {gl(a, b)} folgt {var} = ?', erg(a, b), rech(a, b).replace(' : ', ' / ').replace(' · ', ' * ').replace(' − ', ' - '),
                     f'{var} = {rech(a, b)} = {erg(a, b)} (Umkehrrechnung). Genauso stellst du die Formel {anz} um.',
                     'Mit welcher Umkehrrechnung bekommst du die Zahl für den Buchstaben?')
        e = [x for x in EIN if x[0] == anz][0]
        opts = e[3][var]
        return A(R, f'Aus {gl(a, b)} folgt {var} = {rech(a, b)} = {erg(a, b)}. Genauso: Aus {anz} folgt …', opts[0][0], [t for t, _ in opts[1:]],
                 f'Dieselbe Umkehrrechnung wie mit den Zahlen: {WEG[(anz, var)]}.', 'Mache mit den Buchstaben genau das, was du mit den Zahlen gemacht hast.')
    if (st == 3 and R.random() < .5) or (st == 2 and R.random() < .12):
        # Probe statt Rechnen
        art = R.choice(['rechteck', 'dichte', 'strom'])
        if art == 'rechteck':
            a, b = R.choice([4, 5, 8]), R.choice([2, 4, 5])
            A_ = a * b; fb = Fr(a, A_)
            t = f'Ein Rechteck hat A = {A_} cm² und a = {a} cm. Jemand rechnet b = a : A = {zt(fb)} cm. Welche Probe zeigt den Fehler?'
            ri = f'{a} · {zt(fb)} = {zt(a * fb)} und nicht {A_}'
            fa = [f'{zt(fb)} ist kleiner als {a}', 'Die Einheit cm stimmt nicht', f'{A_} : {a} = {b} ist größer als {zt(fb)}']
            w = f'Probe in A = a · b: {a} · {zt(fb)} = {zt(a * fb)} ≠ {A_}. Richtig: b = A : a = {b} cm.'
        elif art == 'dichte':
            rho, m = R.choice([(Fr(5, 2), 10), (Fr(2), 8), (Fr(5, 2), 20), (Fr(4), 12)])
            fV = rho / m
            t = f'Ein Stoff hat ρ = {zt(rho)} g/cm³, ein Stück wiegt m = {m} g. Jemand rechnet V = ρ : m = {zt(fV)} cm³. Welche Probe zeigt den Fehler?'
            ri = f'{zt(rho)} · {zt(fV)} = {zt(rho * fV)}, nicht {m}'
            fa = [f'{zt(fV)} ist kleiner als 1', f'{m} : {zt(rho)} = {zt(m / rho)}, also passt es', 'Die Einheit g stimmt nicht']
            w = f'Aus ρ = m : V folgt m = ρ · V. Probe: {zt(rho)} · {zt(fV)} = {zt(rho * fV)} ≠ {m}. Richtig: V = m : ρ = {zt(m / rho)} cm³.'
        else:
            U, R_ = R.choice([(12, 4), (24, 6), (230, 10), (9, 3)])
            fI = Fr(R_, U)
            t = f'An einem Widerstand R = {R_} Ω liegt U = {U} V. Jemand rechnet I = R : U = {ca_(fI)} A. Welche Probe zeigt den Fehler?'
            ri = f'{R_} · {ca_(fI)} ergibt etwa {zt(round(float(R_ * fI), 2)) if not ist_endlich(R_ * fI) else zt(R_ * fI)}, nicht {U}'
            fa = [f'{ca_(fI)} A ist zu klein für eine Stromstärke', f'{U} : {R_} = {zt(Fr(U, R_))} ist größer, also passt es', 'Die Einheit A stimmt nicht']
            w = f'Aus U = R · I: Probe {R_} · {ca_(fI)} ≈ {zt(round(float(R_ * fI), 2))} ≠ {U}. Richtig: I = U : R = {zt(Fr(U, R_))} A.'
        return A(R, t, ri, fa, w, 'Setze das Ergebnis in die ursprüngliche Formel ein.')
    if st == 3:
        # Zahl einsetzen nach dem Umstellen (Größe im Nenner)
        anz, var, frage = R.choice([('v = s : t', 't', 'v'), ('ρ = m : V', 'V', 'r'), ('p = F : A', 'A', 'p'), ('P = W : t', 't', 'P'), ('k = y : x', 'x', 'k')])
        z = Fr(R.randint(2, 25)) if R.random() < .6 else Fr(R.randint(5, 95), 10)
        g = Fr(R.randint(2, 12))
        oben = z * g
        sym = {'r': 'ρ'}.get(frage, frage)
        oben_n = {'v = s : t': 's', 'ρ = m : V': 'm', 'p = F : A': 'F', 'P = W : t': 'W', 'k = y : x': 'y'}[anz]
        return Z(f'Es gilt {anz}. Berechne {var} für {oben_n} = {zt(oben)} und {sym} = {zt(g)}.', z, f'{cz(oben)} / {cz(g)}',
                 f'Umstellen: {var} = {oben_n} : {sym} = {zt(oben)} : {zt(g)} = {zt(z)}.', f'Stelle zuerst nach {var} um. {var} steht im Nenner.')
    return umstell_aufgabe(R, EIN, st)


def ca_(x):
    return zt(x) if ist_endlich(x) and len(zt(x).split(',')[-1]) <= 3 else zt(round(float(x), 2))


MITTEL = {'n': 0}


def g_zwei_schritte(R, st):
    if st == 1:
        bank = [f for f in ZWEI if f[0] in ('y = m · x + t', 'A = g · h : 2', 'V = G · h : 3', 'K = G + n · p', 'E = m · g · h')]
        return umstell_aufgabe(R, bank, st)
    if st == 2 and R.random() < .55:
        return umstell_aufgabe(R, [f for f in ZWEI if f[0] not in ('A = (a + c) · h : 2', 'u = 2 · (a + b)')], st)
    if st == 3 and R.random() < .35:
        # gesuchte Größe steht in einer Klammer
        f = R.choice([x for x in ZWEI if x[0] in ('A = (a + c) · h : 2', 'u = 2 · (a + b)')])
        return umstell_aufgabe(R, [f], st, nur=R.choice(['c', 'a'] if f[0].startswith('A') else ['a', 'b']))
    # Stufe 3: umstellen und Zahl berechnen
    arten = ['lin', 'fahrenheit', 'trapez'] + (['mittel'] if MITTEL['n'] < 3 else [])
    art = R.choice(arten)
    if art == 'mittel': MITTEL['n'] += 1
    if art == 'lin':
        m, t = R.choice([2, 3, 4, 5, -2, -3]), R.randint(-9, 9)
        x = Fr(R.randint(-8, 8)); y = m * x + t
        return Z(f'Es gilt y = m · x + t mit m = {zt(m)} und t = {zt(t)}. Für welches x ist y = {zt(y)}?', x, f'({cz(y)} - ({t})) / ({m})',
                 f'x = (y − t) : m = ({zt(y)} − {"(" + zt(t) + ")" if t < 0 else zt(t)}) : {"(" + zt(m) + ")" if m < 0 else zt(m)} = {zt(x)}.', 'Stelle nach x um: x = (y − t) : m.')
    if art == 'fahrenheit':
        C = Fr(R.choice([-40, -20, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 100]))
        F = Fr(9, 5) * C + 32
        return Z(f'Für Temperaturen gilt F = 1,8 · C + 32 (F in Grad Fahrenheit, C in Grad Celsius). Wie viel Grad Celsius sind {zt(F)} °F?', C, f'({cz(F)} - 32) / 1.8',
                 f'C = (F − 32) : 1,8 = ({zt(F)} − 32) : 1,8 = {zt(C)}.', 'Stelle nach C um: erst − 32, dann : 1,8.', einheit='°C')
    if art == 'trapez':
        a, c, h = R.randint(4, 15), R.randint(2, 12), R.randint(2, 12)
        Af = Fr((a + c) * h, 2)
        return Z(f'Ein Trapez hat A = {zt(Af)} cm², a = {a} cm und h = {h} cm. Berechne c aus A = (a + c) · h : 2.', c, f'2 * {cz(Af)} / {h} - {a}',
                 f'c = 2 · A : h − a = {zt(2 * Af)} : {h} − {a} = {zt(2 * Af / h)} − {a} = {c} cm.', 'Stelle nach c um: · 2, dann : h, dann − a.', einheit='cm')
    while True:
        a, b, c = R.randint(1, 6), R.randint(1, 6), R.randint(1, 6)
        M = Fr(a + b + c, 3)
        if ist_endlich(M) and M not in (a, b, c) and a not in (b, c): break
    return Z(f'Der Mittelwert dreier Noten ist M = {zt(M)}. Zwei Noten sind {b} und {c}. Welche ist die dritte? Nutze M = (a + b + c) : 3.', a, f'3 * {cz(M)} - {b} - {c}',
             f'M = (a + b + c) : 3 | · 3 → 3 · M = a + b + c | − b − c → a = 3 · M − b − c = {zt(3 * M)} − {b} − {c} = {a}.', 'Stelle nach a um: erst · 3, dann die bekannten Noten abziehen.')


def g_einsetzen(R, st):
    art = R.choice({1: ['rad', 'strom', 'dichte'], 2: ['rad', 'strom', 'dichte', 'zins_p', 'tarif'], 3: ['zins_K', 'kraft', 'arbeit', 'einheit_v', 'einheit_m']}[st])
    if art == 'einheit_v':
        mi = R.choice([15, 20, 30, 40, 45, 90])
        v = R.choice([60, 80, 100, 120, 140, 160, 180, 200])
        s_ = Fr(v * mi, 60)
        if s_.denominator != 1: return g_einsetzen(R, st)
        return Z(f'Ein Zug fährt {zt(s_)} km in {mi} Minuten. Wie groß ist seine Durchschnittsgeschwindigkeit in km/h? (v = s : t)', v, f'{cz(s_)} / ({mi} / 60)',
                 f'Erst umrechnen: {mi} min = {zt(Fr(mi, 60))} h. v = s : t = {zt(s_)} km : {zt(Fr(mi, 60))} h = {v} km/h.',
                 'Rechne die Minuten zuerst in Stunden um.', einheit='km/h')
    if art == 'einheit_m':
        stoff, rho = R.choice([('Holz', Fr(6, 10)), ('Eis', Fr(9, 10)), ('Aluminium', Fr(27, 10)), ('Glas', Fr(5, 2))])
        V = R.choice([2, 3, 4, 5, 10])
        m = rho * V
        return Z(f'Ein Stück {stoff} (ρ = {zt(rho)} g/cm³) hat das Volumen {V} dm³. Wie schwer ist es in kg? (ρ = m : V)', m, f'{cz(rho)} * {V} * 1000 / 1000',
                 f'{V} dm³ = {V * 1000} cm³. m = ρ · V = {zt(rho)} g/cm³ · {V * 1000} cm³ = {zt(rho * V * 1000)} g = {zt(m)} kg.',
                 'Rechne dm³ zuerst in cm³ um. Am Ende g in kg.', einheit='kg')
    if art == 'rad':
        v = R.choice([12, 15, 16, 18, 20, 24, 25, 30, 40, 50, 60, 80, 90, 100, 120])
        t = Fr(R.choice([1, 2, 3, 5, 6, 8, 10, 12, 15]), R.choice([1, 2, 4]))
        s = v * t
        if s.denominator != 1: return g_einsetzen(R, st)
        return Z(f'Ein Fahrzeug legt {zt(s)} km mit der Durchschnittsgeschwindigkeit {v} km/h zurück. Wie lange braucht es? (v = s : t)', t, f'{cz(s)} / {v}',
                 f't = s : v = {zt(s)} km : {v} km/h = {zt(t)} h.', 'Stelle v = s : t nach t um. t steht im Nenner.', einheit='h')
    if art == 'strom':
        R_, I = R.choice([5, 10, 20, 25, 40, 50, 100, 200]), Fr(R.choice([1, 2, 3, 4, 5, 6, 8, 12]), R.choice([1, 2, 4, 10]))
        U = R_ * I
        return Z(f'An einem Widerstand von {R_} Ω liegt die Spannung {zt(U)} V. Wie groß ist die Stromstärke I? (U = R · I)', I, f'{cz(U)} / {R_}',
                 f'I = U : R = {zt(U)} V : {R_} Ω = {zt(I)} A.', 'Stelle U = R · I nach I um.', einheit='A')
    if art == 'dichte':
        stoff, rho = R.choice([('Aluminium', Fr(27, 10)), ('Eisen', Fr(79, 10)), ('Kupfer', Fr(89, 10)), ('Glas', Fr(5, 2)), ('Eis', Fr(9, 10))])
        V = Fr(R.choice([2, 4, 5, 10, 20, 25, 40, 50, 100]))
        m = rho * V
        if R.random() < .5:
            return Z(f'{stoff} hat die Dichte ρ = {zt(rho)} g/cm³. Ein Stück wiegt {zt(m)} g. Welches Volumen hat es? (ρ = m : V)', V, f'{cz(m)} / {cz(rho)}',
                     f'V = m : ρ = {zt(m)} g : {zt(rho)} g/cm³ = {zt(V)} cm³.', 'Stelle ρ = m : V nach V um.', einheit='cm³')
        return Z(f'{stoff} hat die Dichte ρ = {zt(rho)} g/cm³. Wie schwer ist ein Stück mit V = {zt(V)} cm³? (ρ = m : V)', m, f'{cz(rho)} * {cz(V)}',
                 f'm = ρ · V = {zt(rho)} · {zt(V)} = {zt(m)} g.', 'Stelle ρ = m : V nach m um.', einheit='g')
    if art == 'zins_p':
        K, p = R.choice([200, 400, 500, 800, 1000, 1200, 2000, 2500, 5000]), Fr(R.choice([5, 10, 15, 20, 25, 30, 40]), 10)
        Zi = K * p / 100
        return Z(f'Ein Guthaben von {zt(K)} € bringt in einem Jahr {zt(Zi)} € Zinsen. Wie hoch ist der Zinssatz p in Prozent? (Z = K · p : 100)', p, f'100 * {cz(Zi)} / {K}',
                 f'p = 100 · Z : K = 100 · {zt(Zi)} : {zt(K)} = {zt(p)}.', 'Stelle nach p um: erst · 100, dann : K.', einheit='%')
    if art == 'zins_K':
        K, p = R.choice([300, 600, 750, 1500, 2400, 3000, 4000, 6000]), Fr(R.choice([5, 10, 15, 20, 25, 30, 40]), 10)
        Zi = K * p / 100
        return Z(f'Bei einem Zinssatz von {zt(p)} % bekommt man in einem Jahr {zt(Zi)} € Zinsen. Wie groß ist das Guthaben K? (Z = K · p : 100)', K, f'100 * {cz(Zi)} / {cz(p)}',
                 f'K = 100 · Z : p = 100 · {zt(Zi)} : {zt(p)} = {zt(K)} €.', 'Stelle nach K um: erst · 100, dann : p.', einheit='€')
    if art == 'tarif':
        G, p = Fr(R.choice([5, 8, 10, 12, 15])), Fr(R.choice([5, 10, 15, 20, 25]), 10)
        n = R.randint(4, 30)
        K = G + n * p
        return Z(f'Ein Tarif kostet K = G + n · p mit G = {eur(G)} € und p = {eur(p)} € pro Stunde. Die Rechnung beträgt {eur(K)} €. Wie viele Stunden n wurden genutzt?', n, f'({cz(K)} - {cz(G)}) / {cz(p)}',
                 f'n = (K − G) : p = ({eur(K)} − {eur(G)}) : {eur(p)} = {n}.', 'Stelle nach n um: erst − G, dann : p.')
    if art == 'kraft':
        m, a = Fr(R.choice([2, 4, 5, 8, 10, 20, 25, 50, 80])), Fr(R.choice([1, 2, 3, 4, 5, 15, 25]), R.choice([1, 2, 10]))
        F = m * a
        return Z(f'Eine Kraft von {zt(F)} N beschleunigt einen Körper mit a = {zt(a)} m/s². Welche Masse hat er? (F = m · a)', m, f'{cz(F)} / {cz(a)}',
                 f'm = F : a = {zt(F)} : {zt(a)} = {zt(m)} kg.', 'Stelle F = m · a nach m um.', einheit='kg')
    m, h = Fr(R.choice([2, 5, 10, 20, 50, 60, 75])), Fr(R.choice([2, 3, 4, 5, 8, 10, 12, 15]))
    E = m * 10 * h
    return Z(f'Die Lageenergie ist E = m · g · h mit g = 10 N/kg. Ein Körper mit m = {zt(m)} kg hat E = {zt(E)} J. In welcher Höhe h ist er?', h, f'{cz(E)} / ({cz(m)} * 10)',
             f'h = E : (m · g) = {zt(E)} : ({zt(m)} · 10) = {zt(h)} m.', 'Stelle nach h um: durch das Produkt m · g teilen.', einheit='m')


def g_geometrie(R, st):
    art = R.choice({1: ['rechteck', 'quadrat', 'parallelogramm'], 2: ['dreieck', 'quader', 'rechteck_u', 'prisma'], 3: ['trapez', 'pyramide', 'quader', 'dreieck']}[st])
    if art == 'rechteck':
        a, b = R.randint(3, 20), R.randint(2, 15)
        return Z(f'Ein Rechteck hat den Flächeninhalt {a * b} cm² und die Länge {a} cm. Wie breit ist es?', b, f'{a * b} / {a}',
                 f'A = a · b → b = A : a = {a * b} : {a} = {b} cm.', 'Stelle A = a · b nach b um.', einheit='cm')
    if art == 'quadrat':
        a = Fr(R.randint(3, 60), R.choice([1, 2]))
        return Z(f'Ein Quadrat hat den Umfang {zt(4 * a)} cm. Wie lang ist eine Seite?', a, f'{cz(4 * a)} / 4',
                 f'u = 4 · a → a = u : 4 = {zt(4 * a)} : 4 = {zt(a)} cm.', 'Stelle u = 4 · a nach a um.', einheit='cm')
    if art == 'parallelogramm':
        g, h = R.randint(3, 20), R.randint(2, 15)
        return Z(f'Ein Parallelogramm hat A = {g * h} cm² und die Grundseite g = {g} cm. Berechne die Höhe h.', h, f'{g * h} / {g}',
                 f'A = g · h → h = A : g = {g * h} : {g} = {h} cm.', 'Stelle A = g · h nach h um.', einheit='cm')
    if art == 'dreieck':
        g, h = R.randint(3, 20), R.randint(2, 16)
        Af = Fr(g * h, 2)
        return Z(f'Ein Dreieck hat A = {zt(Af)} cm² und die Grundseite g = {g} cm. Berechne die Höhe h.', h, f'2 * {cz(Af)} / {g}',
                 f'A = g · h : 2 → h = 2 · A : g = {zt(2 * Af)} : {g} = {h} cm.', 'Stelle A = g · h : 2 nach h um. Vergiss die 2 nicht.', einheit='cm')
    if art == 'quader':
        a, b, c = R.randint(2, 12), R.randint(2, 10), R.randint(2, 15)
        return Z(f'Ein Quader hat das Volumen {a * b * c} cm³, die Länge {a} cm und die Breite {b} cm. Wie hoch ist er?', c, f'{a * b * c} / ({a} * {b})',
                 f'V = a · b · c → c = V : (a · b) = {a * b * c} : {a * b} = {c} cm.', 'Teile das Volumen durch die Grundfläche a · b.', einheit='cm')
    if art == 'rechteck_u':
        a, b = R.randint(3, 25), R.randint(2, 20)
        return Z(f'Ein Rechteck hat den Umfang {2 * (a + b)} cm und die Länge {a} cm. Wie breit ist es?', b, f'{2 * (a + b)} / 2 - {a}',
                 f'u = 2 · (a + b) → b = u : 2 − a = {a + b} − {a} = {b} cm.', 'Stelle u = 2 · (a + b) nach b um: erst : 2, dann − a.', einheit='cm')
    if art == 'prisma':
        G, h = R.randint(4, 40), R.randint(2, 15)
        return Z(f'Ein Prisma hat das Volumen {G * h} cm³ und die Grundfläche G = {G} cm². Wie hoch ist es?', h, f'{G * h} / {G}',
                 f'V = G · h → h = V : G = {G * h} : {G} = {h} cm.', 'Stelle V = G · h nach h um.', einheit='cm')
    if art == 'pyramide':
        G, h = R.randint(4, 40), R.randint(2, 15)
        V = Fr(G * h, 3)
        if not ist_endlich(V): return g_geometrie(R, st)
        return Z(f'Eine Pyramide hat das Volumen {zt(V)} cm³ und die Grundfläche {G} cm². Wie hoch ist sie? (V = G · h : 3)', h, f'3 * {cz(V)} / {G}',
                 f'h = 3 · V : G = {zt(3 * V)} : {G} = {h} cm.', 'Stelle V = G · h : 3 nach h um.', einheit='cm')
    a, c, h = R.randint(5, 16), R.randint(2, 12), R.randint(2, 12)
    Af = Fr((a + c) * h, 2)
    return Z(f'Ein Trapez hat A = {zt(Af)} cm² und die parallelen Seiten a = {a} cm und c = {c} cm. Berechne die Höhe h.', h, f'2 * {cz(Af)} / ({a} + {c})',
             f'A = (a + c) · h : 2 → h = 2 · A : (a + c) = {zt(2 * Af)} : {a + c} = {h} cm.', 'Stelle nach h um: · 2, dann durch (a + c).', einheit='cm')


def g_pruefen(R, st):
    bank = EIN if st == 1 else (ZWEI if st == 3 else EIN + ZWEI)
    anz, lhs, rhs, ziele = R.choice(bank)
    var = R.choice(list(ziele))
    opts = ziele[var]
    behauptet = R.choice(opts[:1] * 2 + opts[1:])
    richtig = behauptet == opts[0]
    falsch_rest = [t for t, _ in opts[1:] if t != behauptet[0]]
    if richtig:
        antw, andere = 'Ja, die Umstellung ist richtig.', [f'Nein, richtig wäre {t}.' for t in falsch_rest[:2]]
        if len(andere) < 2: andere.append('Nein, man kann die Formel nicht nach dieser Größe umstellen.')
    else:
        antw, andere = f'Nein, richtig wäre {opts[0][0]}.', ['Ja, die Umstellung ist richtig.'] + [f'Nein, richtig wäre {t}.' for t in falsch_rest[:1]]
    v = NAMEN.get(var, var)
    return A(R, f'Jemand stellt {anz} nach {v} um und erhält {behauptet[0]}. Stimmt das?', antw, andere,
             f'Richtig ist {opts[0][0]}: {WEG[(anz, var)]}. {probe(R, anz, lhs, rhs, var, *opts[0])}',
             'Mache die Probe mit einfachen Zahlen.')


GEN = {'ein_schritt': g_ein_schritt, 'zwei_schritte': g_zwei_schritte, 'einsetzen': g_einsetzen, 'geometrie': g_geometrie, 'pruefen': g_pruefen}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

def _tab(*zeilen):
    return {'typ': 'tabelle', 'kopf': ['Größe', 'Zeichen', 'Wert'], 'zeilen': [list(z) for z in zeilen]}


_OBST = [('Preis', 'P', '5 €'), ('Kilopreis', 'k', '2 €/kg')]
_TAXI = [('Kosten', 'K', '20 €'), ('Grundgebühr', 'G', '4 €'), ('Preis je km', 'p', '2 €')]
_RAD = [('Strecke', 's', '45 km'), ('Geschwindigkeit', 'v', '18 km/h')]
_DREI = {'A': [0, 0], 'B': [8, 0], 'C': [3, 6], '_H': [3, 0]}
UMBAU = {
 'ein_schritt': {
  'einstieg': 'An der Obsttheke gilt Preis = Kilopreis · Menge. Bei 2 € pro kg willst du wissen, wie viel du für 5 € bekommst. Dafür musst du die Formel ⟦umstellen⟧.',
  'woerter': [['Formel', 'eine Rechenvorschrift mit Buchstaben, z. B. P = k · m'], ['umstellen', 'so umschreiben, dass das Gesuchte allein steht'], ['Umkehrrechnung', 'die Rechnung, die etwas rückgängig macht: mal ↔ geteilt']],
  'bild': _tab(*_OBST, ('Menge', 'm', '?')),
  'schritte': [{'text': 'Die Formel ist P = k · m. Gesucht ist die Menge m.'},
               {'text': 'm wird mit k malgenommen. Die Umkehrrechnung ist: durch k teilen.'},
               {'text': 'Beide Seiten durch k teilen: ⟦m = P : k⟧.'},
               {'text': 'Mit Zahlen: m = 5 : 2 = 2,5. Du bekommst 2,5 kg.', 'bild': _tab(*_OBST, ('Menge', 'm', '2,5 kg'))}],
  'fehler': 'm = P · k wäre 5 · 2 = 10 kg für 5 € – viel zu viel. Was ⟦malgenommen⟧ wird, wird beim Umstellen geteilt.',
  'fehler_bild': _tab(*_OBST, ('Menge', 'm', '10 kg?')),
  'regel': 'Mach die Rechnung mit der ⟦Umkehrrechnung⟧ rückgängig. Mal wird zu geteilt, plus wird zu minus – auf beiden Seiten.'},
 'zwei_schritte': {
  'einstieg': 'Ein Taxi kostet 4 € Grundgebühr und 2 € pro Kilometer. Du hast 20 € bezahlt – wie weit bist du gefahren? Dafür machst du zwei Rechenschritte ⟦rückwärts⟧.',
  'woerter': [['Grundgebühr', 'Betrag, den man immer zahlt, auch für 0 km'], ['rückwärts', 'was zuletzt gerechnet wurde, machst du zuerst rückgängig']],
  'bild': _tab(*_TAXI, ('Strecke', 's', '?')),
  'schritte': [{'text': 'Die Formel ist K = G + p · s. Gesucht ist die Strecke s.'},
               {'text': '+ G kam zuletzt dazu, also zuerst abziehen: K − G = p · s.'},
               {'text': 'Dann beide Seiten durch p teilen: ⟦s = (K − G) : p⟧.'},
               {'text': 'Mit Zahlen: (20 − 4) : 2 = 8. Du bist 8 km gefahren.', 'bild': _tab(*_TAXI, ('Strecke', 's', '8 km'))}],
  'fehler': 's = K : p − G ist falsch: 20 : 2 − 4 = 6 km statt 8 km. Die Grundgebühr muss ⟦zuerst⟧ weg.',
  'fehler_bild': _tab(*_TAXI, ('Strecke', 's', '6 km?')),
  'regel': 'Gehe ⟦rückwärts⟧ vor: Was zuletzt gerechnet wurde, kommt zuerst weg. Meist erst plus oder minus, dann mal oder geteilt.'},
 'pruefen': {
  'einstieg': 'Ein quadratisches Beet bekommt einen Zaun: Umfang = 4 · Seitenlänge. Jemand stellt die Formel um und ist unsicher. Er probiert es aus – das ist die ⟦Probe mit Zahlen⟧.',
  'woerter': [['Umfang', 'die Länge einmal um die Figur herum'], ['Probe mit Zahlen', 'erfundene Werte einsetzen und vergleichen']],
  'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [3, 0], 'C': [3, 3], 'D': [0, 3]}, 'flaeche': ['A', 'B', 'C', 'D'],
           'linien': [['A', 'B', 'a'], ['B', 'C', 'a'], ['C', 'D', 'a'], ['D', 'A', 'a']]},
  'schritte': [{'text': 'Behauptung: Aus u = 4 · a folgt a = u − 4.'},
               {'text': 'Erfinde a = 3 m. Dann ist u = 4 · 3 = 12 m.',
                'bild': {'linien': [['A', 'B', '3 m'], ['B', 'C', '3 m'], ['C', 'D', '3 m'], ['D', 'A', '3 m']]}},
               {'text': 'In die Umstellung: 12 − 4 = 8. Herauskommen müsste aber 3.'},
               {'text': 'Also ist die Umstellung ⟦falsch⟧. Richtig ist a = u : 4.'}],
  'fehler': 'Ein Beispiel kann zufällig passen: a = u − 12 klappt bei a = 4. Mit a = 5 aber nicht mehr. Teste ⟦zwei verschiedene⟧ Zahlen.',
  'regel': 'Prüfe mit ⟦zwei erfundenen Zahlen⟧. Original und Umstellung müssen dasselbe ergeben. Nimm keine 0 und keine 1.'},
 'einsetzen': {
  'einstieg': 'Deine Radtour ist 45 km lang, du fährst im Schnitt 18 km pro Stunde. Wie lange bist du unterwegs? Erst umstellen, dann die Zahlen mit ⟦Einheiten⟧ einsetzen.',
  'woerter': [['Einheit', 'was hinter der Zahl steht: km, h, km/h'], ['v = s : t', 'Geschwindigkeit = Strecke : Zeit'], ['h', 'Abkürzung für Stunde']],
  'bild': _tab(*_RAD, ('Zeit', 't', '?')),
  'schritte': [{'text': 'Die Formel ist v = s : t. Gesucht ist die Zeit t.'},
               {'text': 'Mal t, dann durch v teilen: t = s : v.'},
               {'text': 'Einsetzen: t = 45 km : 18 km/h = ⟦2,5 h⟧.', 'bild': _tab(*_RAD, ('Zeit', 't', '2,5 h'))},
               {'text': 'km geteilt durch km/h ergibt h, also eine Zeit. Das passt.'}],
  'fehler': 't = v : s ergibt 0,4 h. Das ist falsch: 45 km in 24 Minuten schafft niemand. Die ⟦Einheit⟧ wäre auch keine Zeit.',
  'fehler_bild': _tab(*_RAD, ('Zeit', 't', '0,4 h?')),
  'regel': 'Erst ⟦nach der gesuchten Größe umstellen⟧, dann einsetzen. Die Einheit des Ergebnisses zeigt, ob es stimmt.'},
 'geometrie': {
  'einstieg': 'Ein dreieckiges Beet soll 24 m² groß werden, die Seite am Zaun ist 8 m lang. Wie weit reicht es in den Garten? Dafür stellst du die ⟦Flächenformel⟧ um.',
  'woerter': [['Flächenformel', 'A = g · h : 2 für das Dreieck'], ['Höhe', 'Abstand der Spitze von der Grundseite, senkrecht gemessen'], ['Grundseite g', 'die Seite, auf der die Höhe steht – hier am Zaun']],
  'bild': {'typ': 'figur', 'punkte': _DREI, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'B', 'g = 8 m'], ['C', '_H', 'h = ?', 'gestrichelt']], 'rechter_winkel': [['_H', 'B', 'C']]},
  'schritte': [{'text': 'Die Flächenformel ist A = g · h : 2. Grundseite g, Höhe h.'},
               {'text': 'Erst „: 2“ rückgängig machen: 2 · A = g · h.'},
               {'text': 'Dann durch g teilen: h = 2 · A : g.'},
               {'text': 'Einsetzen: h = 48 : 8 = ⟦6 m⟧.', 'bild': {'linien': [['A', 'B', 'g = 8 m'], ['C', '_H', 'h = 6 m', 'gestrichelt']]}}],
  'fehler': 'h = A : g = 3 m ist falsch: Das „: 2“ der Formel wurde vergessen. Ein so flaches Beet hätte nur ⟦12 m²⟧.',
  'fehler_bild': {'punkte': {**_DREI, 'C': [3, 3]}, 'linien': [['A', 'B', 'g = 8 m'], ['C', '_H', 'h = 3 m?', 'gestrichelt']]},
  'regel': 'Formel aufschreiben, ⟦nach der fehlenden Länge umstellen⟧, einsetzen. Bei Dreiecken das „: 2“ nicht vergessen.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): Grundwissen 8 bayerischer Gymnasien (Linsenformel nach einer Variablen auflösen und Werte
# einsetzen; Trapezformel umstellen), BMT10 2024 (Parameter einer Formel aus einem Messwert bestimmen), BMT8 2023 (Quaderhöhe aus Volumen in Litern),
# RS-Jahrgangsstufentest 8 2023 (Fehler in einer Rechnung finden), Physik-Formeln (U = R · I, ρ = m : V) wie in Schulaufgaben.
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_9)

# ein_schritt
SW.a('ein_schritt', 2, 'Stelle P = U · I nach I um.', 'I = P : U', ['I = U : P', 'I = P · U', 'I = P − U'], 'I wird mit U multipliziert. Umkehrung: durch U teilen: I = P : U.',
     'Welche Rechnung macht „· U“ rückgängig?')
SW.a('ein_schritt', 2, 'Stelle m = ρ · V nach ρ um.', 'ρ = m : V', ['ρ = V : m', 'ρ = m · V', 'ρ = m − V'], 'Durch V teilen: ρ = m : V.', 'Teile beide Seiten durch V.')
SW.z('ein_schritt', 3, 'Für einen elektrischen Widerstand gilt U = R · I. Ein Gerät nimmt bei 230 V eine Stromstärke von 0,5 A auf. Wie groß ist sein Widerstand R?', 460, '230 / 0.5',
     'R = U : I = 230 : 0,5 = 460 Ω.', 'Stelle nach R um. Durch 0,5 teilen heißt verdoppeln.', einheit='Ω', art='P')
SW.a('ein_schritt', 3, 'Für Linsen gilt 1/f = 1/g + 1/b. Stelle nach 1/b um.', '1/b = 1/f − 1/g', ['1/b = 1/g − 1/f', '1/b = 1/f + 1/g', 'b = f − g'],
     '1/g steht als Summand bei 1/b. Rückgängig: auf beiden Seiten 1/g abziehen: 1/b = 1/f − 1/g.', 'Behandle 1/g wie eine Zahl, die addiert wurde.', art='P')
SW.a('ein_schritt', 3, 'Es gilt v = s : t. Die Strecke s wird verdoppelt, die Zeit t halbiert. Was passiert mit v?', 'v wird viermal so groß.', ['v bleibt gleich.', 'v wird doppelt so groß.', 'v wird halbiert.'],
     'Doppeltes s verdoppelt v. Halbes t verdoppelt v noch einmal. Zusammen: 4-mal so groß. Beispiel: 100 : 20 = 5, 200 : 10 = 20.', 'Probiere mit Zahlen, z. B. s = 100, t = 20.', art='K')
SW.a('ein_schritt', 3, 'Für ein Dreieck gilt A = g · h : 2. Die Grundseite g wird verdreifacht. Wie muss sich h ändern, damit A gleich bleibt?', 'h muss gedrittelt werden.',
     ['h muss verdreifacht werden.', 'h muss um 3 kleiner werden.', 'h bleibt gleich.'],
     'A bleibt gleich, wenn g · h gleich bleibt. Bei 3-fachem g muss h ein Drittel so groß sein.', 'Wie hängen g und h zusammen, wenn A fest ist?', art='K')

# zwei_schritte
SW.a('zwei_schritte', 2, 'Stelle u = 2 · (l + b) nach b um.', 'b = u : 2 − l', ['b = u − 2 · l', 'b = (u − l) : 2', 'b = u : 2 + l'],
     'Erst durch 2 teilen: u : 2 = l + b. Dann l abziehen: b = u : 2 − l.', 'Was wurde zuletzt gerechnet? Das kommt zuerst weg.')
SW.a('zwei_schritte', 2, 'Stelle K = 5 + 0,2 · x nach x um.', 'x = (K − 5) : 0,2', ['x = K : 0,2 − 5', 'x = (K + 5) : 0,2', 'x = (K − 5) · 0,2'],
     'Erst 5 abziehen: K − 5 = 0,2 · x. Dann durch 0,2 teilen.', 'Zuerst plus/minus, dann mal/geteilt rückgängig machen.')
SW.a('zwei_schritte', 3, 'Stelle die Trapezformel A = (a + c) · h : 2 nach c um.', 'c = 2 · A : h − a', ['c = 2 · A : (h − a)', 'c = A : (2 · h) − a', 'c = 2 · A − a : h'],
     'Mal 2: 2A = (a + c) · h. Durch h: 2A : h = a + c. Minus a: c = 2 · A : h − a.', 'Mache die Schritte „: 2“, „· h“ und „+ a“ in umgekehrter Reihenfolge rückgängig.', art='P')
SW.z('zwei_schritte', 3, 'Für den Bremsweg auf nasser Straße gilt näherungsweise s = v² : k (v in km/h, s in m). Bei 50 km/h ist der Bremsweg 50 m lang. Bestimme k.', 50, '50**2 / 50',
     'Einsetzen: 50 = 2 500 : k ⇔ 50 · k = 2 500 ⇔ k = 50.', 'Setze die beiden Messwerte ein. Dann ist nur k unbekannt.', art='P')
SW.a('zwei_schritte', 3, 'Welche Formel ergibt nach x umgestellt x = y : 5 − 2?', 'y = 5 · (x + 2)', ['y = 5x + 2', 'y = 5x − 10', 'y = (x + 2) : 5'],
     'Rückwärts: x = y : 5 − 2 ⇔ x + 2 = y : 5 ⇔ y = 5 · (x + 2). Probe: y = 5x − 10 ergäbe x = y : 5 + 2.', 'Stelle x = y : 5 − 2 nach y um.', art='K')
SW.a('zwei_schritte', 3, 'Stelle a · x + b = c · x nach x um (a ≠ c).', 'x = b : (c − a)', ['x = b : (a − c)', 'x = (c − b) : a', 'x = c : (a + b)'],
     'Alle x nach rechts: b = c · x − a · x = (c − a) · x. Durch (c − a): x = b : (c − a).', 'Sammle beide x-Glieder auf einer Seite und klammere x aus.', art='K')

# pruefen
SW.a('pruefen', 2, 'Jemand stellt U = R · I nach R um und erhält R = U : I. Stimmt das?', 'Ja, die Umstellung ist richtig.', ['Nein, richtig wäre R = I : U.', 'Nein, richtig wäre R = U · I.'],
     'Probe mit R = 4, I = 3: U = 12. Umstellung: 12 : 3 = 4 ✓.', 'Prüfe mit zwei erfundenen Zahlen.')
SW.a('pruefen', 2, 'Jemand stellt s = v · t + 5 nach t um und erhält t = s : v − 5. Stimmt das?', 'Nein, richtig wäre t = (s − 5) : v.', ['Ja, die Umstellung ist richtig.', 'Nein, richtig wäre t = s : (v − 5).'],
     'Probe mit v = 2, t = 3: s = 11. Umstellung: 11 : 2 − 5 = 0,5 ≠ 3. Richtig: (11 − 5) : 2 = 3 ✓.', 'Was wurde zuletzt gerechnet: das Mal oder das Plus 5?')
SW.a('pruefen', 3, 'Jemand stellt 1/f = 1/g + 1/b nach f um und erhält f = g + b. Stimmt das?', 'Nein: Probe g = 2, b = 2 gibt 1/f = 1, also f = 1, nicht 4.',
     ['Ja: Kehrwerte darf man einzeln bilden.', 'Nein: richtig ist f = g − b.', 'Ja: Probe g = 2, b = 2 gibt f = 4.'],
     'Kehrwert einer Summe ist nicht die Summe der Kehrwerte. 1/2 + 1/2 = 1, also f = 1. Richtig: f = g · b : (g + b) = 4 : 4 = 1 ✓.', 'Setze für g und b dieselbe Zahl 2 ein.', art='P')
SW.a('pruefen', 3, 'Ist h = 2 · A : (a + c) die richtige Umstellung von A = (a + c) · h : 2?', 'Ja, die Umstellung ist richtig.', ['Nein, richtig wäre h = A : (2 · (a + c)).',
     'Nein, richtig wäre h = 2 · A : a + c.'],
     'Probe a = 2, c = 4, h = 3: A = 6 · 3 : 2 = 9. Umstellung: 2 · 9 : (2 + 4) = 18 : 6 = 3 ✓.', 'Erfinde a, c und h, berechne A und setze ein.', art='P')
SW.a('pruefen', 3, 'Jemand stellt A = a · b nach b um und erhält (falsch) b = A · a. Mit welcher Probezahl für a fällt der Fehler NICHT auf?', 'a = 1', ['a = 2', 'a = 5', 'a = 10'],
     'Für a = 1 ist A · 1 = A : 1. Beide Formeln geben dasselbe – der Fehler bleibt unentdeckt. Darum nimmt man keine 1 (und keine 0) zum Prüfen.',
     'Für welche Zahl ist „mal“ dasselbe wie „geteilt“?', art='K')
SW.a('pruefen', 3, 'Lea stellt M = (a + b + c) : 3 nach c um: c = 3 · M − a − b. Tom schreibt: c = 3 · (M − a − b). Wer hat recht?', 'Lea',
     ['Tom', 'beide', 'keiner'],
     'Probe a = b = c = 3: M = 3. Lea: 9 − 3 − 3 = 3 ✓. Tom: 3 · (3 − 6) = −9 ✗. Erst mal 3, dann a und b abziehen.', 'Prüfe beide mit denselben Zahlen.', art='K')

# einsetzen
SW.z('einsetzen', 2, 'Gold hat die Dichte ρ = 19,3 g/cm³. Ein Goldbarren wiegt 965 g. Welches Volumen hat er? (ρ = m : V)', 50, '965 / 19.3', 'V = m : ρ = 965 : 19,3 = 50 cm³.',
     'Stelle nach V um.', einheit='cm³')
SW.z('einsetzen', 2, 'Eine Lampe hat den Widerstand 920 Ω und liegt an 230 V. Wie groß ist die Stromstärke? (U = R · I)', 0.25, '230 / 920', 'I = U : R = 230 : 920 = 0,25 A.',
     'Stelle nach I um.', einheit='A')
SW.z('einsetzen', 3, 'Eine Regentonne fasst 210 Liter. Ihre Grundfläche beträgt 0,35 m². Wie hoch steht das Wasser, wenn sie voll ist? (V = G · h)', 60, '210 / 35 * 10',
     '210 l = 210 dm³, 0,35 m² = 35 dm². h = V : G = 210 : 35 = 6 dm = 60 cm.', 'Rechne alles in dm um: 1 l = 1 dm³, 1 m² = 100 dm².', einheit='cm', art='P')
SW.z('einsetzen', 3, 'Für Linsen gilt 1/f = 1/g + 1/b. Berechne f für g = 30 cm und b = 15 cm.', 10, '1 / (1/30 + 1/15)',
     '1/f = 1/30 + 2/30 = 3/30 = 1/10. Also f = 10 cm.', 'Rechne erst die rechte Seite mit Hauptnenner 30 aus. Dann den Kehrwert bilden.', einheit='cm', art='P')
SW.z('einsetzen', 3, 'Eine Läuferin schafft 400 m in 50 s. Wie schnell ist sie in km/h? (v = s : t)', 28.8, '400 / 50 * 3.6',
     'v = 400 m : 50 s = 8 m/s. In einer Stunde (3 600 s): 8 · 3 600 = 28 800 m = 28,8 km. Also 28,8 km/h.', 'Rechne erst m/s aus und dann auf eine Stunde hoch.', einheit='km/h', art='K')
SW.z('einsetzen', 3, 'Es gilt F = 1,8 · C + 32 (F in °F, C in °C). Bei welcher Celsius-Temperatur zeigen beide Skalen dieselbe Zahl?', -40, '32 / (1 - 1.8)',
     'Gleiche Zahl: C = 1,8 · C + 32 ⇔ −0,8 · C = 32 ⇔ C = −40. Probe: 1,8 · (−40) + 32 = −40.', 'Setze F = C und löse nach C.', einheit='°C', art='K')

# geometrie
SW.z('geometrie', 2, 'Ein Dreieck hat den Flächeninhalt 18 cm² und die Höhe 4 cm. Wie lang ist die zugehörige Grundseite?', 9, '2 * 18 / 4', 'g = 2 · A : h = 36 : 4 = 9 cm.',
     'A = g · h : 2. Das „: 2“ nicht vergessen.', einheit='cm')
SW.z('geometrie', 2, 'Ein Rechteck hat den Umfang 50 cm und die Breite 7,5 cm. Wie lang ist es?', 17.5, '50 / 2 - 7.5', 'u : 2 = l + b ⇔ 25 = l + 7,5 ⇔ l = 17,5 cm.',
     'Der halbe Umfang ist Länge plus Breite.', einheit='cm')
SW.z('geometrie', 3, 'Ein quaderförmiges Aquarium fasst 96 Liter. Es ist 6 dm lang und 4 dm breit. Wie hoch ist es?', 4, '96 / (6 * 4)',
     '96 l = 96 dm³. h = V : (l · b) = 96 : 24 = 4 dm.', '1 Liter = 1 dm³.', einheit='dm', art='P')
SW.z('geometrie', 3, 'Ein Quader mit der Grundfläche 5 cm × 8 cm hat dasselbe Volumen wie ein Würfel mit der Kantenlänge 10 cm. Wie hoch ist der Quader?', 25, '10**3 / (5 * 8)',
     'Würfel: V = 10 · 10 · 10 = 1 000 cm³. Quader: 40 cm² · h = 1 000 cm³ ⇔ h = 25 cm.', 'Berechne zuerst das Würfelvolumen.', einheit='cm', art='P')
SW.z('geometrie', 3, 'Ein Trapez hat den Flächeninhalt 54 cm² und die Höhe 6 cm. Eine der parallelen Seiten ist doppelt so lang wie die andere. Wie lang ist die kürzere?', 6, '54 * 2 / 6 / 3',
     'a + c = 2A : h = 108 : 6 = 18. Mit c = 2a: 3a = 18 ⇔ a = 6 cm (und c = 12 cm).', 'Stelle zuerst nach a + c um. Dann nutze c = 2a.', einheit='cm', art='K')
SW.z('geometrie', 3, 'Ein Rechteck hat den Umfang 30 cm. Seine Länge ist doppelt so groß wie seine Breite. Berechne den Flächeninhalt.', 50, '10 * 5',
     '2 · (2b + b) = 30 ⇔ 6b = 30 ⇔ b = 5 cm, l = 10 cm. A = 10 · 5 = 50 cm².', 'Drücke die Länge durch die Breite aus.', einheit='cm²', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Umstellen', ['ein_schritt', 'zwei_schritte', 'pruefen']), ('Anwenden', ['einsetzen', 'geometrie'])],
         'Formeln aus Geometrie, Physik und Alltag nach einer gesuchten Größe auflösen und damit rechnen.',
         ['Umkehrrechnung: Mal ↔ Geteilt, Plus ↔ Minus.', 'Rückwärts vorgehen: Was zuletzt gerechnet wurde, wird zuerst rückgängig gemacht.',
          'Probe mit Zahlen zeigt, ob eine Umstellung stimmt.'])
