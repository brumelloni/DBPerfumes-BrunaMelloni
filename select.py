import sqlite3
connection = sqlite3.connect("Mestre dos Perfumes")
print(connection.total_changes)
cursor = connection.cursor()

rows = cursor.execute("SELECT id, nome, quantidade, id_volume_FK, id_marca_FK, id_fixacao_FK FROM perfumes")
print(rows)
