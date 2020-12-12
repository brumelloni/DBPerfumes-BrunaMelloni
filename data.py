import sqlite3
connection = sqlite3.connect("Mestre dos Perfumes")
print(connection.total_changes)
cursor = connection.cursor()

cursor.execute("INSERT INTO perfumes VALUES (1, 'La Fleur', 5, 123, 321, 213)")
cursor.execute("INSERT INTO Perfumes VALUES (2, 'Le Rêve Bleu', 5, 456, 654, 546)")
