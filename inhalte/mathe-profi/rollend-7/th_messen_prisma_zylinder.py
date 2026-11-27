T = "messen.prisma_zylinder"
import math
P = "3.141592653589793"
# ───────── prisma_volumen ─────────
neu(T, "prisma_volumen", "lueckenweg", L(
    "Ein gerades Prisma hat als Grundfläche ein Dreieck mit der Grundseite 9 cm und der zugehörigen Höhe 4 cm. Das Prisma ist 15 cm hoch. Die Grundfläche ist ① cm² groß. Das Volumen ist ② cm³.",
    KOMM(2), [18, 270], ["9 * 4 / 2", "{1} * 15"], ["36 // 2", "18 * 15"], "Die Grundfläche des Dreiecks ist die Hälfte von Grundseite mal Höhe. Das Volumen ist Grundfläche mal Körperhöhe.",
    "G = 9 · 4 : 2 = 18 cm². V = 18 · 15 = 270 cm³.",
    {0: [(36, "fb.aus_dem_rechteck.halbieren_vergessen", "das Halbieren vergessen", "9 * 4")], 1: [(540, "fb.aus_dem_rechteck.halbieren_vergessen", "mit der Rechteckfläche 36 gerechnet", "9 * 4 * 15")]}), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "prisma_volumen", "zwei_wege", Z(
    "Ein gerades Prisma hat als Grundfläche ein rechtwinkliges Dreieck mit den Katheten 6 cm und 5 cm. Das Prisma ist 8 cm hoch. Berechne das Volumen auf zwei Wegen. Weg A: Grundfläche des Dreiecks mal Körperhöhe. Weg B: Zwei solche Prismen ergeben zusammen einen Quader mit den Kanten 6 cm, 5 cm und 8 cm, das Prisma ist also die Hälfte davon. Wie groß ist das Volumen?",
    120, "6 * 5 / 2 * 8", "6 * 5 * 8 / 2", "Beide Wege müssen dasselbe Volumen ergeben.",
    "Weg A: G = 6 · 5 : 2 = 15 cm², V = 15 · 8 = 120 cm³. Weg B: Der Quader hat 6 · 5 · 8 = 240 cm³, die Hälfte ist 120 cm³.",
    [(240, "fb.aus_dem_rechteck.halbieren_vergessen", "das Halbieren vergessen", "6 * 5 * 8"), (19, None, "6 + 5 + 8 gerechnet", "6 + 5 + 8")], "cm³"), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "prisma_volumen", "anwenden", Z(
    "Ein Zelt hat die Form eines liegenden geraden Prismas. Die Grundfläche ist ein Dreieck, die Zeltöffnung: 4 m breit und 2,5 m hoch. Das Zelt ist 6 m lang. Wie viel Kubikmeter Luft passen in das Zelt?",
    30, "4 * 2.5 / 2 * 6", "5 * 6", "Die Öffnung ist die Grundfläche, die Länge des Zelts ist die Körperhöhe.",
    "G = 4 · 2,5 : 2 = 5 m². V = 5 · 6 = 30 m³. Es passen 30 m³ Luft hinein.",
    [(60, "fb.aus_dem_rechteck.halbieren_vergessen", "das Halbieren vergessen", "4 * 2.5 * 6"), (12.5, None, "4 + 2,5 + 6 gerechnet", "4 + 2.5 + 6")], "m³"), g="einkleidung", regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── prisma_oberflaeche ─────────
neu(T, "prisma_oberflaeche", "lueckenweg", L(
    "Ein gerades Prisma hat als Grundfläche ein Rechteck mit den Seiten 3 cm und 4 cm. Es ist 10 cm hoch. Die Grundfläche ist ① cm². Der Mantel ist ein Rechteck mit der Höhe 10 cm und dem Umfang der Grundfläche als Länge. Er ist ② cm² groß. Die Oberfläche ist ③ cm².",
    KOMM(3), [12, 140, 164], ["3 * 4", "(3 + 4) * 2 * 10", "2 * {1} + {2}"], ["12", "14 * 10", "24 + 140"], "Die Oberfläche besteht aus zwei Grundflächen und dem Mantel.",
    "G = 12 cm². Umfang 14 cm, Mantel 14 · 10 = 140 cm². O = 2 · 12 + 140 = 164 cm².",
    {1: [(70, None, "nur den halben Umfang genommen", "(3 + 4) * 10")], 2: [(152, "fb.haut.nur_drei_flaechen", "nur eine Grundfläche gerechnet: 12 + 140", "{1} + {2}")]}), regel="id.flaeche_raum.haut")
neu(T, "prisma_oberflaeche", "fehler_detektiv", FD(
    "Kim berechnet die Oberfläche eines geraden Prismas mit einem Quadrat als Grundfläche. Die Seite des Quadrats ist 5 cm lang, die Körperhöhe des Prismas ist 8 cm.",
    [("Grundfläche: 5 · 5 = 25 cm².", 5 * 5 == 25), ("Mantel: Umfang der Grundfläche 4 · 5 = 20 cm, mal die Körperhöhe 8 cm = 160 cm².", 4 * 5 * 8 == 160), ("Oberfläche: Mantel plus eine Grundfläche, also 160 + 25 = 185 cm².", 160 + 25 == 160 + 2 * 25)],
    "Wie viele Grundflächen hat ein Prisma?", "Ein Prisma hat zwei Grundflächen: Grund- und Deckfläche. O = 2 · 25 + 160 = 210 cm²."), regel="id.flaeche_raum.haut")
neu(T, "prisma_oberflaeche", "bruecke", W(
    "Die Tabelle zeigt alle Teilflächen des Netzes eines geraden Dreiecksprismas. Wie groß ist die Oberfläche?",
    "132 cm²", [("126 cm²", "nur eine Grundfläche gezählt: 6 + 120"), ("120 cm²", "nur den Mantel gezählt"), ("252 cm²", "die drei Rechtecke doppelt gezählt: 12 + 2 · 120")],
    "Rechne Anzahl mal Fläche je Stück für jede Zeile und addiere.",
    "2 · 6 = 12 cm². Mantel: 30 + 40 + 50 = 120 cm². O = 12 + 120 = 132 cm².",
    lambda: 2 * 6 + 30 + 40 + 50 == 132 and 6 + 120 == 126 and 30 + 40 + 50 == 120 and 12 + 2 * 120 == 252,
    grafik=TAB(["Teil des Netzes", "Anzahl", "Fläche je Stück"], ["Dreieck", "2", "6 cm²"], ["Rechteck 3 cm × 10 cm", "1", "30 cm²"], ["Rechteck 4 cm × 10 cm", "1", "40 cm²"], ["Rechteck 5 cm × 10 cm", "1", "50 cm²"])), regel="id.flaeche_raum.haut")

# ───────── prisma_umstellen ─────────
neu(T, "prisma_umstellen", "lueckenweg", L(
    "Ein gerades Prisma hat das Volumen 720 cm³ und die Grundfläche 48 cm². Die Höhe ist ① cm. Ein zweites gerades Prisma hat dieselbe Grundfläche und die doppelte Höhe. Seine Höhe ist ② cm und sein Volumen ③ cm³.",
    KOMM(3), [15, 30, 1440], ["720 // 48", "2 * {1}", "48 * {2}"], ["15", "30", "1440"], "Das Volumen ist Grundfläche mal Höhe. Stelle um: Höhe = Volumen : Grundfläche.",
    "h = 720 : 48 = 15 cm. Doppelte Höhe: 30 cm. V = 48 · 30 = 1 440 cm³.",
    {0: [(768, None, "720 + 48 gerechnet", "720 + 48"), (34560, None, "720 · 48 gerechnet", "720 * 48")], 2: [(720, None, "das Volumen des ersten Prismas übernommen", "720")]}), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "prisma_umstellen", "umkehren", Z(
    "Ein gerades Prisma hat die Grundfläche 45 cm² und die Höhe 12 cm. Ein zweites gerades Prisma hat dasselbe Volumen. Seine Grundfläche ist ein Quadrat und seine Höhe ist 15 cm. Wie lang ist eine Seite dieses Quadrats?",
    6, "6", 6, "Berechne zuerst das Volumen. Daraus folgt die Grundfläche des zweiten Prismas.",
    "V = 45 · 12 = 540 cm³. Grundfläche des zweiten: 540 : 15 = 36 cm². Das Quadrat hat die Seite 6 cm, denn 6 · 6 = 36.",
    [(36, None, "die Grundfläche statt der Seitenlänge angegeben", "45 * 12 / 15"), (18, None, "36 : 2 gerechnet statt die Wurzel zu ziehen", "36 / 2"), (540, None, "das Volumen statt der Seitenlänge angegeben", "45 * 12")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.aus_dem_rechteck")
assert 45 * 12 // 15 == 36 and 6 * 6 == 36
neu(T, "prisma_umstellen", "anwenden", Z(
    "Ein Aquarium hat die Form eines Quaders. Der Boden ist 80 cm lang und 40 cm breit. Das Aquarium fasst 96 Liter. Wie hoch ist es? Es gilt 1 Liter = 1 000 cm³.",
    30, "96 * 1000 / (80 * 40)", 30, "Rechne die Liter in cm³ um. Stelle dann V = G · h nach h um.",
    "96 l = 96 000 cm³. G = 80 · 40 = 3 200 cm². h = 96 000 : 3 200 = 30 cm.",
    [(3, "fb.groesse.flaeche_mit_zehn", "in dm statt in cm angegeben: 96 : (8 · 4)", "96 / (8 * 4)"), (1200, None, "96 · 1000 : 80 gerechnet, die Breite vergessen", "96 * 1000 / 80"), (0.3, None, "in m statt cm angegeben", "30 / 100")], "cm"), g="einkleidung", regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── zylinder_volumen ─────────
neu(T, "zylinder_volumen", "lueckenweg", L(
    "Eine Konservendose ist ein Zylinder mit dem Radius 4 cm und der Höhe 10 cm. Die Grundfläche ist ① · π cm². Das Volumen ist ② · π cm³. Mit π ≈ 3 ist das Volumen etwa ③ cm³.",
    KOMM(3), [16, 160, 480], ["4 ** 2", "{1} * 10", "3 * {2}"], ["16", "160", "3 * 160"], "Die Grundfläche ist ein Kreis: Radius mal Radius mal π.",
    "G = π · 4² = 16π cm². V = 16π · 10 = 160π cm³. Mit π ≈ 3: 480 cm³.",
    {0: [(8, "fb.potenz.basis_mal_hochzahl", "4 · 2 statt 4² gerechnet", "4 * 2")], 1: [(40, None, "4 · 10 gerechnet, die Grundfläche vergessen", "4 * 10")]}), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "zylinder_volumen", "zwei_wege", Z(
    "Ein Zylinder hat den Radius 5 cm und die Höhe 12 cm. Berechne sein Volumen in cm³ auf ganze Zahlen gerundet auf zwei Wegen. Weg A: mit π ≈ 3,14. Weg B: mit der π-Taste des Taschenrechners. Beide Wege führen auf dieselbe ganze Zahl. Welchen Wert erhältst du?",
    942, "3.14 * 5 ** 2 * 12", f"round({P} * 5 ** 2 * 12)", "Beide Wege dürfen sich nur in der Rundung unterscheiden.",
    "Weg A: 3,14 · 25 · 12 = 942. Weg B: π · 25 · 12 ≈ 942,48, gerundet 942. Das Volumen beträgt etwa 942 cm³.",
    [(471, None, "durch 2 geteilt", "3.14 * 5 ** 2 * 12 / 2"), (377, "fb.potenz.basis_mal_hochzahl", "5² als 5 · 2 gerechnet: π · 5 · 2 · 12", "round(3.14 * 5 * 2 * 12)"), (3768, "fb.aus_dem_rechteck.durchmesser_statt_radius", "den Radius 5 verdoppelt, also mit 10 quadriert: π · 10² · 12", "3.14 * 10 ** 2 * 12")], "cm³"), regel="id.flaeche_raum.aus_dem_rechteck")
assert round(math.pi * 25 * 12) == 942 and round(3.14 * 25 * 12) == 942
neu(T, "zylinder_volumen", "umkehren", Z(
    "Ein Zylinder ist 10 cm hoch. Sein Volumen beträgt etwa 785 cm³. Wie groß ist sein Radius in cm? Runde auf ganze cm.",
    5, "5", 5, "Stelle V = π · r² · h nach r² um. Welche Zahl mal sich selbst gibt das?",
    "r² = 785 : (π · 10) ≈ 25. Also r = 5 cm. Probe: π · 25 · 10 ≈ 785.",
    [(25, None, "r² statt r angegeben", "round(785 / (3.141592653589793 * 10))"), (12.5, None, "25 durch 2 geteilt statt die Wurzel zu ziehen", "25 / 2"), (10, None, "die Höhe statt des Radius angegeben", "10")], "cm"), g="rueckwaerts", regel="id.flaeche_raum.aus_dem_rechteck")
assert round((785 / (math.pi * 10)) ** 0.5) == 5

# ───────── zylinder_oberflaeche ─────────
neu(T, "zylinder_oberflaeche", "lueckenweg", L(
    "Ein Zylinder hat den Radius 3 cm und die Höhe 8 cm. Eine Grundfläche ist ① · π cm² groß. Der Mantel ist ein Rechteck mit der Höhe 8 cm und dem Kreisumfang als Länge. Er ist ② · π cm² groß. Die Oberfläche ist ③ · π cm².",
    KOMM(3), [9, 48, 66], ["3 ** 2", "2 * 3 * 8", "2 * {1} + {2}"], ["9", "48", "18 + 48"], "Der Kreisumfang ist 2 mal π mal Radius. Die Oberfläche hat zwei Grundflächen und einen Mantel.",
    "G = 9π. Mantel: 2π · 3 · 8 = 48π. O = 2 · 9π + 48π = 66π cm².",
    {1: [(24, None, "den Kreisumfang nur mit r · π gerechnet: 3 · 8", "3 * 8"), (96, "fb.aus_dem_rechteck.durchmesser_statt_radius", "den Durchmesser 6 statt des Radius im Umfang genommen: 2 · 6 · 8", "2 * 6 * 8")], 2: [(57, "fb.haut.nur_drei_flaechen", "nur eine Grundfläche gezählt: 9 + 48", "{1} + {2}")]}), regel="id.flaeche_raum.haut")
neu(T, "zylinder_oberflaeche", "bruecke", W(
    "Das Netz eines Zylinders besteht aus zwei Kreisen und einem Rechteck, wie die Tabelle zeigt. Welche Formel gibt die Oberfläche eines Zylinders mit Radius r und Höhe h an?",
    "2πr² + 2πrh", [("πr² + 2πrh", "nur einen Kreis gezählt"), ("2πr² + πrh", "den Kreisumfang ohne die 2 benutzt"), ("2πr + 2πh", "Längen statt Flächen addiert")],
    "Zähle die Flächen der Tabelle zusammen: Anzahl mal Fläche je Stück.",
    "Zwei Kreise: 2 · π · r². Das Rechteck hat die Länge 2πr und die Breite h: 2πrh. Zusammen 2πr² + 2πrh.",
    lambda: gl("2*n*a**2+2*n*a*b", "2*n*a**2+2*n*a*b") and not gl("2*n*a**2+2*n*a*b", "n*a**2+2*n*a*b") and not gl("2*n*a**2+2*n*a*b", "2*n*a**2+n*a*b") and not gl("2*n*a**2+2*n*a*b", "2*n*a+2*n*b"),
    grafik=TAB(["Teil des Netzes", "Anzahl", "Fläche je Stück"], ["Kreis mit Radius r", "2", "π · r²"], ["Rechteck (Mantel)", "1", "2 · π · r · h"])), regel="id.flaeche_raum.haut")
neu(T, "zylinder_oberflaeche", "anwenden", Z(
    "Eine Blechdose hat den Durchmesser 8 cm und die Höhe 11 cm. Sie hat Boden, Deckel und Mantel. Wie viel Quadratzentimeter Blech braucht man für eine Dose, wenn nichts verschnitten wird? Rechne mit der π-Taste und runde auf ganze cm².",
    377, f"round(2 * {P} * 4 ** 2 + 2 * {P} * 4 * 11)", 377, "Der Radius ist halb so groß wie der Durchmesser.",
    "r = 4 cm. Zwei Kreise: 2 · π · 16 ≈ 100,5. Mantel: 2 · π · 4 · 11 ≈ 276,5. O ≈ 377,0 cm², gerundet 377 cm². (Mit π ≈ 3,14 erhält man 376,8, gerundet ebenfalls 377.)",
    [(239, None, "den Mantel mit π · 4 · 11 statt 2π · 4 · 11 gerechnet", f"round(2 * {P} * 4 ** 2 + {P} * 4 * 11)"), (955, "fb.aus_dem_rechteck.durchmesser_statt_radius", "mit dem Durchmesser 8 als Radius gerechnet", f"round(2 * {P} * 8 ** 2 + 2 * {P} * 8 * 11)"), (276, "fb.haut.nur_drei_flaechen", "nur den Mantel gerechnet", f"round(2 * {P} * 4 * 11)")], "cm²"), g="einkleidung", regel="id.flaeche_raum.haut")
assert round(2 * math.pi * 16 + 2 * math.pi * 4 * 11) == 377

# ───────── sach ─────────
neu(T, "sach", "lueckenweg", L(
    "Ein Schwimmbecken ist ein gerades Prisma mit einer rechteckigen Grundfläche von 10 m mal 5 m. Es ist 2 m tief. Es fasst ① m³. In einen Kubikmeter passen 1 000 Liter, also fasst es ② Liter. Eine Pumpe schafft 4 000 Liter in der Stunde. Das Füllen dauert ③ Stunden.",
    KOMM(3), [100, 100000, 25], ["10 * 5 * 2", "{1} * 1000", "{2} // 4000"], ["100", "100 * 1000", "100000 // 4000"], "Volumen = Länge mal Breite mal Tiefe. Dann in Liter umrechnen.",
    "V = 10 · 5 · 2 = 100 m³ = 100 000 l. 100 000 : 4 000 = 25. Das Füllen dauert 25 Stunden.",
    {0: [(17, None, "10 + 5 + 2 gerechnet", "10 + 5 + 2")], 1: [(10000, "fb.stellenwert.eine_stelle_daneben", "eine Null zu wenig: mal 100 statt mal 1 000", "{1} * 100")], 2: [(250, None, "100 000 : 400 gerechnet", "{2} // 400")]}), regel="id.flaeche_raum.aus_dem_quader")
neu(T, "sach", "anwenden", Z(
    "Ein zylinderförmiger Wassertank hat den Durchmesser 2 m und die Höhe 3 m. Eine Pumpe füllt ihn mit 500 Litern in der Minute. Wie viele Minuten dauert es, den leeren Tank ganz zu füllen? Runde auf ganze Minuten. Es gilt 1 m³ = 1 000 Liter.",
    19, f"round({P} * 1 ** 2 * 3 * 1000 / 500)", 19, "Berechne erst das Volumen in m³. Rechne dann in Liter um.",
    "r = 1 m. V = π · 1² · 3 ≈ 9,42 m³ ≈ 9 425 l. 9 425 : 500 ≈ 18,85. Es dauert etwa 19 Minuten.",
    [(9425, None, "das Volumen in Litern als Minuten angegeben", f"round({P} * 3 * 1000)"), (9, None, "das Volumen in m³ als Minuten genommen", f"round({P} * 3)"), (75, "fb.aus_dem_rechteck.durchmesser_statt_radius", "mit dem Durchmesser 2 als Radius gerechnet: π · 2² · 3", f"round({P} * 2 ** 2 * 3 * 1000 / 500)")], "min"), g="pruefung", regel="id.flaeche_raum.aus_dem_quader")
assert round(math.pi * 3 * 1000 / 500) == 19
neu(T, "sach", "verfahren_waehlen", W(
    "Du willst wissen, wie viel Erde in einen zylinderförmigen Blumenkübel passt. Der Kübel hat 40 cm Durchmesser und ist 30 cm hoch. Welcher Rechenweg ist richtig?",
    "Radius 20 cm nehmen: V = π · 20² · 30", [("V = π · 40² · 30", "den Durchmesser als Radius genommen"), ("V = 2 · π · 20 · 30", "die Formel für den Mantel statt für das Volumen"), ("V = π · 20 · 30", "den Radius nicht quadriert")],
    "Das Volumen ist Grundfläche mal Höhe. Welche Größe steckt in der Kreisfläche?",
    "r = 40 : 2 = 20 cm. G = π · 20² . V = π · 400 · 30 ≈ 37 699 cm³, also etwa 37,7 Liter.",
    lambda: abs(math.pi * 20 ** 2 * 30 - 37699) < 1 and math.pi * 40 ** 2 * 30 != math.pi * 20 ** 2 * 30 and 2 * math.pi * 20 * 30 != math.pi * 20 ** 2 * 30 and math.pi * 20 * 30 != math.pi * 20 ** 2 * 30), g="erkennen", regel="id.flaeche_raum.aus_dem_rechteck")

# ───────── verstehen ─────────
neu(T, "verstehen", "fehler_detektiv", FD(
    "Kim behauptet: Verdoppelt man bei einem Zylinder den Radius und lässt die Höhe gleich, wird das Volumen doppelt so groß.",
    [("Das Volumen ist V = π · r² · h.", True), ("Mit dem Radius 2r steht dort V = π · 2r · h = 2πrh.", gl("n*(2*a)**2*b", "2*n*a*b")), ("Also ist das neue Volumen doppelt so groß.", True)],
    "Was passiert mit r², wenn r verdoppelt wird? Probe mit r = 1 und r = 2.",
    "(2r)² = 4r². Das neue Volumen ist π · 4r² · h = 4πr²h, also 4-mal so groß. Probe: r = 1 gibt π · h, r = 2 gibt 4π · h."), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "verstehen", "bruecke", W(
    "Die Tabelle zeigt zwei gerade Kreiszylinder. Wie verhält sich das Volumen von Zylinder B zu dem von Zylinder A?",
    "3-mal so groß", [("9-mal so groß", "nur den Radius beachtet: 3² = 9"), ("gleich groß", "3 · (1 : 3) gerechnet, ohne den Radius zu quadrieren"), ("1/3 so groß", "nur die Höhe beachtet")],
    "Der Radius geht quadratisch ein, die Höhe nur einfach. Rechne beide Volumina aus oder vergleiche die Faktoren.",
    "A: π · 2² · 9 = 36π. B: π · 6² · 3 = 108π. 108π : 36π = 3. Der Radius wird 3-mal so groß (Faktor 9), die Höhe 3-mal so klein (Faktor 1/3). Zusammen 9 · 1/3 = 3.",
    lambda: F(6 ** 2 * 3, 2 ** 2 * 9) == 3,
    grafik=TAB(["", "Radius", "Höhe"], ["Zylinder A", "2 cm", "9 cm"], ["Zylinder B", "6 cm", "3 cm"])), regel="id.flaeche_raum.aus_dem_rechteck")
neu(T, "verstehen", "zwei_wege", Z(
    "Ein gerades Prisma hat die Grundfläche 20 cm² und die Höhe 6 cm. Man verändert es: Die Grundfläche wird 3-mal so groß, die Höhe halb so groß. Wie groß ist das neue Volumen? Weg A: neue Grundfläche und neue Höhe ausrechnen, dann das Volumen. Weg B: das alte Volumen mit 3 und mit 1/2 verrechnen.",
    180, "60 * 3", "20 * 6 * 3 / 2", "Beide Wege müssen dasselbe Volumen ergeben.",
    "Weg A: G = 60 cm², h = 3 cm, V = 180 cm³. Weg B: altes V = 120 cm³, 120 · 3 : 2 = 180 cm³.",
    [(360, None, "die Höhe nicht halbiert: 60 · 6", "60 * 6"), (120, None, "das alte Volumen genannt", "20 * 6"), (60, None, "nur die neue Grundfläche genommen", "20 * 3")], "cm³"), regel="id.flaeche_raum.aus_dem_rechteck")
