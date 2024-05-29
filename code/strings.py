# Strings in Python

my_string = "Ich bin ein String"

print(my_string)

my_second_string = " und ich noch einer"
print(my_second_string)

# Strings verbinden
big_string = my_string + my_second_string
print(big_string)

for number in range(10):
    print(number)

for character in my_string:
    print(character)

print()
print(my_string[2])


# String Konkatenation mit + Operator
zahl = 42
antwort = "auf alles"
print("Die Antwort auf alles ist " + str(zahl))

# String Ausgabe mit % 
print("Die Antwort %s ist %d" % (antwort, zahl))

# String Ausgabe mit str.format()
print("Die Antwort {} ist {} ".format(antwort, zahl))
print("Die Antwort {0} ist {1} ".format(antwort, zahl))
print("Die Antwort {antwort} ist {zahl} ".format(antwort=antwort, zahl=zahl))
print("Die Antwort {a} ist {z} ".format(a=antwort, z=zahl))

# String Ausgabe mit F-Strings
print(f"Die Antwort {antwort} ist {zahl}")

# Ausgabe des Werts einer Variable mit Bezeichner:
print("zahl=" + str(zahl))
print(f"{zahl=}")
print(f"{zahl:}")  # funktioniert nicht wie gewünscht, nur Ausgabe des Werts

# Ausgabe eines Strings mit Zeilenumbruch
# durch \n
# der Backslash \ ist ein sog. Escape Character
# dieser bezieht sich immer *nur* auf das direkt darauffolgende Zeichen
# neben dem Zeilenumbruch gibt es noch andere Steuerungszeichen, z.B.
# den Tabulatoru \t
long_string = "Das hier ist ein etwas längerer String \nmit mehr Wörtern als die anderen"
print(f"{long_string}")

# Der Baum ist "grün".
print('Der Baum ist "grün".')
print("Der Baum ist 'grün'.")
# Escapen der doppelten Anfühurungszeichen
# so wird diesem die Bedeutung als öffnendes und schliessendes Element 
# eines Strings entzogen und das Anführungszeichen wird zu einem regulären
# Satzzeichen/Character ohne besondere Bedeutung
print("Der Baum ist \"grün\".")
print("\"grün\"")

