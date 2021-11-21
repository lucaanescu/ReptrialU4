import sqlite3

connection = sqlite3.connect('demo_data.sqlite3')

cursor = connection.cursor()
cursor.execute("CREATE TABLE S ('s', 'x', 'y')")

cursor.execute("INSERT INTO s VALUES ('g', 3, 9)")
cursor.execute("INSERT INTO s VALUES ('v', 5, 7)")
cursor.execute("INSERT INTO s VALUES ('f', 8, 2)")
cursor.execute("INSERT INTO s VALUES ('r', 4, 3)")
cursor.execute("INSERT INTO s VALUES ('u', 8, 10)")