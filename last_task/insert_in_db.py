#!/usr/bin/python3

import csv
import sqlite3
import sys

import datetime
def main(fname1, fname2):
    data = []

    with open(fname1) as fin:
        for user_id, time, bet, win in csv.reader(fin):
            if user_id == "#error":
                data.append(("NULL", '"' + time[1:] + '"', bet, win))
            else:
                print(datetime.datetime.fromisoformat(time[1:]))
                data.append((user_id.split()[4].split("_")[1], '"' + time[1:] + '"', bet, win))
    with open(fname2, encoding="koi8-r") as fn:
        for i in fn:
            print(i.split())
        # for user_id, email, geo 
        #     data.append((ts, sn, result))

        # data.sort()

    # with sqlite3.connect('dev-tests.s3db') as conn:
    #     cur = conn.cursor()
    #     for ts, sn, result in data:
    #         cur.execute('INSERT OR IGNORE INTO devices (sn) VALUES (?)', [sn])
    #         cur.execute(
    #             'INSERT INTO tests (device_id, ts, result)'
    #             ' VALUES ((SELECT id FROM devices WHERE sn = ?), ?, ?)',
    #             (sn, ts, result)
    #         )
    #     conn.commit()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])