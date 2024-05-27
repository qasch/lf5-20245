# Aufgabe 1

x = 10
y = 5
summe = x + y
print(summe)
# print(x + y)   # auch möglich, aber in der Aufgabe anders angegeben


print()
print("---------------------------------------")
print()

# Aufgabe 2

# Hinweis: andere Variablen Namen als in der Aufgabenstellung
text = "Hallo Welt!"
kommazahl = 3.14
wahrheitswert = True  

print("text:", type(text))
print("kommazahl:", type(kommazahl))
print("wahrheitswert:", type(wahrheitswert))
# Ausgabe in einer Zeile
# type kann nur ein einzelnes zu prüfendes Objekt übergeben werden,
# daher muss hier dreimal type() genutzt werden
print(type(text), type(kommazahl), type(wahrheitswert))


print()
print("---------------------------------------")
print()

# Aufgabe 3

name = "Shahin"
age = 35
satz = "Mein Name ist", name, "und ich bin", age, "Jahre alt."
print(satz)
print("Mein Name ist", name, "und ich bin", age, "Jahre alt.")


print()
print("---------------------------------------")
print()

# Aufgabe 4

# Lösung mit Hilfsvariablen
x = 10
y = 20
print("x:", x, "y:", y)
x1 = x
y1 = y
x = y1
y = x1
print("x:", x, "y:", y)


# kürzere Alternative in Python:
x = 10
y = 20
print("x:", x, "y:", y)
x, y = y, x
print("x:", x, "y:", y)
 
 

print()
print("---------------------------------------")
print()

 # Aufgabe 5

a = 10
b = 3

addition = a + b
subtraktion = a - b 
multiplikation = a * b
division = a / b
ganzzahl_division = a // b
modulo = a % b

print("Addition:", addition)
print("Multiplikation", multiplikation)
print("Subtraktion", subtraktion)
print("Divsion", division)
print("Ganzzahl Divission", ganzzahl_division)
print("Modulo", modulo)


print()
print("---------------------------------------")
print()

## Zusatz-Aufgabe 6

name = input("Bitte Namen eingeben: ")
alter = input("Bitte Alter eingeben: ")

## Ausgabe mit mehreren Argumenten durch Komma getrennt:
#print("Hallo", name, ", du bist", alter, "Jahre alt.")

# Ausgabe mit + als Konkatenationsoperator (Stringkonkatenation)
print("Hallo " + name + ", du bist " + alter + " Jahre alt.")
