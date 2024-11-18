import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('dev-tests.s3db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
id INTEGER PRIMARY KEY AUTOINCREMENT,
sn TEXT NOT NULL UNIQUE
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS tests (
id INTEGER PRIMARY KEY AUTOINCREMENT,
ts INTEGER NOT NULL,
device_id INTEGER NOT NULL REFERENCES devices(id),
result INTEGER --0 - fail, 1 - passed
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()