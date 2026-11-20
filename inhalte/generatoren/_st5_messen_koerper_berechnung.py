"""Zwanzigste Runde, Klasse 5: messen.koerper_berechnung – Typen, neue Übungen, Knobel-Bordkarten (siehe _stufen_kl5.py)."""
from _stufen_kl5 import A, Z

KARTEN = {
 'quader': {
  'leiter': ('Kanten von Würfel und Quader zählen und die Kantenlänge insgesamt berechnen.',
             'Kantensummen bei Quadern, eine Kante aus der Kantensumme bestimmen, Flächen, Kanten und Ecken zusammen.',
             'Kantenmodelle rückwärts, Flächen am Quader, Netze und angemalte Würfel, Fehler bei der Kantensumme.'),
  'typ': [(r'Kantenmodell eines Quaders', 'rueckwaerts'), (r'größte Seitenfläche|Würfelnetz besteht', 'verknuepfen'), (r'Ist das ein Würfelnetz|rot angemalt', 'transfer'),
          (r'Draht wird das Kantenmodell|Alle Kanten eines Würfels sind zusammen', 'umkehr'), (r'8 Ecken, 12 Kanten|Wie viele Kanten hat|Wie viele seiner Kanten', 'erkennen'),
          (r'Flächen, Kanten und Ecken', 'darstellung'), (r'^Ein Würfel hat die Kantenlänge', 'direkt'), (r'^Ein Quader ist', 'mehrschritt')],
  'neu': [
   ('einkleidung', Z('Für ein Kantenmodell eines Würfels mit 15 cm Kantenlänge braucht man Holzstäbe. Wie viele Meter Holz sind das insgesamt?', 1.8, '12 * 15 / 100', '12 Kanten · 15 cm = 180 cm = 1,8 m.', 'Wie viele Kanten hat ein Würfel?', einheit='m')),
   ('fehler', A('Jemand sagt: „Ein Quader mit 4 cm, 3 cm und 2 cm hat Kanten von zusammen 9 cm.“ Was ist falsch?', 'Jede Kantenlänge kommt viermal vor: 4 · (4 + 3 + 2) = 36 cm.', ['Nichts, das stimmt.', 'Richtig sind 18 cm.', 'Richtig sind 24 cm.'],
                'Ein Quader hat je 4 gleich lange Kanten in Länge, Breite und Höhe.', 'Wie oft kommt jede Kantenlänge vor?')),
  ],
  'knobel': [
   Z('Ein großer Würfel aus 3 · 3 · 3 kleinen Würfeln wird außen rot angemalt. Wie viele kleine Würfel haben gar keine rote Fläche?', 1, '1', 'Nur der Würfel ganz in der Mitte berührt keine Außenfläche: 1.', 'Welche kleinen Würfel liegen ganz innen?'),
   Z('Für das Kantenmodell eines Quaders braucht man genau 60 cm Draht. Länge, Breite und Höhe sind ganze cm und alle verschieden. Wie viele verschiedene Quader sind möglich (ohne Rücksicht auf die Reihenfolge)?', 12, '12',
     'Länge + Breite + Höhe = 60 : 4 = 15. Drei verschiedene Zahlen mit Summe 15: (1, 2, 12), (1, 3, 11), (1, 4, 10), (1, 5, 9), (1, 6, 8), (2, 3, 10), (2, 4, 9), (2, 5, 8), (2, 6, 7), (3, 4, 8), (3, 5, 7), (4, 5, 6) – das sind 12.',
     'Was müssen Länge, Breite und Höhe zusammen ergeben? Zähle dann systematisch.'),
  ],
 },
 'oberflaeche': {
  'leiter': ('Die Oberfläche eines Würfels oder Quaders mit Hilfe einer Tabelle berechnen.',
             'Oberflächen ohne Hilfe berechnen, aus einer Seitenfläche die Oberfläche bestimmen, Gegenstände lackieren.',
             'Kanten aus der Oberfläche zurückrechnen, Vergrößerungen und Schnitte deuten, Einheiten mischen, Fehler (Volumen statt Oberfläche) erklären.'),
  'typ': [(r'Wie lang ist eine Kante|Wie lang sind alle seine Kanten', 'rueckwaerts'), (r'doppelt so lang|verdoppelt|durchgeschnitten', 'transfer'), (r'dm lang|mm breit', 'verknuepfen'),
          (r'Oberfläche 94', 'pruefung'), (r'Was ist falsch', 'fehler'), (r'Seitenfläche', 'umkehr'), (r'Die Tabelle hilft|^Berechne die Oberfläche eines Würfels', 'direkt'), (r'.', 'mehrschritt')],
  'neu': [
   ('erkennen', A('Aus wie vielen Rechtecken besteht die Oberfläche eines Quaders?', '6', ['4', '8', '12'], 'Ein Quader hat 6 Flächen: je 2 gleiche gegenüber.', 'Zähle oben/unten, vorne/hinten, links/rechts.')),
   ('einkleidung', Z('Ein Spielwürfel aus Holz hat 2 cm Kantenlänge. Er wird ganz lackiert. Wie viele cm² werden lackiert?', 24, '6 * 2 * 2', '6 Quadrate zu je 4 cm²: 24 cm².', 'Wie viele gleiche Flächen hat ein Würfel?', einheit='cm²')),
  ],
  'knobel': [
   Z('Ein Quader hat die Kanten 1 cm, 2 cm und 3 cm. Zwei solche Quader werden so zusammengeklebt, dass die Oberfläche möglichst klein wird. Wie groß ist sie?', 32, '2 * 22 - 2 * 6',
     'Ein Quader hat 2 · (2 + 3 + 6) = 22 cm². Beim Kleben verschwinden zwei Flächen. Am meisten spart man mit den größten Flächen (2 cm · 3 cm = 6 cm²): 44 − 12 = 32 cm².', 'Welche Flächen sollte man aufeinanderkleben?', einheit='cm²'),
   Z('Ein Würfel hat die Oberfläche 150 cm². Er wird in 8 gleich große kleine Würfel zerschnitten. Wie groß ist die Oberfläche aller kleinen Würfel zusammen?', 300, '8 * 6 * 25 // 4',
     'Kante des großen Würfels: 150 : 6 = 25 = 5 · 5, also 5 cm. Kleine Würfel: Kante 2,5 cm, je 6 · 6,25 = 37,5 cm². 8 · 37,5 = 300 cm² – doppelt so viel wie vorher.', 'Bestimme zuerst die Kantenlänge des großen Würfels.', einheit='cm²'),
  ],
 },
 'sachaufgaben': {
  'leiter': ('Die Oberfläche einer Schachtel berechnen, die ganz beklebt wird.',
             'Behälter ohne Deckel, nur einige Seiten, aus der Papiermenge die Kante bestimmen.',
             'Zimmer und Becken mit Aussparungen, Zuschläge, mehrere Gegenstände, Fehler bei offenen Behältern.'),
  'typ': [(r'Zimmer', 'pruefung'), (r'Zehntel|Schwimmbecken|steht mittig', 'transfer'), (r'Holzwürfel|Fliesen', 'verknuepfen'), (r'rechnet jemand', 'fehler'),
          (r'ohne Deckel', 'mehrschritt'), (r'nur an den vier Seiten', 'einkleidung'), (r'.', 'direkt')],
  'neu': [
   ('erkennen', A('Ein Aquarium hat keinen Deckel. Aus wie vielen Glasflächen besteht es?', '5', ['6', '4', '8'], 'Boden und vier Seiten: 5 Flächen.', 'Welche Fläche fehlt?')),
   ('umkehr', Z('Für einen Würfel braucht man genau 54 cm² Papier, um ihn ganz zu bekleben. Wie lang ist eine Kante?', 3, '3', 'Eine Fläche: 54 : 6 = 9 cm² = 3 cm · 3 cm. Kante 3 cm.', 'Wie groß ist eine Fläche?', einheit='cm')),
  ],
  'knobel': [
   Z('Ein Karton ohne Deckel ist 20 cm lang, 20 cm breit und 10 cm hoch. Er wird innen und außen mit Folie beklebt. Wie viele cm² Folie braucht man?', 2400, '2 * (400 + 4 * 200)', 'Eine Seite des Kartons: Boden 400 cm² und vier Wände je 200 cm², zusammen 1 200 cm². Innen und außen: 2 400 cm².', 'Rechne erst eine Seite (innen oder außen) aus.', einheit='cm²'),
   Z('Aus einem Quadrat von 30 cm × 30 cm Pappe schneidet man an jeder Ecke ein Quadrat von 5 cm × 5 cm aus und faltet die Ränder hoch. Wie viele cm² Pappe hat die offene Schachtel?', 800, '900 - 4 * 25',
     'Die Schachtel besteht aus der Pappe, die übrig bleibt: 900 cm² − 4 · 25 cm² = 800 cm².', 'Muss man die Schachtel wirklich ausrechnen?', einheit='cm²'),
  ],
 },
 'zusammengesetzt': {
  'leiter': ('Die Oberfläche von zwei zusammengeklebten Würfeln bestimmen.',
             'Türme und Reihen aus mehreren Würfeln, Pakete einpacken, aus der Oberfläche auf die Anzahl schließen.',
             'Quader auf verschiedene Arten zusammenkleben, Würfel auf Quadern, Bauformen vergleichen, Fehler beim Addieren erklären.'),
  'typ': [(r'Was ist falsch', 'fehler'), (r'einmal mit den', 'verknuepfen'), (r'Zwei gleiche Quader', 'transfer'), (r'mittig ein Würfel', 'pruefung'), (r'2 · 2 · 2', 'transfer'),
          (r'der vierte sitzt', 'verknuepfen'), (r'einmal eine Reihe und einmal', 'begruenden'), (r'^2 Würfel mit 1 cm', 'direkt'), (r'.', 'mehrschritt')],
  'neu': [
   ('erkennen', A('Zwei Würfel werden zusammengeklebt. Wie viele Würfelflächen fehlen dadurch in der Oberfläche?', '2', ['1', '4', '0'], 'Die beiden Klebeflächen liegen innen – eine von jedem Würfel.', 'Welche Flächen sieht man nach dem Kleben nicht mehr?')),
   ('erkennen', A('Drei Würfel werden in einer Reihe zusammengeklebt. Wie viele Würfelflächen liegen innen und gehören nicht zur Oberfläche?', '4', ['2', '3', '6'], 'Zwei Klebestellen mit je zwei Flächen: 4.', 'Wie viele Klebestellen gibt es?')),
   ('direkt', Z('Ein Würfel mit 1 cm Kantenlänge hat die Oberfläche 6 cm². Wie viele cm² Oberfläche haben zwei solche Würfel, wenn sie einzeln nebeneinanderliegen (nicht geklebt)?', 12, '2 * 6', 'Nicht geklebt: Alle Flächen bleiben sichtbar, 2 · 6 = 12 cm².', 'Geht beim bloßen Nebeneinanderlegen eine Fläche verloren?', einheit='cm²')),
   ('einkleidung', Z('Zwei Kartons (je 30 cm × 20 cm × 10 cm) werden mit den großen Flächen (30 cm × 20 cm) aufeinandergestellt und zusammen eingepackt. Wie viele cm² Papier braucht man mindestens?', 3200, '2 * 2200 - 2 * 600',
                     'Ein Karton: 2 · (600 + 300 + 200) = 2 200 cm². Zwei: 4 400 cm². Die beiden Auflageflächen (je 600 cm²) fallen weg: 3 200 cm².', 'Welche Flächen werden nicht beklebt?', einheit='cm²')),
   ('umkehr', Z('Eine Reihe aus gleichen Würfeln mit 1 cm Kantenlänge hat die Oberfläche 22 cm². Wie viele Würfel sind es?', 5, '(22 - 2) // 4', 'Jeder Würfel trägt 4 cm² an den Seiten bei, dazu kommen die beiden Enden (2 cm²): 4 · n + 2 = 22, also n = 5.', 'Wie viele Flächen jedes Würfels sieht man?')),
  ],
  'knobel': [
   Z('Zehn Würfel mit 1 cm Kantenlänge werden zu einem Turm aufeinandergestapelt. Wie groß ist die Oberfläche des Turms?', 42, '4 * 10 + 2', 'Jeder Würfel zeigt 4 Seitenflächen: 40 cm². Dazu oben und unten je 1 cm²: 42 cm².', 'Welche Flächen jedes Würfels sind sichtbar?', einheit='cm²'),
   Z('Aus 4 Würfeln mit 1 cm Kantenlänge wird ein Körper gebaut (Würfel immer mit ganzen Flächen aneinander). Wie groß ist die kleinste mögliche Oberfläche?', 16, '4 * 6 - 2 * 4',
     'Jede Klebestelle spart 2 cm². Eine Reihe oder ein L hat 3 Klebestellen: 24 − 6 = 18 cm². Das 2 · 2-Quadrat hat 4 Klebestellen: 24 − 8 = 16 cm².', 'Wie viele Klebestellen kann man mit 4 Würfeln höchstens haben?', einheit='cm²'),
  ],
 },
 'volumen': {
  'leiter': ('Das Volumen eines Quaders aus Einheitswürfeln abzählen.',
             'Volumen mit der Formel berechnen, eine Kante aus dem Volumen bestimmen, Kartons und Behälter.',
             'Würfel zerlegen, fehlende Kanten rückwärts, Liter und Füllhöhen, Vergrößerungen deuten.'),
  'typ': [(r'in kleine Würfel', 'transfer'), (r'hat das Volumen \d+ cm³\. (Er|Seine)', 'rueckwaerts'), (r'Aquarium', 'verknuepfen'), (r'Schachtel', 'pruefung'),
          (r'verdreifacht', 'begruenden'), (r'Wie lang ist eine Kante', 'umkehr'), (r'^Berechne das Volumen', 'mehrschritt'), (r'.', 'direkt')],
  'neu': [
   ('erkennen', A('Welche Einheit passt zum Volumen?', 'cm³', ['cm²', 'cm', 'kg'], 'Volumen misst man in Würfeln: cm³.', 'Was ist ein Kubikzentimeter?')),
   ('erkennen', A('Wie viele Einheitswürfel (1 cm³) passen in einen Würfel mit 2 cm Kantenlänge?', '8', ['4', '6', '2'], '2 · 2 · 2 = 8 Einheitswürfel.', 'Zwei Schichten zu je 2 · 2 Würfeln.')),
   ('einkleidung', Z('Ein Schuhkarton ist 30 cm lang, 20 cm breit und 10 cm hoch. Wie viele cm³ passen hinein?', 6000, '30 * 20 * 10', '30 · 20 · 10 = 6 000 cm³.', 'Länge mal Breite mal Höhe.', einheit='cm³')),
  ],
  'knobel': [
   Z('Ein Quader aus Einheitswürfeln hat das Volumen 24 cm³ und ist 2 cm hoch. Wie viele verschiedene Grundflächen (Länge · Breite in ganzen cm, gedreht nicht neu) sind möglich?', 3, '3', 'Die Grundfläche muss 24 : 2 = 12 cm² haben: 1 · 12, 2 · 6, 3 · 4. Das sind 3.', 'Wie groß muss die Grundfläche sein?'),
   Z('Wie viele Würfel mit 1 cm Kantenlänge braucht man für einen hohlen Würfel mit 5 cm Außenkante und 1 cm dicken Wänden?', 98, '5 ** 3 - 3 ** 3', 'Voller Würfel: 125. Innen hohl bleibt ein Würfel mit 3 cm Kante: 27. 125 − 27 = 98.', 'Rechne den vollen Würfel minus den leeren Innenraum.'),
  ],
 },
 'verstehen': {
  'leiter': ('Einfache Aussagen über Würfel und Quader prüfen.',
             'Aussagen über Oberfläche, Kanten und Volumen mit einer kleinen Rechnung prüfen, Alltagsangaben prüfen.',
             'Zusammenhänge zwischen Volumen und Oberfläche begründen oder widerlegen, typische Fehler erklären.'),
  'typ': [(r'Oberfläche 62|alle Kanten zusammen 24|Volumen 24 cm³', 'mehrschritt'), (r'Klebt man zwei Würfel', 'darstellung'),
          (r'achtmal|gleichem Volumen|größerem Volumen', 'begruenden'), (r'5 × 4 × 3', 'transfer'), (r'verdoppelt sich die Oberfläche|Was ist falsch', 'fehler'),
          (r'Welche Aussage über jeden Quader', 'pruefung'), (r'dieselbe Maßzahl', 'parameter'), (r'.', 'erkennen')],
  'neu': [
   ('direkt', Z('Wie viele Ecken hat ein Würfel?', 8, '8', 'Ein Würfel hat 8 Ecken: 4 oben, 4 unten.', 'Zähle oben und unten.')),
   ('umkehr', A('Stimmt die Aussage? „Ein Würfel mit dem Volumen 27 cm³ hat 3 cm lange Kanten.“', 'Ja: 3 · 3 · 3 = 27.', ['Nein: Die Kanten sind 9 cm lang.', 'Nein: Die Kanten sind 27 cm lang.', 'Nein: Man kann die Kante nicht bestimmen.'],
                'Probe: 3 cm · 3 cm · 3 cm = 27 cm³.', 'Welche Zahl dreimal mit sich selbst malgenommen ergibt 27?')),
   ('einkleidung', A('Stimmt die Aussage? „Für einen Würfelkarton mit 10 cm Kantenlänge reichen 500 cm² Geschenkpapier.“', 'Nein: Man braucht mindestens 6 · 100 cm² = 600 cm².', ['Ja, das reicht.', 'Ja, man braucht nur 400 cm².', 'Nein: Man braucht 1 000 cm².'],
                     'Oberfläche: 6 Quadrate zu je 100 cm² = 600 cm².', 'Berechne die Oberfläche.')),
  ],
  'knobel': [
   Z('Ein Quader hat ganzzahlige Kantenlängen. Alle Kanten zusammen sind 24 cm lang, die Oberfläche ist 22 cm². Wie groß ist sein Volumen?', 6, '1 * 2 * 3',
     'Länge + Breite + Höhe = 24 : 4 = 6. Möglichkeiten: 1, 1, 4 (Oberfläche 18), 1, 2, 3 (Oberfläche 2 · (2 + 3 + 6) = 22), 2, 2, 2 (24). Passend ist 1 · 2 · 3: Volumen 6 cm³.', 'Was ergeben die drei Kantenlängen zusammen?', einheit='cm³'),
   Z('Ein Würfel mit 3 cm Kantenlänge wird in Würfel mit 1 cm Kantenlänge zerschnitten. Um wie viele cm² ist die Oberfläche aller kleinen Würfel zusammen größer als die des großen Würfels?', 108, '27 * 6 - 6 * 9',
     'Großer Würfel: 6 · 9 = 54 cm². 27 kleine Würfel: 27 · 6 = 162 cm². Unterschied 108 cm².', 'Wie viele kleine Würfel entstehen?', einheit='cm²'),
  ],
 },
}
