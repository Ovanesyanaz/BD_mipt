import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('dev-tests.s3db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM devices')
devices = cursor.fetchall()

# Выводим результаты
for device in devices:
  print(device)

# Закрываем соединение
connection.close()