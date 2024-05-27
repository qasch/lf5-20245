name = input("Bitte Namen eingeben: ")
alter = input("Bitte Alter als Zahl eingeben: ")
# Explizites Casting (Umwandlung in einen bestimmten Datentyp)

# Prüfung, ob alter als Zahl eingegeben wurde
if alter.isdigit():
    alter = int(alter)

    geburtsjahr = 2024 - alter
    ## Ausgabe mit mehreren Argumenten durch Komma getrennt:
    #print("Hallo", name, ", du bist", alter, "Jahre alt.")

    # Ausgabe mit + als Konkatenationsoperator (Stringkonkatenation)
    print("Hallo " + name + ", du bist " + str(alter) + " Jahre alt, d.h. du bist im Jahr " + str(geburtsjahr) + " geboren.")
else:
    print(str(alter) + "ist keine Zahl. Abbruch.")

