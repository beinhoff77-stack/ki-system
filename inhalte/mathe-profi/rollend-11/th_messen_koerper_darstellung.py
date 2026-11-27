T = "messen.koerper_darstellung"

# ───────── prisma: Brücke ─────────
def prisma(n):
    return [str(2 * n), str(n + 2), str(3 * n)]


assert 27 // 3 + 2 == 11 and 3 * 9 == 27
Z(T, "prisma", "bruecke",
  "Die Tabelle zeigt, wie viele Ecken, Flächen und Kanten gerade Prismen haben, deren Grundfläche ein Vieleck ist. Ein solches Prisma hat 27 Kanten. Wie viele Flächen hat es?",
  11, "27 / 3 + 2", "9 + 2",
  "Suche in der Tabelle ein Muster: Wie hängt die Zahl der Kanten mit der Zahl der Ecken der Grundfläche zusammen?",
  "In der Tabelle ist die Kantenzahl das Dreifache der Eckenzahl der Grundfläche: 3 · 3 = 9, 3 · 4 = 12, 3 · 5 = 15, 3 · 6 = 18. Bei 27 Kanten hat die Grundfläche 27 : 3 = 9 Ecken. "
  "Die Flächenzahl ist immer 2 mehr als die Eckenzahl der Grundfläche (Grund- und Deckfläche kommen zu den Seitenflächen dazu): 9 + 2 = 11 Flächen.",
  [(9, "27 / 3", "die Eckenzahl der Grundfläche als Flächenzahl genannt"),
   (18, "27 / 3 * 2", "die Zahl der Ecken des Prismas genannt (2 · 9)"),
   (29, "27 + 2", "zur Kantenzahl 2 addiert statt zur Eckenzahl der Grundfläche")],
  "id.flaeche_raum.haut", einheit="Flächen",
  grafik={"typ": "tabelle", "kopf": ["Grundfläche", "3-Eck", "4-Eck", "5-Eck", "6-Eck"],
          "zeilen": [["Ecken"] + prisma(3)[:1] + [prisma(4)[0], prisma(5)[0], prisma(6)[0]],
                     ["Flächen"] + [prisma(n)[1] for n in (3, 4, 5, 6)],
                     ["Kanten"] + [prisma(n)[2] for n in (3, 4, 5, 6)]]})

# ───────── zylinder: Brücke ─────────
spur = {"A": (20, 9), "B": (28, 7), "C": (16, 12)}
flaechen = {k: u * h for k, (u, h) in spur.items()}
assert max(flaechen.values()) - min(flaechen.values()) == 16
Z(T, "zylinder", "bruecke",
  "Drei Dosen werden einmal auf dem Tisch abgerollt (eine ganze Umdrehung). Die Tabelle zeigt die Länge der Spur und die Höhe jeder Dose. "
  "Zu jeder Dose gehört ein Etikett, das genau einmal rund um den Mantel passt, ohne Überstand. Um wie viele Quadratzentimeter ist das größte Etikett größer als das kleinste?",
  16, "28 * 7 - 20 * 9", "196 - 180",
  "Wie lang ist die Spur im Vergleich zum Rand des Bodens? Welche Form hat ein Etikett, das man glatt auf den Tisch legt?",
  "Die Spur ist genau so lang wie der Umfang der Grundfläche. Das Etikett ist ein Rechteck mit Länge = Umfang und Breite = Höhe. A: 20 · 9 = 180 cm². B: 28 · 7 = 196 cm². C: 16 · 12 = 192 cm². "
  "Größtes Etikett B (196 cm²), kleinstes A (180 cm²): 196 − 180 = 16 cm².",
  [(12, "192 - 180", "das Etikett der Dose C als größtes genommen (C minus A)"),
   (5, "12 - 7", "nur die Höhen der Dosen verglichen"),
   (196, "28 * 7", "nur die Fläche des größten Etiketts genannt")],
  "id.flaeche_raum.haut", einheit="cm²",
  grafik={"typ": "tabelle", "kopf": ["Dose", "A", "B", "C"], "zeilen": [["Spur in cm", "20", "28", "16"], ["Höhe in cm", "9", "7", "12"]]})

# ───────── schraegbild: Umkehren ─────────
assert 8 * 6 * 6 == 288
Z(T, "schraegbild", "umkehren",
  "Ein Quader ist 8 cm breit und 6 cm hoch. Sein Volumen beträgt 288 cm³. Im Schrägbild wird die Tiefe halb so lang gezeichnet wie in Wirklichkeit. Wie lang ist die nach hinten führende Kante im Schrägbild?",
  3, "288 / (8 * 6) / 2", "(288 / 48) / 2",
  "Das Volumen ist Breite · Höhe · Tiefe. Welche Tiefe gehört zum Volumen? Was passiert damit im Bild?",
  "Volumen = Breite · Höhe · Tiefe, also Tiefe = 288 : (8 · 6) = 288 : 48 = 6 cm. Im Schrägbild wird die Tiefe halbiert: 6 : 2 = 3 cm. Probe: 8 · 6 · 6 = 288.",
  [(6, "288 / (8 * 6)", "die wahre Tiefe genannt, nicht die gezeichnete"),
   (12, "288 / (8 * 6) * 2", "die Tiefe im Bild verdoppelt statt halbiert"),
   (36, "288 / 8", "nur durch die Breite geteilt")],
  "id.flaeche_raum.aus_dem_quader", einheit="cm")
