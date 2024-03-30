import hashlib
import sqlite3


def encyrpt(value: str) -> hex:
    return hashlib.sha256(value.encode()).hexdigest()


def addUser(username: str) -> hex:
    return encyrpt(username)


def addPassword(password: str) -> hex:
    return encyrpt(password)


sqliteConnection = sqlite3.connect('users.db')
cursor = sqliteConnection.cursor()

command1 = '''CREATE TABLE users (
id_number INTEGER PRIMARY KEY,
username VARCHAR(20),
password VARCHAR(30),
balance INTEGER;'''

cursor.execute(command1)

username = addUser(input('Enter username'))
password = addPassword(input('Enter password'))

command2 = '''INSERT INTO users VALUES(1,{},'Doe',12345 );'''
cursor.execute(command2)
sqliteConnection.commit()
sqliteConnection.close()
