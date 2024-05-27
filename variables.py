# Variablen und Datentypen

## Kommentare

# Raute "#" für den einzeiligen Kommentar
# Drei aufeinanderfolgende Anführungszeichen (einfache oder doppelte) leiten einen 
# mehrzeiligen Kommentar ein. Dieser muss durch erneute Eingabe von drei Anführungszeichen
# wieder geschlossen/beendet werden.

"""Das hier ist ein 
mehrzeiliger Kommentar.

Er endet erst hier."""

## Integer

ganzezahl = 0
print("ganzezahl")   # Durch Anführungszeichen erfolgt die Ausgabe des Strings "ganzezahl"
                     # und nicht des Inhalts der Variablen ganzezahl
print(ganzezahl)

## Camel-Case Notation

ganzeZahl = 1
print("ganzeZahl:", ganzeZahl)   # Übergabe von zwei Argumenten an den Builtin print 
                                 # Builtin: in Python eingebaute Funktion

## Snake-Case Notation (Konvention in Python)

ganze_Zahl = 2
print("ganze_Zahl:", ganze_Zahl)

## Gleitkommazahlen

# Punkt ist Dezimaltrenner, daher müssen wir den Punkt als Trennzeichen nehmen
komma_zahl = 2.14    
print("komma_zahl:", komma_zahl)

"""Ausgabe des Datentyps der Variabel komma_zahl mit dem Builtin type()
type() produziert selbst keine Ausgabe (gibt nur einen konkreten Wert *zurück*)
daher brauchen wir zusätzlich print() für die Ausgabe auf der Konsole/in der Shell
"""
datentyp_komma_zahl = type(komma_zahl)
print(datentyp_komma_zahl)

# gleich wie oben, nur verkürzt auf eine Zeile 
# beide Schreibweisen sind zulässig, persönliche Vorliebe/Stilfrage
print(type(komma_zahl))

genauere_komma_zahl = 234.2983492387492837
print(genauere_komma_zahl)
print(type(genauere_komma_zahl))

