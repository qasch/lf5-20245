# Funktionen in Python

# 1. Funktionsdeklaration
def gib_immer_das_gleiche_aus():
    print("Hallo")
    print("ich")
    print("bin")
    print("eine")
    print("Funktion")

def gib_etwas_bestimmtes_aus(text):  # Parameter
    print(text)

def addiere(zahl1, zahl2):
    summe = zahl1 + zahl2
    # return summe     # Ende der Funktion, summe wird 'zurückgegeben'
    print("Hallo")   # wird niemals erreicht/ausgeführt, da nach return
    print(summe)

# 2. Funktionsaufruf (muss *nach* der Deklaration kommen)
# gib_immer_das_gleiche_aus()

# gib_etwas_bestimmtes_aus("etwas ganz anderes")   # Argument

print(addiere(4, 9))
print("nach funktion 1")
ergebnis = addiere(123, 98)
print("nach funktion 2")

def produkt_aus_summen(wert1, wert2):
    return addiere(wert1, wert2) * addiere(wert1, wert2)

# foo = "bla"
# print(type(foo))

print(produkt_aus_summen(4, 2))

