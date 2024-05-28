# Loops in Python

# Zählvariable
# Bedingung muss irgendwann *nicht* mehr erfüllt sein,
# damit wir keine Endlosschleife produzieren.
# Daher muss die Zählvariable verändert werden.
zahl = 7
while zahl < 10:
    print(str(zahl) + " ist kleiner als 10.")
    # Zählvariable erhöhen/inkrementieren
    # zahl = zahl + 1
    zahl += 1     # Kurzschreibweise für obigen Ausdruck
    # zahl++        # Inkrement in anderen C-Sprachen 

# Abbruch Endlosschleife mit STRG+C


# Alle Zahlen von 20 bis 10 in absteigender Reihenfolge ausgeben
# number = 20
# while number >= 10:
#     print(number)
#     number -= 1

# Schleife mit else (wird ausgeführt wenn Bedingung nicht [mehr] wahr ist.)
number = 19 
while number >= 10:
    print(number)
    number -= 1
else:
    print("Es wurden insgesamt " + str(number + 1) + " Elemente ausgegeben.")


# Schleife mit break
# wird das Schlüsselwort break in einer Schleife erreicht, wird die Schleife unabhängig
# von der Bedingugn abgebrochen.
number = 1
while number <= 100:
    print(number)
    number += 1
    if number == 20:
        break      # Schleife beenden

print
print("---------------------")
print

# Schleife mit continue
number = 15
while number <= 25:
    number += 1
    if number == 20:
        # mit continue springen wir wieder an den Anfang der Schleife,
        # der Rest der Schleife wird in diesem Durchgang nicht mehr ausgeführt
        continue   
    print(number)


# For loop: Ausgabe der Zahlen von 0 bis 9
print()
print("for loop mit range")
print()
for count in range(10):
    print(count)

# gleiche Ausgabe wie oben als while Schleife
count = 0
while count < 10:
    print(count)
    count += 1

print()
print("for loop mit range und start und stop Argument")
print()
for count in range(10, 20):
    print(count)

print()
print("for loop mit range und start und stop Argument und step")
print()
for count in range(10, 100, 5):
    print(count)

print()
print("for loop mit range und start und stop Argument und negativem step")
print("sorgt dafür, dass geprüft wird, ob start *kleiner* ist als stop")
print()
for count in range(100, 10, -5):
    print(count)
