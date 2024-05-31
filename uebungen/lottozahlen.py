# Lottozahlen

## Schritt 1

# 6 Zufallszahlen generieren (zwischen 1 und 49), jede Zahl darf nur einmal vorkommen
# Zufallszahlen in einer Liste speichern
# Benutzereingabe Tipp: 6 Zahlen zwischen 1 und 49, jede Zahl darf nur einmal vorkommen
# -> zum Testen evtl. Liste mit Zahlen erstellen (schneller fürs Testen)
# Benutzereingaben prüfen
# Tipp in einer Liste speichern
# Listen miteinander vergleichen
# -> nacheinander alle Werte aus Tipp mit Lottozahlen vergleichen
# Ausgabe wieviel Richtige

## Schritt 2
# Programm solange Ziehungen machen, bis ihr 6 Richtige habt
# Anzahl der Versuche zählen

import random

zufallszahl = random.randint(10, 20)
print(zufallszahl)