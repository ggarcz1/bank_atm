import sqlite3
from faker import Faker

sqliteConnection = sqlite3.connect('users.db')
cursor = sqliteConnection.cursor()

##search for a user
# username = 'admin'
# cursor.execute("SELECT password FROM users WHERE username=?", (username,))
# print(cursor.fetchall())
# cursor.execute("DELETE FROM users WHERE username=?",('John',))

#print out all users in the db
cursor.execute("SELECT * FROM users",)
lst = cursor.fetchall()
print('Username, Password, Email')
for idx in range(len(lst)):
    print(lst[idx])

fake = Faker()
data_to_add = ['']
for _ in range(10):
    name = fake.name().split(' ')
    email = fake.email()
    
# print(cursor.fetchall())
## add a user
# values = ['John','Doe','johnDoe@example.com']
# cursor.execute("INSERT INTO users VALUES (?, ?, ?)",values)

sqliteConnection.commit()
sqliteConnection.close()