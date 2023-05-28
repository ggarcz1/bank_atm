from flask import Flask, session, render_template, redirect, request, url_for
import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login_page', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # log to file
        f = open('logs.txt', 'a')
        logText = str(datetime.datetime.now())+'\t'+username + '\t'+password+'\n'
        f.write(logText)
        f.close()

        found_username = False
        sqliteConnection = sqlite3.connect('users.db')
        cursor = sqliteConnection.cursor()
        # check if user exists and get password
        cursor.execute('SELECT password FROM users WHERE username=?', (username,))
        database_password = cursor.fetchall()
        sqliteConnection.close()
        found_username = len(database_password) != 0
        # print(database_password)
        # print(len(database_password) != 0)
        # print(len(database_password))
        
        if found_username and password == database_password[0][0]:
            session['user'] = username
            return redirect(url_for('logged_in', username=username))
        else:
            return render_template('login_page.html')

    return render_template('login_page.html')

@app.route('/user/<username>', methods=['GET', 'POST'])
def logged_in(username):
    # get data on user from a database 
    balance = 0
    account_number = 1234567890
    first_name =username+', Real_name'
    return render_template('account_page.html', first_name=first_name, account_number=account_number, balance=balance)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        values = [request.form['username'], request.form['password'], request.form['email']]
        if len(values[0]) == 0:
            return render_template('create_account.html', error='Username Field cannot be blank')
        elif len(values[1]) == 0:
            return render_template('create_account.html', error='Password Field cannot be blank')
        elif len(values[2]) == 0:
            return render_template('create_account.html', error='Email Field cannot be blank')
        
        sqliteConnection = sqlite3.connect('users.db')
        cursor = sqliteConnection.cursor()
        # check if user exists in the database already
        cursor.execute('SELECT password FROM users WHERE username=?', (values[0],))
        database_password = cursor.fetchall()
        found_username = len(database_password) == 0
        if found_username:
            cursor.execute('INSERT INTO users VALUES (?, ?, ?)',values)
            sqliteConnection.commit()
            sqliteConnection.close()
            return redirect(url_for('account_created_successfully'))
        else:
            return render_template('create_account.html',error='Username already exists')
        
    return render_template('create_account.html', error='')


@app.route('/account_created_successfully', methods=['GET', 'POST'])
def account_created_successfully():
    return render_template('account_created_successfully.html')

@app.route('/logout')
def logout():
    session['user'] = None
    return 'Logged out' + '\n' + str(session['user'])
if __name__=='__main__':
   app.run('127.0.0.1')