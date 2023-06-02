import sqlite3

sqliteConnection = sqlite3.connect('users.db')
cursor = sqliteConnection.cursor()
# username = 'admin'
# cursor.execute("SELECT password FROM users WHERE username=?", (username,))
# print(cursor.fetchall())
# cursor.execute("DELETE FROM users WHERE username=?",('John',))

cursor.execute("SELECT * FROM users",)
lst = cursor.fetchall()
print('Username, Password, Email')
for idx in range(len(lst)):
    print(lst[idx])


# print(cursor.fetchall())
# values = ['John','Doe','johnDoe@example.com']
# cursor.execute("INSERT INTO users VALUES (?, ?, ?)",values)

sqliteConnection.commit()
sqliteConnection.close()