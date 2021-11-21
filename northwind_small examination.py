import sqlite3

connection = sqlite3.connect('northwind_small.sqlite3')

cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]

cursor.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()

cursor.execute('SELECT * FROM Product WHERE UnitPrice = '
               '(SELECT MAX(UnitPrice) FROM Product) ORDER BY UnitPrice DESC LIMIT 10;')

cursor.execute('age = SELECT HireDate FROM Employee')

cursor.execute('SELECT AVG(column_name);')

