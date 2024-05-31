# Lottozahlen

## Schritt 1

# - [x] 6 Zufallszahlen generieren (zwischen 1 und 49), jede Zahl darf nur einmal vorkommen
# - [x] Zufallszahlen in einer Liste speichern
# - [ ] Benutzereingabe Tipp: 6 Zahlen zwischen 1 und 49, jede Zahl darf nur einmal vorkommen
# - [x] -> zum Testen evtl. Liste mit Zahlen erstellen (schneller fürs Testen)
# - [ ] Benutzereingaben prüfen
# - [x] Tipp in einer Liste speichern
# - [x] Listen miteinander vergleichen
# - [x] -> nacheinander alle Werte aus Tipp mit Lottozahlen vergleichen
# - [_] Ausgabe wieviel Richtige

## Schritt 2
# - [ ] Programm solange Ziehungen machen, bis ihr 6 Richtige habt
# - [ ] Anzahl der Versuche zählen

import random

# Anahl der Richtigen
correct_numbers = 0
attempts = 0

while correct_numbers < 6:
    lottozahlen = []
    correct_numbers = 0

    attempts += 1

    # lottozahlen.extend(range(1, 50))
    # print(lottozahlen)
    # lottozahlen = random.sample(lottozahlen, 6)
    # print(lottozahlen)

    while len(lottozahlen) < 6:
        num = random.randint(1, 49) 
        if num not in lottozahlen:
            lottozahlen.append(num)
    # print(lottozahlen)

    # TODO: User input bauen, fixe Liste nur zum Testen
    tipp = [3, 5, 32, 17, 9, 22]

    # Prüfe für jede Zahl in lottozahlen, ob diese in der Liste
    # tipp enthalten ist
    # falls ja, zähle die Anzahl der Richtigen um 1 hoch
    for number in lottozahlen:
        if number in tipp:
            correct_numbers += 1

print(f"Glückwunsch! Du hast {correct_numbers} Richtige: {lottozahlen} (Dein Tipp: {tipp})")
print(f"Und dafür hast du nur {attempts} Versuche gebraucht.")











 