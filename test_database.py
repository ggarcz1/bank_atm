import sqlite3
from faker import Faker



def account_data():

    sqliteConnection = sqlite3.connect('account_details.db')
    cursor = sqliteConnection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS account_details (
        first_name TEXT,
        last_name TEXT, 
        balance DOUBLE, 
        email TEXT, 
        account_number INTEGER, 
        pin INTEGER, 
        zipcode INTEGER
        )
    ''')

# already added these 3
    # account_details = ['tom', 
    #                    'tom',
    #                    43232.82,
    #                    'tom@tom.com',
    #                    839284661,
    #                    8392,
    #                    75234]
    
    # account_details2 = ['admin', 
    #                    'admin',
    #                    None,
    #                    'admin@admin.com',
    #                    None,
    #                    None,
    #                    None]

    # account_details3 = ['JOE', 'doe',100.0, 'joe@joe.com', 123456789, 1234, 12345]
    
    # cursor.execute('INSERT INTO account_details VALUES (?, ?, ?, ?, ?, ?, ?)', account_details)
    # cursor.execute('INSERT INTO account_details VALUES (?, ?, ?, ?, ?, ?, ?)', account_details2)
    # cursor.execute('INSERT INTO account_details VALUES (?, ?, ?, ?, ?, ?, ?)', account_details3)
    # sqliteConnection.commit()

    # print the database
    cursor.execute('SELECT * FROM account_details',)
    lst = cursor.fetchall()
    print('first_name, last_name, balance, email, account_number, pin, zipcode')
    for idx in range(len(lst)):
        print(lst[idx])
    sqliteConnection.close()

def users():
    sqliteConnection = sqlite3.connect('users.db')
    cursor = sqliteConnection.cursor()
    ##search for a user
    # username = 'admin'
    # cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    # print(cursor.fetchall())
    # cursor.execute('DELETE FROM users WHERE username=?',('John',))

    #print out all users in the db
    cursor.execute('SELECT * FROM users',)
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
    # cursor.execute('INSERT INTO users VALUES (?, ?, ?)',values)

    sqliteConnection.commit()
    sqliteConnection.close()

print('Account Data\n#######################################')
account_data()

print('Users\n#######################################')
users()