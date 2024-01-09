import sqlite3
from faker import Faker



def account_data():

    sqliteConnection = sqlite3.connect('account_details.db')
    cursor = sqliteConnection.cursor()

    # cursor.execute('''CREATE TABLE IF NOT EXISTS account_details (
    #     first_name TEXT,
    #     last_name TEXT, 
    #     balance DOUBLE, 
    #     email TEXT, 
    #     account_number INTEGER, 
    #     pin INTEGER, 
    #     zipcode INTEGER
    #     )
    # ''')

    account_details = ['testFirst', 
                       'testLast',
                       100.00,
                       'test@test.com',
                       123456789,
                       1234,
                       12345]
    
    # cursor.execute("INSERT INTO users VALUES (?, ?, ?)",values)

    cursor.execute("INSERT INTO account_details VALUES (?, ?, ?, ?, ?, ?, ?)", account_details)

    cursor.execute(f"SELECT * FROM account_details",)
    print(cursor.fetchall())

    sqliteConnection.commit()
    sqliteConnection.close()

def users():
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

    # fake = Faker()
    # data_to_add = ['']
    # for _ in range(10):
    #     name = fake.name().split(' ')
    #     email = fake.email()
        
    # print(cursor.fetchall())
    ## add a user
    # values = ['John','Doe','johnDoe@example.com']
    # cursor.execute("INSERT INTO users VALUES (?, ?, ?)",values)

    sqliteConnection.commit()
    sqliteConnection.close()



# account_data()
users()