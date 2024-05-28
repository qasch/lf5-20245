# Aufgabe 1
# zahl = int(input("Bitte eine positive ganze Zahle eingeben: "))

# summe = 0
# for zahl in range(1, zahl + 1):
#     summe += zahl
# print(summe)


# # Aufgabe 2
# zahl = int(input("Bitte eine positive ganze Zahle eingeben: "))

# fakultaet = 1
# for zahl in range(1, zahl + 1):
#     fakultaet *= zahl
# print(fakultaet)


# # Aufgabe 3
# start = int(input("Bitte eine Zahl als Startwert eingeben: "))
# ende = int(input("Bitte eine weitere Zahl als Endwert eingeben: "))

# for i in range(start, ende + 1):
#     # ausgabe aller geraden zahlen
#     if i % 2 != 0:
#         continue
#         # inkl. start und end
#     print(i)


# for i in range(start, ende + 1):
#     print(i * 2)


# Aufgabe 4
eingabe = input("Bitte eine beliebige Zeichenkette eingeben: ")
vokale = "aeiou"
count = 0

for zeichen in eingabe:
    if zeichen in vokale:
        count += 1
print("In " + eingabe + " sind insgesamt " + str(count) + " Vokale enthalten")










