"""Denkfigur je Aufgabe (Feld „idee“): je Lernziel mindestens 5 verschiedene, höchstens 2 gleiche."""
IDEEN = {
 # finanzen.zinsen
 1: 'Sparen und Kredit auseinanderhalten', 2: 'Kreditzinsen und Guthabenzinsen gegeneinander aufrechnen', 3: 'Vorzeichen: gezahlt oder erhalten',
 4: 'Fehlersuche in der Saldo-Rechnung', 5: 'Zinsen aus Rückzahlung ablesen', 6: 'Rückwärts: Zinssatz aus Differenz', 7: 'Gewinn nur bei Zinsunterschied',
 8: 'Fehlersuche beim Prozentkomma', 9: 'Ergebnis einer Rechnung prüfen', 10: 'Zinssatz als Faktor schreiben', 11: 'Mehrere Ergebnisse auf einen Fehler zurückführen',
 12: 'Zinssatz ändern, Zinsen verfolgen', 13: 'Fehlersuche bei Dezimalstellen', 14: 'Zwei Rechenwege vergleichen',
 15: 'Zinssatz sinkt, Kapital muss steigen', 16: 'Verhältnisse: gleiche Zinsen, anderes Kapital', 17: 'Gleichung zum Kapital aufstellen', 18: 'Fehlersuche beim Umstellen',
 19: 'Gleiche Zinsen, Zinssätze vergleichen', 20: 'Teilanlage und Rückschluss auf das Ganze', 21: 'Ungleichung aus zwei Anlagen',
 22: 'Brücke Monate und Jahr', 23: 'Zinsmonate ablesen und prüfen', 24: 'Verschiedene Angebote vergleichen', 25: 'Zeitanteil als Bruch eintragen',
 26: 'Passende Rechenvorschrift wählen', 27: 'Rückwärts vom Teiljahr zum Jahr', 28: 'Proportionalität der Zeit',
 # terme.umformen
 29: 'Fehlersuche beim Zusammenfassen', 30: 'Parameter so wählen, dass ein Glied entfällt', 31: 'Umfang als Term', 32: 'Fehlersuche bei zwei Variablen', 33: 'Rückwärts: Term zum Ergebnis finden', 34: 'Umkehroperation: Differenz zum Term', 35: 'Sachsituation in Terme übersetzen',
 36: 'Fehlersuche bei Minusklammern', 37: 'Probe durch Einsetzen', 38: 'Parameter durch Koeffizientenvergleich', 39: 'Begründen mit Gegenbeispiel', 40: 'Zwei Wege: Umformen oder Einsetzen', 41: 'Fehlersuche bei Plus- und Minusklammer', 42: 'Länge als Term',
 43: 'Einsetzen widerlegt keine Gleichwertigkeit', 44: 'Gleicher Wert nur an einer Stelle', 45: 'Parameter durch Ausmultiplizieren', 46: 'Zwei Wege: Umformen oder Einsetzen', 47: 'Wie viele Einsetzungen beweisen?', 48: 'Gleichwertigen Term unter vier finden', 49: 'Parameter durch Koeffizientenvergleich',
 # terme.umformen_teil2
 50: 'Ausklammern durch Ausmultiplizieren prüfen', 51: 'Umkehren: Faktor aus Fläche', 52: 'Fehlersuche beim größten gemeinsamen Faktor', 53: 'Geschickt rechnen', 54: 'Grenzen des Ausklammerns', 55: 'Gemeinsamen Faktor festlegen', 56: 'Fläche als Produkt',
 57: 'Fehlersuche beim Quadrieren', 58: 'Ergänzen zur binomischen Formel', 59: 'Warum fehlt das gemischte Glied?', 60: 'Flächenzuwachs am Quadrat', 61: 'Kopfrechnen mit binomischer Formel', 62: 'Fehlersuche beim gemischten Glied', 63: 'Aus der Fläche auf die Seite schließen',
 # geometrie.kreis
 64: 'Rechter Winkel legt C auf den Kreis', 65: 'Koordinate aus rechtem Winkel', 66: 'Ortslinie: alle Punkte gleich weit von M', 67: 'Fehlersuche Radius und Durchmesser', 68: 'Lage zum Kreis an Koordinaten prüfen', 69: 'Hypotenuse als Durchmesser des Umkreises', 70: 'Gleichschenklige Teildreiecke und Winkel',
 71: 'Abstand variieren, Schnittpunkte zählen', 72: 'Rückwärts: Abstand aus Schnittpunkten', 73: 'Radius so wählen, dass nichts schneidet', 74: 'Passante, Tangente oder Sekante bestimmen', 75: 'Tangentenabstand aus dem Durchmesser', 76: 'Zwei Kreise mit gleichem Mittelpunkt', 77: 'Radius vergrößern, Lage ändert sich',
 78: 'Umkreismittelpunkt außerhalb', 79: 'Lage des Umkreismittelpunkts', 80: 'Lage nach Dreiecksart zuordnen', 81: 'Fehlersuche beim Inkreis', 82: 'Gegenbeispiel zu einer Immer-Aussage', 83: 'Winkelbedingung für die Lage', 84: 'Umkreis und Inkreis im gleichseitigen Dreieck',
 # zahlen.natuerlich
 85: 'Ziffern vertauschen, Wert vergleichen', 86: 'Gleiche Ziffer, verschiedener Wert', 87: 'Volle Hunderter und Zehner zählen', 88: 'Fehlersuche beim Stellenwert', 89: 'Null als Platzhalter', 90: 'Zahlen aus Ziffern bilden und vergleichen', 91: 'Rückwärts: Zahl nach Anhängen einer Null',
 92: 'Zahl mit Nullen lesen', 93: 'Zahlwort verändern', 94: 'Fehlersuche bei Klassen', 95: 'Warum Klassen gelesen werden', 96: 'Zahlwörter der Größe nach vergleichen', 97: 'Fehlersuche beim Lesen', 98: 'Zahlwort nach Malnehmen',
 99: 'Teilstriche und Skalenwert', 100: 'Zahl an Teilstrichen ablesen', 101: 'Rückwärts: Schrittweite aus Marken', 102: 'Fehlersuche beim Maßstab', 103: 'Zahl zwischen zwei Teilstrichen', 104: 'Rückwärts: Zahl am dritten Teilstrich', 105: 'Gleichmäßige Skala begründen',
 106: 'Umkehren: Zahlen mit gleichem Rundungsergebnis zählen', 107: 'Umkehren: Grenzen des Rundungsbereichs', 108: 'Welche Zahl rundet auf den Wert?', 109: 'Fehlersuche bei der Rundungsstelle', 110: 'Rundung vergrößert oder verkleinert', 111: 'Zweimal runden gegen einmal runden', 112: 'Abstand zweier Zahlen mit gleichem Rundungsergebnis',
 113: 'Wann Runden unsinnig ist', 114: 'Aufrunden aus Sachgründen', 115: 'Verschieden genau runden', 116: 'Überschlag mit Rundung vor dem Rechnen', 117: 'Zu grobes Runden verfälscht', 118: 'Überschlag der Summe', 119: 'Rundungsfehler summiert sich',
 120: 'Fehlersuche bei Subtraktionsregel', 121: 'Regeln der römischen Zahlen anwenden', 122: 'Zeichen zählen', 123: 'Bausteine bewerten', 124: 'Rückwärts: Zahl zur römischen Schreibweise', 125: 'Zwei Schreibweisen vergleichen', 126: 'Muster in einer Zahlenfolge',
 127: 'Anhängen einer Null im Zweiersystem', 128: 'Zerlegen in Zweierpotenzen', 129: 'Zweierzahlen vergleichen', 130: 'Fehlersuche beim Umwandeln', 131: 'Eins und Nullen: Zweierpotenz', 132: 'Anzahl darstellbarer Zahlen', 133: 'Rückwärts: Länge aus dem Wert',
}

