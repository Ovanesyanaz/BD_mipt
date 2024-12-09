
import csv
import sqlite3
import sys

cursor = sqlite3.connect("data.s3db")

cursor.commit()
def main(argv1, argv2):
    with open(argv1, encoding='koi8-r') as user:
        user.readline()
        for user_id, email, geo in csv.reader(user, delimiter='\t'):
            user_id = user_id if user_id else None
            email = email if email else None
            geo = geo if geo else None
            cursor.execute("INSERT INTO USERS_DIRTY VALUES (?, ?, ?)", (user_id, email, geo))
        cursor.commit()

    with open(argv2, encoding="utf8") as log:
        for user_id, time, bet, win in csv.reader(log):
            user_id = user_id if user_id else None
            time = time if time else None
            bet = int(bet) if bet else 0
            win = int(win) if win else 0
            cursor.execute("INSERT INTO LOG_DIRTY (user_id, time, bet, win) VALUES (?, ?, ?, ?)", (user_id, time, bet, win))
        cursor.commit()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])