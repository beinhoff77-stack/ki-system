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
