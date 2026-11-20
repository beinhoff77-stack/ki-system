# Postfach luecken-neu (Achtzehnte Runde, Teil A: drei neue Flüge)

Neueste Meldung oben.

## 2026-11-17 14:05 – FERTIG (Abschlussbericht Teil A)

Alle drei Flüge stehen auf luecken-neu, je Thema ein Commit. Kein Merge, keine Änderung an Datenbank, App-Code oder Tests.

| Thema | thema_id | Ort (block_id) | Klasse / reihenfolge | Lernkarten | Aufgaben |
|---|---|---|---|---|---|
| messen.flaechen_vielecke – Flächen von Parallelogramm, Dreieck und Trapez | 99 | Quito (114) | gym_by 6 / 4 | 7 | 196 |
| messen.volumen – Volumen | 100 | Quito (114) | gym_by 6 / 5 | 7 | 196 |
| messen.prisma_zylinder – Prismen und Zylinder | 101 | Cusco (86) | gym_by 8 / 14 | 7 | 196 |

Je Karte: 18 Übungen (Stufe 1: 4, 2: 6, 3: 8; davon 2 nach Prüfungsvorbild, 1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung. `python3 -I tools/inhalt_pruefen.py` für alle drei Dateien OK ohne Hinweise.
Jede Aufgabe gelesen und nachgerechnet; Lösungen rechnet der Generator (Brüche exakt, π-Aufgaben mit Rundungstoleranz), der Rechenausdruck c wird beim Bauen geprüft.
Zeichnungen per Skript (`masstab` in _luecken_neu.py) auf Maßstab geprüft und im Browser mit lernBild/lernFigur angesehen.

### Lernkarten und Lehrplanbezug (LehrplanPLUS Gymnasium Bayern)
- **messen.flaechen_vielecke** (M6 2.1 Flächeninhalt): parallelogramm, dreieck, trapez, rueckwaerts (fehlende Seite/Höhe ohne Gleichung), zusammengesetzt, oberflaeche (Quader/Würfel), verstehen.
- **messen.volumen** (M6 2.2 Volumen): einheitswuerfel, quader, einheiten (mm³ bis m³), liter (l, ml), rueckwaerts (fehlende Kante, Füllhöhe), zusammengesetzt, verstehen.
- **messen.prisma_zylinder** (M8 7 Kreis und Zylinder): prisma_volumen (V = G · h für jede Grundfläche), prisma_oberflaeche (Netz, Mantel u · h), prisma_umstellen, zylinder_volumen (Grenzfall des Prismas, Hohlzylinder), zylinder_oberflaeche (Netz begründen), sach (Annahmen), verstehen (Änderung von r und h, volumengleich).
  Die Karte „zylinder“ in messen.kreisberechnung (Buenos Aires) bleibt unverändert; zylinder_volumen verweist im Einstieg darauf und vertieft. Einfache Übungen der Stufe 1 (V und O aus r, h) wiederholen bewusst die Buenos-Aires-Formeln.

### Prüfungsvorbilder (nur Typ und Niveau; eigene Zahlen und Einkleidung)
- Bayerischer Mathematik-Test 8 (ISB), Aufgaben: 2005 A/B (https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2005/bmt8_2005_aufgaben_gruppe_a.pdf), 2007 A (…/2007/bmt8_2007_aufgaben_gruppe_a.pdf), 2008 B (…/2008/bmt8_2008_aufgaben_gruppe_b.pdf), 2009 B (…/2009/bmt8-2009-aufgaben-gruppe-b.pdf), 2010 B (…/2010/bmt8-2010-aufgaben-gruppe-b.pdf), 2011 A (…/2011/bmt8_aufgabe_a.pdf), 2013 B (…/2013/bmt8_2013_aufgaben_gruppe_b.pdf), 2015 B (…/2015/bmt8_2015_aufgaben_gruppe_b.pdf), 2018 A (…/2018/bmt8_2018_aufgaben_gruppe_a.pdf), 2022 A (…/2022/bmt8_2022_aufgaben_gruppe_a.pdf), 2023 A (…/2023/BMT8_2023_Aufgaben_Gruppe_A.pdf), 2025 A (…/2025/BMT8_2025_Aufgaben_Gruppe_A.pdf); Pfad jeweils https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/
- Bayerischer Mathematik-Test 10 (ISB): 2024 Gruppe B Aufg. 6 (https://isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2024/BMT10_2024_Aufgaben_Gruppe_B.pdf), 2021 A (…/2021/bmt10_2021_aufgaben_gruppe_a.pdf)
- Jahrgangsstufentest Realschule Bayern 6, 2010 (https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2010/end_6test2010_ohne-foto.pdf)
- Abschlussprüfung Realschule Bayern 2020, Mathematik I, B1 (https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2020/2020_mi_ht.pdf)
- VERA-8 2012, Modul C (Würfelkörper), über NiBiS
- Niveaubestimmende Aufgabe Sachsen-Anhalt „Prisma“ (https://www.bildung-lsa.de/pool/RRL_Lehrplaene/niveaubestimmende_Aufgaben_Gym/Mathematik/Aufgabe_Prisma_10.pdf) – dort für einen höheren Schuljahrgang; hier nur der Aufgabentyp „volumengleicher Quader“ übernommen.
- IQB-Lernaufgabe „Hamsterhaltung“ (https://www.iqb.hu-berlin.de/media/exercise_files/Lernaufgaben_Mathematik_Sek_I/Hamsterhaltung_Aufgabe.pdf)
- Lehrplan: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik und …/gymnasium/8/mathematik

### Offene Punkte / Unsicherheiten
- Belegt: Die Prüfungsquellen für Klasse 8 zu **Oberflächen** von Prismen sind dünn (BMT8/BMT10 fragen vor allem Volumen); die Oberflächen-Vorbilder stammen aus der Realschul-Abschlussprüfung und VERA-8.
- Kinder können in der App nicht zeichnen oder messen; Aufgaben zum Zeichnen von Netzen/Schrägbildern sind deshalb als Auswahl- oder Rechenaufgaben gebaut.
- Klasse 6: keine Gleichungen mit x; Rückwärtsaufgaben über Umkehraufgaben. Klasse 8: kein Pythagoras; schräge Kanten und Diagonalen sind immer angegeben.
- Klasse-6-reihenfolge: flaechen_vielecke (4) und volumen (5) eingeschoben, die folgenden Klasse-6-Themen rücken um 2 nach hinten. Bitte prüfen, ob das zur gewünschten Reiseroute passt.
- Zylinder werden in Aufgaben nur als Netz gezeichnet; liegende Schrägbilder kurzer Zylinder waren mit den heutigen Zeichenmitteln (keine halb verdeckten Kreise) nicht sauber lesbar und wurden weggelassen.
- Zeichentechnik: freie Beschriftungen über Hilfspunkte mit Strecke der Länge 0 (gestrichelt, also unsichtbar); Höhen an Prismen als Maßlinie links neben der Grundfläche. Nutzt nur, was lernFigur heute kann.

## 2026-11-17 14:00 – STATUS
messen.prisma_zylinder (thema_id 101, Cusco, Klasse 8) fertig: 7 Lernkarten (prisma_volumen, prisma_oberflaeche, prisma_umstellen, zylinder_volumen, zylinder_oberflaeche, sach, verstehen), 196 Aufgaben
(je Karte 18 Übungen 4/6/8 mit 2 Prüfungsvorbildern und 1 Knobelaufgabe, 1 Test, 3 Korrektur, 6 Sicherung). inhalt_pruefen OK ohne Hinweise; alle Aufgaben gelesen und nachgerechnet.
Verweis auf die Karte „zylinder“ in messen.kreisberechnung (Buenos Aires), dort nichts verschoben. Eintrag in themenliste.json: Klasse 8, reihenfolge 14 (nach messen.koerper_darstellung).

## 2026-11-17 13:41 – STATUS
messen.volumen (thema_id 100, Quito, Klasse 6) fertig: 7 Lernkarten (einheitswuerfel, quader, einheiten, liter, rueckwaerts, zusammengesetzt, verstehen), 196 Aufgaben
(je Karte 18 Übungen 4/6/8 mit 2 Prüfungsvorbildern und 1 Knobelaufgabe, 1 Test, 3 Korrektur, 6 Sicherung). inhalt_pruefen OK ohne Hinweise; alle Aufgaben gelesen und nachgerechnet.
Schrägbilder (Quader, Stufen, Aquarium mit Wasserstand) maßstäblich, im Browser geprüft. Eintrag in themenliste.json: Klasse 6, reihenfolge 5 (nach messen.flaechen_vielecke).

## 2026-11-17 13:34 – STATUS
messen.flaechen_vielecke (thema_id 99, Quito, Klasse 6) fertig: 7 Lernkarten (parallelogramm, dreieck, trapez, rueckwaerts, zusammengesetzt, oberflaeche, verstehen), 196 Aufgaben
(je Karte 18 Übungen 4/6/8 mit 2 Prüfungsvorbildern und 1 Knobelaufgabe, 1 Test, 3 Korrektur, 6 Sicherung). inhalt_pruefen OK ohne Hinweise; alle Aufgaben gelesen und nachgerechnet.
Zeichnungen per Skript auf Maßstab geprüft (angeschriebene = gezeichnete Längen, Tiefenkanten im Schrägbild halb so lang unter 45°, rechte Winkel echt) und im Browser mit lernen.js angesehen.
Neu in inhalte/themenliste.json (Klasse 6, reihenfolge 4 nach bruch.rechnen; die folgenden Klasse-6-Themen rücken um 1 nach hinten).
Gemeinsame Hilfsdatei: inhalte/generatoren/_luecken_neu.py.
Hinweis: Höhen-Beschriftungen stehen frei neben der Höhe (Hilfspunkt mit Strecke der Länge 0 und Text), damit sie keine Seite überdecken – das nutzt nur, was lernFigur heute schon zeichnet.