IDEEN.update({
 1: 'Nettosatz: nur der Zinsunterschied zählt', 2: 'Nettobilanz gegen das Bauchgefühl', 5: 'Rückzahlung enthält Kredit und Zinsen', 7: 'Rollen aus Sicht der Bank',
 9: 'Zinssatz zehnmal kleiner, Zinsen zehnmal kleiner', 10: 'Zinssatz als Rechenfaktor schreiben', 11: 'Ergebnis mit Begründung prüfen', 12: 'Zinssatz aus dem Zinsbetrag zurückschließen',
 13: 'Kapital und Zinssatz gegeneinander verrechnen', 14: 'Zinssatz zerlegen',
 15: 'Altes und neues Kapital vergleichen', 22: 'Laufzeit aus den Zinsen rückwärts', 23: 'Zinssatz und Zeit gleichen sich aus', 24: 'Zeitanteil als Prozent des Kapitals',
 25: 'Zeitanteile als Bruch des Jahres', 27: 'Proportionalität der Zeit ohne Kapital', 28: 'Zinsen wachsen mit der Zeit',
 31: 'Gegenbeispiel zum Zusammenfassen', 33: 'Fehlende Zahlen rückwärts ergänzen', 37: 'Variable fällt beim Auflösen weg', 40: 'Einsetzprobe als Kontrolle', 42: 'Geschickt rechnen mit Minusklammer',
 44: 'Konstanter Unterschied: nie gleich', 45: 'Zwei Übereinstimmungen beweisen nichts', 47: 'Term aus Wertetabelle erschließen',
 50: 'Falsche Umformung durch Probe finden', 51: 'Parameter aus der Faktorzerlegung', 53: 'Größtmöglichen Faktor wählen', 56: 'Breite aus Fläche und Länge',
 58: 'Parameter für ein Quadrat', 61: 'Abstand benachbarter Quadrate', 63: 'Aus der Fläche auf die Seite schließen',
 64: 'Rechter Winkel legt C auf den Kreis', 65: 'Koordinate aus rechtem Winkel', 66: 'Umkreisradius und Hypotenuse', 67: 'Fehlersuche Radius und Durchmesser',
 68: 'Ortslinie aller Punkte mit rechtem Winkel', 69: 'Hypotenuse als Durchmesser des Umkreises', 70: 'Gleichschenklige Teildreiecke und Winkel',
 71: 'Radius aus der Zahl der Passanten', 73: 'Gerade fest, Radius ändert sich', 74: 'Tangente steht senkrecht auf dem Berührradius', 75: 'Abstand einer Geraden zum Kreis', 77: 'Höchstens zwei Schnittpunkte',
 78: 'Lage außen über beide stumpfen Fälle zählen', 81: 'Fehlersuche bei der Umkreiskonstruktion', 82: 'Inkreismittelpunkt liegt immer innen', 83: 'Winkelhalbierende halbiert den Winkel',
 85: 'Tausch benachbarter Stellen rückwärts', 92: 'Nullen bei Zahlwörtern', 100: 'Falsch beschriftete Skala erkennen', 101: 'Näher an welcher Marke', 104: 'Striche und Abschnitte',
 108: 'Größter Rundungsfehler', 112: 'Zwei Rundungen gleichzeitig', 113: 'Rundungsfehler wird vervielfacht', 120: 'Fehlersuche ohne genannte Regel', 122: 'Längste römische Schreibweise',
 127: 'Ziffer anhängen: doppelt plus Ziffer', 128: 'Zahlen mit genau einer Eins',
})

