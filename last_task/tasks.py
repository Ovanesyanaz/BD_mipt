import sqlite3

connection = sqlite3.connect('data.s3db')
cursor = connection.cursor()

#для получения названия полей 
# cursor.execute('PRAGMA table_info("sales")')
# column_names = [i[1] for i in cursor.fetchall()]
# print(column_names)


#task a
# cursor.execute(
# '''
# SELECT avg(CAST(visits as REAL) / CAST(bets as REAL))
# FROM 
#     (SELECT user_id, count(*)  as visits FROM LOG GROUP BY user_id) as visits,
#     (SELECT user_id, count(*) as bets FROM LOG WHERE bet != 0 GROUP BY user_id) as bets
# WHERE visits.user_id = bets.user_id
# ''')

#task b
# cursor.execute(
# '''
# SELECT avg(procent_win)
# FROM (
#     SELECT
#         case when sum(win) != 0
#         then (CAST(sum(win) as REAL) * 100.0) /  CAST(sum(bet) as REAL)
#         else 0
#         end as procent_win
#     FROM LOG group by user_id
# )
# ''')

# task c
# cursor.execute(
# '''
  # SELECT user_id, MAX(0, sum(win) - sum(bet))
  # FROM LOG group by user_id
# ''')

#task d
# cursor.execute('''
  # SELECT geo, sum(bet - win) as dohod
  # FROM LOG JOIN USERS ON USERS.user_id = LOG.user_id 
  # GROUP BY geo ORDER BY dohod DESC;
# ''')

# task e
# cursor.execute('''
  # SELECT geo, max(bet) as max_bet 
  # FROM LOG JOIN USERS ON USERS.user_id = LOG.user_id 
  # GROUP BY geo ORDER BY max_bet DESC;
# ''')

data = cursor.fetchall()
for d in data:
  print(d)
  print()

cursor.close()