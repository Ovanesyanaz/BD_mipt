import sqlite3

connection = sqlite3.connect('train_db.db')
cursor = connection.cursor()

#для получения названия полей 
# cursor.execute('PRAGMA table_info("sales")')
# column_names = [i[1] for i in cursor.fetchall()]
# print(column_names)

#task 1

# cursor.execute('SELECT FirstName, LastName FROM customers WHERE City = "Prague"')
# users = cursor.fetchall()
# for user in users:
#   print(user)
#   print()

#task 2
# cursor.execute('SELECT FirstName, LastName FROM customers WHERE (SELECT instr(FirstName, "M") = 1) or (SELECT instr(FirstName, "ch") > 0) or (SELECT instr(FirstName, "Ch") > 0)')
# users = cursor.fetchall()
# for user in users:
#   print(user)
#   print()

#task 3
# cursor.execute('SELECT bytes / 1048576.0 FROM tracks')
# tracks = cursor.fetchall()
# for track in tracks:
#   print(track)
#   print()

#task 4
# cursor.execute('SELECT LastName, FirstName FROM employees WHERE city = "Calgary" and (SELECT instr((HireDate), "2002") = 1) ')
# employees = cursor.fetchall()
# for employee in employees:
#   print(employee)
#   print()

#task 5
# cursor.execute('SELECT LastName, FirstName FROM employees WHERE date(HireDate, "-40 year") > date(BirthDate)')
# employees = cursor.fetchall()
# for employee in employees:
#   print(employee)
#   print()

#task 6
# cursor.execute("SELECT FirstName, Fax FROM customers WHERE Country = 'USA' and Fax is NULL")
# users = cursor.fetchall()
# print()
# for user in users:
#   print(user)
#   print()
# connection.close()

#task 7

# cursor.execute("SELECT ShipCity FROM sales WHERE ShipCountry = 'Canada' and ((SELECT instr(SalesDate, '09') = 6) or (SELECT instr(SalesDate, '08') = 6))")
# sales = cursor.fetchall()
# print()
# for sale in sales:
#   print(sale)
#   print()

#task 8

# cursor.execute('SELECT Email FROM customers WHERE (SELECT instr(Email, "gmail.com") > 0)')
# users = cursor.fetchall()
# for user in users:
#   print(user)
#   print()


#task 9

# cursor.execute('SELECT * FROM employees WHERE date("now", "-18 year") > date(HireDate)')
# employees = cursor.fetchall()
# for employee in employees:
#   print(employee)
#   print()

# task 10

# cursor.execute('SELECT DISTINCT Title FROM employees ORDER BY Title')
# employees = cursor.fetchall()
# for employee in employees:
#   print(employee)
#   print()

#task 11

# cursor.execute('SELECT LastName, FirstName, Age FROM customers ORDER BY LastName, FirstName, Age')
# users = cursor.fetchall()
# for user in users:
#   print(user)
#   print()

#task 12

# cursor.execute('SELECT min(milliseconds)/1000.0 FROM tracks')
# tracks = cursor.fetchall()
# for track in tracks:
#   print(track)
#   print()

#task 13

# cursor.execute('SELECT Name, min(milliseconds)/1000.0 FROM tracks')
# tracks = cursor.fetchall()
# for track in tracks:
#   print(track)
#   print()

#task 14

# cursor.execute('SELECT Country, avg(Age) FROM customers GROUP BY Country')
# users = cursor.fetchall()
# for user in users:
#   print(user)
#   print()

#task 15 

# cursor.execute('SELECT LastName FROM employees WHERE (SELECT instr(HireDate, "10") = 6)')
# employees = cursor.fetchall()
# for employee in employees:
#   print(employee)
#   print()

#task 16

# cursor.execute('SELECT LastName FROM employees WHERE HireDate = (SELECT min(HireDate) FROM employees)')
# employees = cursor.fetchall()
# for employee in employees:
#   print(employee)
#   print()