IDEEN[124] = 'Subtraktionspaare zählen'

# zweite Vorprüfung: umgebaute oder ersetzte Aufgaben
IDEEN.update({
 9: 'Von 1 % aus auf andere Zinssätze schließen', 13: 'Zwei Sparbücher getrennt berechnen und vergleichen', 22: 'Laufzeit bei zwei Anlagen angleichen',
 29: 'Zwei Umfänge für jedes x gleichsetzen', 38: 'Parameter durch Einsetzen', 43: 'Eine Übereinstimmung beweist nichts',
 45: 'Umformungskette auf Gleichwertigkeit prüfen', 81: 'Inkreisgedanke in der Umkreiskonstruktion', 83: 'Winkel am Inkreismittelpunkt rückwärts',
 92: 'Stellenzahl und Stelle aus dem Zahlwort', 99: 'Skala ohne Nullpunkt: Maßstab aus zwei Marken', 106: 'Höchstabstand zweier Rundungsbereiche',
 107: 'Randfälle an der Rundungsgrenze', 112: 'Kleiner Unterschied, großer Sprung beim Runden', 114: 'Gleiche Rechnung, andere Rundungsrichtung',
 120: 'Regel anwenden und Längen vergleichen', 127: 'Länge im Zweiersystem als Wertebereich', 129: 'Führende Null ändert den Wert nicht',
})

IDEEN.update({
 53: 'Mehrere gleichwertige Produktformen prüfen', 58: 'Parameter für das Quadrat einer Differenz', 106: 'Zehner- und Hunderterrundung über einen Zahlenbereich vergleichen',
 111: 'Reihenfolge bleibt beim Runden erhalten',
})

IDEEN.update({
 15: 'Zinsunterschied zweier Zinssätze auf das Kapital zurückführen', 30: 'Glieder zählen und Vorzeichen des x²-Gliedes',
 34: 'Gegenläufige x-Glieder heben sich auf', 43: 'Sechs Terme in gleichwertige Gruppen sortieren',
 64: 'Der Abstand zum Mittelpunkt bleibt bei allen rechtwinkligen Dreiecken gleich', 83: 'Aus zwei Teilwinkeln am Inkreismittelpunkt alle Winkel',
 103: 'Zwei Teilungen desselben Zahlenstrahls', 113: 'Fehler beim Aufrunden zweier Faktoren', 122: 'Warum die Subtraktionsregel Zeichen spart',
 126: 'Kleinste Zahl mit sechs Zeichen', 128: 'Zweierpotenzen erkennen', 131: 'Wert der vordersten Zweierstelle über einen Unterschied',
})

