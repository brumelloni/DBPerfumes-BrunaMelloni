import sqlite3
connection = sqlite3.connect("Mestre dos Perfumes")
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute("CREATE TABLE perfumes (id INTEGER, nome VARCHAR, quantidade INTEGER, id_volume_FK INTEGER,id_marca_FK INTEGER, id_fixacao_FK INTEGER, PRIMARY KEY(id, id_volume_FK, id_marca_FK, id_fixacao_FK))")
cursor.execute("CREATE TABLE marcas (id INTEGER PRIMARY KEY, nome VARCHAR, FOREIGN KEY (id) REFERENCES perfumes (id_marca_FK))")
cursor.execute("CREATE TABLE fixacoes (id INTEGER PRIMARY KEY, nome VARCHAR, FOREIGN KEY (id) REFERENCES perfumes (id_fixacao_FK))")
cursor.execute("CREATE TABLE volumes (id INTEGER PRIMARY KEY, nome VARCHAR, FOREIGN KEY (id) REFERENCES perfumes (id_volume_FK))")
cursor.execute("CREATE TABLE essencia_perfume (id_essencia_FK INTEGER, id_perfume INTEGER, PRIMARY KEY(id_essencia_FK, id_perfume), FOREIGN KEY (id_perfume) REFERENCES perfumes (id))")
cursor.execute("CREATE TABLE essencias (id INTEGER PRIMARY KEY, nome VARCHAR, FOREIGN KEY (id) REFERENCES essencia_perfume (id_essencia_FK))")