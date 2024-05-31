# Lottozahlen

## Schritt 1

# - [x] 6 Zufallszahlen generieren (zwischen 1 und 49), jede Zahl darf nur einmal vorkommen
# - [x] Zufallszahlen in einer Liste speichern
# - [ ] Benutzereingabe Tipp: 6 Zahlen zwischen 1 und 49, jede Zahl darf nur einmal vorkommen
# - [x] -> zum Testen evtl. Liste mit Zahlen erstellen (schneller fürs Testen)
# - [ ] Benutzereingaben prüfen
# - [x] Tipp in einer Liste speichern
# - [ ] Listen miteinander vergleichen
# - [ ] -> nacheinander alle Werte aus Tipp mit Lottozahlen vergleichen
# - [ ] Ausgabe wieviel Richtige

## Schritt 2
# - [ ] Programm solange Ziehungen machen, bis ihr 6 Richtige habt
# - [ ] Anzahl der Versuche zählen

import random

# num = random.randint(1, 49)    # 1 und 49 sind inklusive

lottozahlen = []

# lottozahlen.extend(range(1, 50))
# print(lottozahlen)
# lottozahlen = random.sample(lottozahlen, 6)
# print(lottozahlen)

while len(lottozahlen) < 6:
    num = random.randint(1, 49) 
    if num not in lottozahlen:
        lottozahlen.append(num)
print(lottozahlen)

# TODO: User input bauen, fixe Liste nur zum Testen
tipp = [3, 5, 32, 17, 9, 22]

# Anahl der Richtigen
correct = 0
# Prüfe für jede Zahl in lottozahlen, ob diese in der Liste
# tipp enthalten ist
# falls ja, zähle die Anzahl der Richtigen um 1 hoch
for number in lottozahlen:
    if number in tipp:
        correct += 1

print(f"Du hast {correct}: {lottozahlen} (richtige {tipp})")











# counter = 0
# print(num)

# nums = []

# while True:
#     # user_guess = int(input("Bitte eine Zahl zwischen 1 und 10 eingeben: "))

#     counter += 1

#     if user_guess > num:
#         print("zu gross, nochmal versuchen")
#     elif user_guess < num:
#         print("zu klein, nochmal versuchen")
#     else:
#         print("Gewonnen")
#         break

# print(f"Ende, du hast {counter} Versuche gebraucht.")











 