IDEEN.update({
 1: 'Nettozinsen rückwärts auf den Kredit', 5: 'Zinssatz von der Sparer- auf die Kreditnehmerrolle übertragen',
 8: 'Zinsen doppelt gezählt (Fehler mitten in der Rechnung)', 15: 'Mehr Zinssatz heißt weniger Kapital, aber nicht im gleichen Maß',
 18: 'Prozentzahl statt Faktor in der Gleichung', 25: 'Zinssatzwechsel im Lauf des Jahres',
 42: 'Minus wirkt auf jedes Glied einer langen Klammer', 44: 'Zwei Zählweisen eines Streichholzmusters',
 46: 'Zahlenrätsel mit einem Term erklären', 48: 'Übereinstimmung an zwei Stellen ist kein Beweis',
 51: 'Vorzeichen des ausgeklammerten Faktors', 52: 'Nicht der größte gemeinsame Faktor (Fehler in Zeile 1)',
 55: 'Faktor muss genau 6x und nicht größer sein', 79: 'Dreiecke nach Lage des Umkreismittelpunkts zählen',
 80: 'Dritter Winkel entscheidet die Lage', 81: 'Bedingung für den Umkreis schon in Zeile 1 falsch',
 116: 'Rundungsbereich in eine Preisrechnung übernehmen', 118: 'Rundungsbereich durch eine Zahl geteilt',
})

IDEEN.update({6: 'Guthaben, bei dem sich die Rollen ausgleichen'})

# Urteil 1222: neue Kerne
IDEEN.update({
 4: 'Bekommen und Zahlen gleichen sich aus', 12: 'Komma um eine Stelle verschiebt Zinssatz', 13: 'Halbes Kapital braucht doppelten Zinssatz',
 23: 'Doppelte Zeit und halber Zinssatz heben sich auf', 26: 'Kapital mal Monate als gemeinsames Maß',
 30: 'Gleichartige Paare zählen', 35: 'Wertänderung eines Terms bei x + 1', 36: 'Zwei Parameter durch Koeffizientenvergleich',
 39: 'Urteil über eine Klammerumformung mit Gegenprobe', 40: 'Gleichwertige Terme zu einer Minusklammer zählen',
 42: 'Gleichung mit Minusklammer rückwärts lösen', 53: 'Vollständig und unvollständig ausgeklammert unterscheiden',
 61: 'Quadrat ist nie negativ, aber kann null sein', 62: 'Unterschied zweier Terme als Term mit x',
 67: 'Rechter Winkel gibt Mittelpunkt der Hypotenuse', 69: 'Thales-Umkehrung als Durchmesser', 79: 'Grenzwinkel für außen liegenden Mittelpunkt',
 80: 'Winkelverhältnis bestimmt die Lage des Mittelpunkts', 82: 'Inkreismittelpunkt liegt immer innen',
 87: 'Stellenwerte beim Ersetzen von Ziffern', 90: 'Führende Null ausschließen beim Zählen', 93: 'Nullen in einer Zahl aus Klassen erschließen',
 98: 'Leere Klasse mit Nullen füllen', 101: 'Striche und Abstände unterscheiden', 104: 'Maßstab in Zahlenbereich übersetzen',
 107: 'Breite des Rundungsbereichs bestimmen', 112: 'Randzahlen eines Rundungsbereichs',
})

