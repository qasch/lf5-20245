import sqlite3

try:
    # relativer Pfad zur Datenbanksdatei
    path_to_db = "personenverwaltung.db"

    # file = open(path_to_db, 'r')

    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect(path_to_db)

    # Cursor Objekt erzeugen
    cursor = connection.cursor()

    # SQL Statement definieren (kann *beliebiges* SQL sein)
    sql_statement = "SELECT Nachname FROM Person"

    # SQL Statement ausführen
    cursor.execute(sql_statement)

    # Ergebnis in result speichern (ist dann eine List aus Tuples)
    result = cursor.fetchmany()

    # Einzelne Datensätze anzeigen bzw. auf bestimmte Felder zugreifen
    for row in result:
        print(f"Nachname: {row[1]}")

    # Verbindung zur Datenbank wieder schliessen
    cursor.close()
except sqlite3.Error as e:
    print(f"Folgender Fehler ist aufgetreten: {e}")
finally:
    if connection:
        connection.close()
    print("Datenbankverbindung wurd geschlossen.")




# try:
#     # wird auszuführen versucht
# except:
#     # wird ausgeführt, falls try - Block nicht möglich ist