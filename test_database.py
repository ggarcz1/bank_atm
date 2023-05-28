import sqlite3

sqliteConnection = sqlite3.connect('users.db')
cursor = sqliteConnection.cursor()
username = 'admin'
cursor.execute("SELECT password FROM users WHERE username=?", (username,))
print(cursor.fetchall())
cursor.execute("SELECT * FROM users",)
print(cursor.fetchall())
values = ['John','Doe','johnDoe@example.com']
# cursor.execute("INSERT INTO users VALUES (?, ?, ?)",values)
# cursor.execute("DELETE FROM users WHERE username=?",('a',))

sqliteConnection.commit()
sqliteConnection.close()