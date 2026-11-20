#!/usr/bin/env python3
"""Expedition „Gartenpool“ (Klasse 8): Kreisumfang · Zylindervolumen · indirekte Proportionalität · Kreis- und Dreiecksfläche vergleichen.
Aufruf: python3 -I inhalte/generatoren/expedition_pool.py → inhalte/expeditionen/8-pool.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401
import math  # noqa: E402

D, WASSER = 3.6, 1.1
u = round(math.pi * D, 1)
v = round(math.pi * (D / 2) ** 2 * WASSER, 1)
assert (u, v) == (11.3, 11.2)
assert Fr(14 * 60, 3) == 280
wasserflaeche = math.pi * 1.8 ** 2
segel = 4 * 2.4 / 2
assert abs(wasserflaeche - 10.18) < 0.01 and segel == 4.8 and segel < wasserflaeche / 2 < 5.1

KU, ZV, I, KF = B('messen.kreisberechnung', 'umfang'), B('messen.prisma_zylinder', 'zylinder_volumen'), B('groessen.indirekt', 'sach'), B('messen.kreisberechnung', 'flaeche')
schreibe({
    'schluessel': '8-pool', 'titel': 'Gartenpool',
    'einleitung': 'Im Sommer wird im Garten ein runder Aufstellpool aufgebaut. Er hat innen 3,6 m Durchmesser und wird 1,1 m hoch mit Wasser gefüllt. '
                  'Gefüllt wird mit dem Gartenschlauch, und ein Sonnensegel soll das Wasser vor zu viel Sonne schützen.',
    'voraussetzungen': [KU, ZV, I, KF],
    'teile': [
        zahl('a', 'Der Pool hat 3,6 m Durchmesser. Um den oberen Rand soll einmal ganz herum ein Schaumstoffschutz gelegt werden. Wie viele Meter braucht man? Runde auf eine Nachkommastelle.',
             Fr('11.3'), f'round({PI} * 3.6, 1)',
             'Gegeben: d = 3,6 m. Gesucht: Länge einmal herum (Umfang). Ansatz: u = π · d. Rechnung: π · 3,6 ≈ 11,31. Antwort: Man braucht etwa 11,3 m.',
             'Einmal ganz herum ist der Umfang des Kreises.', KU, einheit='m', toleranz=0.1),
        zahl('b', 'Der Pool ist ein Zylinder mit 1,8 m Radius. Das Wasser steht 1,1 m hoch. Wie viele m³ Wasser sind im Pool? Runde auf eine Nachkommastelle.',
             Fr('11.2'), f'round({PI} * 1.8 ** 2 * 1.1, 1)',
             'Gegeben: r = 1,8 m, Wasserhöhe 1,1 m. Gesucht: Wasservolumen. Ansatz: V = π · r² · h. Rechnung: π · 3,24 · 1,1 ≈ 11,20. Antwort: Im Pool sind etwa 11,2 m³ (rund 11 200 Liter) Wasser.',
             'Welche Höhe zählt – die des Pools oder die des Wassers?', ZV, einheit='m³', toleranz=0.1),
        zahl('c', 'Mit einem Gartenschlauch dauert das Füllen 14 Stunden. Der Nachbar leiht zwei weitere, gleich starke Schläuche aus. Wie viele Minuten dauert das Füllen mit allen drei Schläuchen?',
             280, '14 * 60 / 3',
             'Gegeben: 1 Schlauch → 14 h, jetzt 3 gleich starke Schläuche. Gesucht: Zeit in Minuten. Ansatz: Anzahl der Schläuche · Zeit bleibt gleich (indirekt proportional). '
             'Rechnung: 14 h = 840 min; 840 : 3 = 280. Antwort: Mit drei Schläuchen dauert es 280 Minuten (4 h 40 min).',
             'Drei Schläuche schaffen dreimal so viel pro Stunde. Rechne am Ende in Minuten um.', I, einheit='min'),
        auswahl('d', 'Die Wasserfläche ist ein Kreis mit 1,8 m Radius. Ein dreieckiges Sonnensegel hat eine 4 m lange Grundseite und ist 2,4 m hoch. '
                     'Selbst wenn die gesamte Segelfläche Schatten auf das Wasser wirft: Ist das Segel groß genug, um mindestens die Hälfte der Wasserfläche zu beschatten?',
                'Nein: Das Segel hat 4,8 m², die Hälfte der Wasserfläche sind etwa 5,1 m².',
                ['Ja: Das Segel ist größer als die halbe Wasserfläche.', 'Ja, weil die Grundseite mit 4 m länger ist als der Durchmesser von 3,6 m.', 'Das kann man nicht entscheiden, weil ein Dreieck und ein Kreis verschiedene Formen haben.'],
                'Gegeben: Kreis r = 1,8 m, Dreieck g = 4 m, h = 2,4 m. Gesucht: Ist das Dreieck mindestens halb so groß wie der Kreis? '
                'Ansatz: A_Kreis = π · r², A_Dreieck = g · h : 2. Rechnung: π · 3,24 ≈ 10,18 m², die Hälfte ≈ 5,09 m²; 4 · 2,4 : 2 = 4,8 m². 4,8 < 5,09. '
                'Antwort: Das Segel ist etwas zu klein.',
                'Berechne beide Flächen. Die längere Grundseite allein entscheidet nichts.', KF),
    ],
})
