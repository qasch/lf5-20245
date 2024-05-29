# Lists in Python

# Eine list in Python ist so etwas wie ein Array in anderen Programmiersprachen

# Variable, kann einen einzigen Wert speichern
zahl = 4
print("zahl: " + str(zahl))
 
# List, kann beliebig viele Werte speichern
# Element 1  2  3   4
# Index:  0  1  2   3
zahlen = [1, 3, 7, 14]

print("zahlen: " + str(zahlen))

print()
print("List aus Integern: ")
print()
print("Ausgabe 1. Element am Index 0: " + str(zahlen[0]))
print("Ausgabe 2. Element am Index 1: " + str(zahlen[1]))
print("Ausgabe 3. Element am Index 2: " + str(zahlen[2]))

# print("Versuch: Ausgabe 4. Element am Index 4: " + str(zahlen[4]))


strings = ["Hund", "Katze", "Maus"]
print()
print("List aus Strings: ")
print()
print("Ausgabe 1. Element am Index 0: " + str(strings[0]))
print("Ausgabe 2. Element am Index 1: " + str(strings[1]))
print("Ausgabe 3. Element am Index 2: " + str(strings[2]))

# In Python können wir auch verschiedene Datentypen in der gleichen List speichern
my_list = [42, True, "Ich bin ein String", 3.14, False, 12, 23, "Blablabla"]
print()
print("List aus verschiedenen Datentypen: ")
print()
print("Ausgabe 1. Element am Index 0: " + str(my_list[0]))
print("Ausgabe 2. Element am Index 1: " + str(my_list[1]))
print("Ausgabe 3. Element am Index 2: " + str(my_list[2]))
print("Ausgabe 4. Element am Index 3: " + str(my_list[3]))


print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

print()
print()
print()
print("Ausgabe aller Elemente der list my_list mit for-Schleife")

# For Schleife zur Ausgabe aller Elemente in my_list
for element in my_list:
    print(element)

print()
print()
print()
print("Ausgabe aller Elemente der list my_list mit while-Schleife")
# While Schleife zur Ausgabe aller Elemente in my_list
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

print("Anzahl der Elemente in my_list " + str(len(my_list)))

print("\n--------------------\n")

print("Leere Liste erzeugen:")
tiere = []

print("Anzahl der Elemente der List tiere:")
print(len(tiere))

print("Hinzufügen von Elementen zur List tiere mit append()")
# tiere[0] = "Hund"
tiere.append("Hund")
print("Anzahl der Elemente der List tiere:")
print(len(tiere))
print(tiere[0])

tiere.append("Katze")
print("Anzahl der Elemente der List tiere:")
print(len(tiere))
print(tiere[1])

tiere.append("Maus")
tiere.append("Elefant")
tiere.append("Schildkröte")
tiere.append("Biber")
tiere.append("Eichhörnchen")
print(len(tiere))


# Entfernen eines konkreten, vorhandenen Elements aus der Liste
# Element/Wert muss vorhanden sein, sonst kommt es zu einer Exception
tiere.remove("Maus")
print(len(tiere))

print(tiere.pop(2))
print(len(tiere))

print(tiere.pop())
print(len(tiere))