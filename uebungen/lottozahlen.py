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

# Modul random importieren
import random

# Funktionsdeklarationen

def generate_lotto_numbers(amount):
    # lokale Variable, gibt es nur hier innerhalb der Funktion
    # ist im restlichen Code nicht bekannt
    lottozahlen = []
    while len(lottozahlen) < amount:
        num = random.randint(1, 49) 
        if num not in lottozahlen:
            lottozahlen.append(num)
    # Liste zurückgeben, so dass wir sie verwenden können
    return lottozahlen

# Prüfe für jede Zahl in lottozahlen, ob diese in der Liste
# tipp enthalten ist
# falls ja, zähle die Anzahl der Richtigen um 1 hoch
def check_tipp(lottozahlen, tipp):
    # Anahl der Richtigen
    correct_numbers = 0
    for number in lottozahlen:
        if number in tipp:
            correct_numbers += 1
    return correct_numbers

# TODO: User input bauen, fixe Liste nur zum Testen
def get_user_input():
    tipp = [3, 5, 32, 17, 9, 22]
    return tipp


# Logik

attempts = 0

found_numbers = 0
while found_numbers < 6:
    found_numbers = 0
    attempts += 1

    # lottozahlen generieren
    # gleicher Bezeichner wie oben in Funktion, aber komplett andere Variable 
    # (siehe Gültigkeitsbereich von Variablen)
    # nicht verwirren lassen! 
    lottozahlen = generate_lotto_numbers(6)

    tipp = sorted(get_user_input())

    found_numbers = check_tipp(lottozahlen, tipp)

print(f"Glückwunsch! Du hast {found_numbers} Richtige: {sorted(lottozahlen)}")
print(f"Und dafür hast du nur {attempts} Versuche gebraucht.")










 