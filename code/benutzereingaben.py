name = input("Bitte Namen eingeben: ")
alter = input("Bitte Alter eingeben: ")
# Explizites Casting (Umwandlung in einen bestimmten Datentyp)
alter = int(alter)

geburtsjahr = 2024 - alter
## Ausgabe mit mehreren Argumenten durch Komma getrennt:
#print("Hallo", name, ", du bist", alter, "Jahre alt.")

# Ausgabe mit + als Konkatenationsoperator (Stringkonkatenation)
print("Hallo " + name + ", du bist " + str(alter) + " Jahre alt, d.h. du bist im Jahr " + str(geburtsjahr) + " geboren.")