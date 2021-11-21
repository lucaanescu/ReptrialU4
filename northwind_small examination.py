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

cursor.execute('SELECT Id, RIGHT DATEDIFF(HireDate, BirthDate) AS Age FROM Employee;')

cursor.execute('SELECT AVG(Age);')

cursor.execute('SELECT * FROM Product WHERE UnitPrice = '
               '(SELECT MAX(UnitPrice, SupplierId) FROM Product) ORDER BY UnitPrice DESC LIMIT 10;')

cursor.execute('SELECT COUNT( DISTINCT Category, Customer, CustomerCustomerDemo, '
               'CustomerDemographic, Employee, EmployeeTerritory, Order, OrderDetail,'
               ' Product, Region, Shipper, Supplier, Territory)'
               ' as totalDist FROM northwind_small WHERE totalDif = (SELECT MAX(totalDist) ORDER BY totalDif);')

"The relationship between employee and territory is a many-to-many relationship. " \
"This is because an employee can be part of several territories," \
" but a territory can also have multiple employees working in it. The key id is the RegionID and Region name"

"MongoDB is better for building many databases that are interconnected. " \
"It is best used for large projects with many complicated parts. " \
"It is not well used for small projects with a single large database."

"New SQL is similar to sql as it works the same way, but is built on the foundation of it to provide a faster and looser use of queries." \
"It's goald are to make working on projects easyer and opening up query types."
