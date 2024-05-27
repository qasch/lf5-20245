# If-Statements

## Aufgabe 1

# zahl = input("Bitte eine Zahl eingeben: ")

# if int(zahl) >= 0:
#     print("Die Zahl " + str(zahl) + " ist postiv.")
# else:
#     print("Die Zahl " + str(zahl) + " ist negativ.")

# # Alternative Lösung mit isdigit()
# if zahl.isdigit():
#     print("Die Zahl " + str(zahl) + " ist postiv.")
# else:
#     print("Die Zahl " + str(zahl) + " ist negativ.")

## Aufgabe 2

# alter = int(input("Bitte gib dein Alter ein: "))
# if alter < 18:
#     print("Du bist nicht volljährig.")
# else:
#     print("Du bist volljährig.")


# ## Aufgabe 3

# note = int(input("Bitte gib deine Note (zwischen 1 und 5) ein: "))

# if note == 1:
#     print("Sehr gut")
# elif note == 2:
#     print("Gut")
# elif note == 3:
#     print("Befriedigend")
# elif note == 4:
#     print("Ausreichend")
# elif note == 5:
#     print("Nicht ausreichend")
# else:
#     print("Ungültige Note")


## Aufgabe 4

zahl = int(input("Bitte eine Zahl eingeben: "))

if zahl == 0:
    print("Die Zahl ist 0")
elif zahl > 0:
    print("Die Zahl ist positiv")
    if zahl % 2 == 0:
        print("Die Zahl ist gerade")
    else:
        print("Die Zahl ist ungerade")
elif zahl < 0:
    print("Die Zahl ist negativ")


## Aufgabe 5

zahl1 = int(input("Bitte die erste Zahl eingeben: "))
zahl2 = int(input("Bitte die zweite Zahl eingeben: "))

if zahl1 > 0 && zahl2 > 0:
    print("Beide Zahlen sind positiv.")

if zahl1 < 0 || zahl2 < 0:
    print("Mindestens eine der beiden Zahlen ist negativ.")