# Welle 1, Runde 2 (Vorprüfung W1): terme.umformen und zahlen.natuerlich neu nummeriert (5 je Lernziel).
# VT2-044 … 049 und VT2-120 … 133 sind nicht mehr vergeben; ihre Einträge oben werden nicht mehr benutzt.
IDEEN.update({
 # terme.umformen / zusammenfassen
 29: 'Zwei Umfänge für jedes positive x gleichsetzen', 30: 'Fehlersuche bei zwei Variablen',
 31: 'Falsche Zusammenfassung stimmt nur an einer Stelle', 32: 'Gegenläufige x-Glieder heben sich auf',
 33: 'Zahl vor der Variablen als Änderung je Schritt',
 # minusklammer
 34: 'Folge einer falschen Klammerregel rückwärts', 35: 'Fehlersuche bei Plus- und Minusklammer',
 36: 'Minusklammer im Sachzusammenhang deuten', 37: 'Muster wiederholter Minusklammern',
 38: 'Minusklammer dreht eine Differenz um',
 # aequivalenz
 39: 'Zwei Stellen legen einen Term a · x + b fest', 40: 'Zwei Zählweisen eines Streichholzmusters',
 41: 'Zahlenrätsel rückwärts: Ergebnis hängt nicht von der Zahl ab', 42: 'Gleicher x-Teil, andere Zahl: nie gleich',
 43: 'Sechs Terme in gleichwertige Gruppen sortieren',
 # zahlen.natuerlich / stellenwert
 85: 'Wertverhältnis gleicher Ziffern gibt den Stellenabstand', 86: 'Zuwachs beim Ziffertausch hängt nur vom Unterschied ab',
 87: 'Fehlersuche beim Stellenwert', 88: 'Null als Platzhalter, auch die nicht gesprochene', 89: 'Kleinste und größte Zahl aus festen Plättchen',
 # ziffern_zu_zahlwort
 90: 'Leere Klasse: Klassenwort fällt weg', 91: 'Nicht gesprochene Klassen behalten ihre Stellen',
 92: 'Fehlersuche bei Klassen', 93: 'Warum von rechts in Dreiergruppen geteilt wird', 94: 'Höchstens ein „hundert“ je Klasse',
 # strahl_eintragen
 95: 'Skala ohne Nullpunkt: Maßstab aus zwei Marken', 96: 'Strichzahlen bei verschobenem Anfang',
 97: 'Zwei Maßstäbe vergleichen ohne Lage der Zahlen', 98: 'Zwei Teilungen desselben Zahlenstrahls',
 99: 'Gleiche Strecke heißt gleicher Unterschied',
 # runden_regel
 100: 'Zehner- und Hunderterrundung über einen Zahlenbereich vergleichen', 101: 'Größter Rundungsfehler',
 102: 'Fehlersuche bei der Rundungsstelle', 103: 'Rundung vergrößert, verkleinert oder lässt gleich',
 104: 'Reihenfolge bleibt beim Runden erhalten',
 # runden_sinnvoll
 105: 'Rundungsbereich durch eine Zahl geteilt', 106: 'Gleiche Rechnung, andere Rundungsrichtung',
 107: 'Verschieden genau runden', 108: 'Fehler beim Aufrunden zweier Faktoren', 109: 'Gleichgerichtete Rundungsfehler addieren sich',
 # roemisch_schreiben
 110: 'Wo die Subtraktionsregel am meisten spart', 111: 'Regeln der römischen Zahlen anwenden',
 112: 'Mehr Zeichen heißt nicht größer', 113: 'Größte schreibbare Zahl', 114: 'Kleinste Zahl mit sechs Zeichen',
 # dualsystem
 115: 'Falsche Leserichtung: nur Spiegelzahlen bleiben richtig', 116: 'Führende Null ändert den Wert nicht',
 117: 'Tausch zweier Stellen: Änderung unabhängig vom Rest', 118: 'Endziffern im Zweiersystem und Teilbarkeit durch 4',
 119: 'Stellenzahl im Zweier- und im Zehnersystem',
})

# Welle 1, Runde 2, nach der zweiten Vorprüfung (vorpruefung-w1-2.md): ersetzte oder umgebaute Aufgaben
IDEEN.update({
 31: 'Was ein einziges gleichartiges Glied am Ergebnis ändern kann', 38: 'Wert einer Minusklammer hängt nur vom Unterschied ab',
 40: 'Aus dem Aufbau eines Terms die Zählweise erschließen', 42: 'Keine, eine oder jede Übereinstimmung nach den Zahlen unterscheiden',
 95: 'Gleicher Unterschied auf zwei Strahlen: Maßstab umgekehrt', 97: 'Striche statt Abstände gezählt: Fehler immer ein Abschnitt',
 98: 'Zwei Teilungen: gemeinsame Striche in festem Abstand', 108: 'Richtung des Schätzfehlers beim Produkt',
 110: 'Rückwärts aus der Ersparnis der Subtraktionsregel', 112: 'Plus 1 kann die Schreibweise verkürzen',
 113: 'Größte schreibbare Zahl aus den Regeln', 115: 'Zahl und Gegenzahl ergeben zusammen 11111',
 117: 'Zahl der Einsen sagt nichts über die Größe', 118: 'Jede Stelle wird von genau der Hälfte der Zahlen gebraucht',
})
