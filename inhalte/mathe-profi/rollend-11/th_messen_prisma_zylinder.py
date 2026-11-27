T = "messen.prisma_zylinder"

# ───────── prisma_volumen: Brücke ─────────
assert [15 * h for h in (2, 4, 6, 8)] == [30, 60, 90, 120] and 15 * 2 / 5 == 6
Z(T, "prisma_volumen", "bruecke",
  "Ein gerades Prisma hat als Grundfläche ein rechtwinkliges Dreieck. Die Tabelle zeigt das Volumen des Prismas bei verschiedenen Körperhöhen. Eine Kathete des Dreiecks ist 5 cm lang. Wie lang ist die andere Kathete?",
  6, "30 / 2 * 2 / 5", "(120 / 8) / (5 / 2)",
  "Das Volumen ist Grundfläche mal Körperhöhe. Wie groß muss die Grundfläche sein, damit die Tabelle stimmt? Wie berechnet man die Fläche eines rechtwinkligen Dreiecks?",
  "Aus der Tabelle: V : h = 30 : 2 = 15, ebenso 60 : 4 = 15 usw. Die Grundfläche ist also 15 cm². Für ein rechtwinkliges Dreieck gilt G = Kathete · Kathete : 2. Also 5 · k : 2 = 15, 5 · k = 30 und k = 6 cm.",
  [(3, "15 / 5", "G = 5 · k gerechnet (das Teilen durch 2 vergessen)"),
   (7.5, "15 / 2", "die Grundfläche halbiert statt die Kathete zu bestimmen"),
   (30, "15 * 2", "G · 2 genannt, ohne durch die Kathete 5 zu teilen")],
  "id.flaeche_raum.aus_dem_quader", einheit="cm",
  grafik={"typ": "tabelle", "kopf": ["Körperhöhe in cm", "2", "4", "6", "8"], "zeilen": [["Volumen in cm³", "30", "60", "90", "120"]]})

# ───────── zylinder_oberflaeche: Umkehren ─────────
assert 2 * 5 * (5 + 10) == 150
Z(T, "zylinder_oberflaeche", "umkehren",
  "Ein gerader Zylinder hat den Radius 5 cm. Seine Oberfläche (Mantel, Boden und Deckel) beträgt 150π cm². Wie hoch ist der Zylinder?",
  10, "150 / (2 * 5) - 5", "(150 - 2 * 5 * 5) / (2 * 5)",
  "Die Oberfläche ist 2πr² + 2πrh. Teile beide Seiten durch π und ziehe dann das Stück für Boden und Deckel ab.",
  "O = 2πr² + 2πrh = 2πr(r + h). Mit r = 5: 150π = 10π(5 + h). Durch 10π teilen: 15 = 5 + h, also h = 10 cm. Probe: 2π · 25 + 2π · 5 · 10 = 50π + 100π = 150π.",
  [(15, "150 / (2 * 5)", "bei r + h stehen geblieben (den Radius nicht abgezogen)"),
   (25, "150 / 5 - 5", "den Faktor 2 aus 2πr vergessen"),
   (20, "150 / (2 * 5) + 5", "den Radius addiert statt abgezogen")],
  "id.flaeche_raum.haut", einheit="cm")
