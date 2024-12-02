import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('db.s3db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS LOGS (
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    time TEXT NOT NULL PRIMARY KEY,
    bet INTEGER,
    win INTEGER
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS USERS (
    user_id INTEGER UNIQUE PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    geo TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()