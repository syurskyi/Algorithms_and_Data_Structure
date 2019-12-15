import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT LastName, City from Employee WHERE City = 'Calgary' ORDER BY LastName limit 7")
results = cursor.fetchall()
for result in results:
    print(result)
#
# cursor.execute("insert into Artist values (Null, 'Сектор газа') ")
# conn.commit()
# new_artists = [
#    ('A Aagrh!',),
#   ('A Aagrh!-2',),
#    ('A Aagrh!-3',),
# ]
# cursor.executemany("insert into Artist values (Null, ?);", new_artists)
# conn.commit()
conn.close()
