from flask import Flask, session, render_template, redirect, request, url_for
import sqlite3
import datetime
import random
from complexity import Complexity

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


global ids
ids = {}

# bug fix #2
# check if user exists
# returns true if value exists
def searchDB(database_name, username):
    sqliteConnection = sqlite3.connect(database=database_name)
    cursor = sqliteConnection.cursor()
    # check if user exists in the database already
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    database_results = cursor.fetchall()
    return len(database_results) != 0

def getPassword(username):
    #should always be 'users.db'
    sqliteConnection = sqlite3.connect('users.db')
    cursor = sqliteConnection.cursor()
    # check if user exists in the database already
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    database_password = cursor.fetchall()
    return database_password[0][0]

def log(email, pin, torf, type_of_log):
    # log 
    error = False
    if type_of_log == 'logon':
        file_name = 'logs.txt'
    elif type_of_log == 'password_reset':
        file_name = 'password_reset_logs.txt'
    else:
        file_name = None
    
    try:
        f = open(file_name, 'a')
        f.write(email+'\t'+pin+'\t'+torf)
    except:
        error = True

    return error

def get_account_details(username):      
    # if not searchDB('users.db',username=username):
    #     return None
    # else:
    #     account_details = {'first_name':'',
    #                    'last_name':'',
    #                    'balance': 0.0,
    #                    'email':'',
    #                    'account_number': '',
    #                    'pin':'',
    #                    'zipcode':0}
    #     sqliteConnection = sqlite3.connect('account_details.db')
    #     cursor = sqliteConnection.cursor()
    #     cursor.execute('SELECT * FROM account_details WHERE username=?', (username,))
    #     data = cursor.fetchall()
    #     #string
    #     account_details['first_name'] = data[0][0]
    #     #string
    #     account_details['last_name'] = data[0][1]
    #     #double
    #     account_details['balance'] = data[0][2]
    #     #string
    #     account_details['email'] = data[0][3]
    #     #string of 10 digits and upper/lowercase characters
    #     account_details['account_number'] = data[0][4]
    #     #number of 4 digits
    #     account_details['pin'] = data[0][5]
    #     #number with 5 digits
    #     account_details['zipcode'] = data[0][6]

        
        # for testing 
    account_details = {'first_name':'FirstName',
                        'last_name':'LastName',
                        'balance': 23344.12,
                        'email':'email@domain.com',
                        'account_number': '12345678',
                        'pin': 1234,
                        'zipcode': 12345}

    return account_details

# TODO:
def send_mfa(email):
    # match email regex here
    email = email
    return False

# TODO:
def reset_password_get_data(email, pin):
    account_details = {'email':'',
                       'pin': 0}
    
    # sqliteConnection = sqlite3.connect('account_details.db')
    # cursor = sqliteConnection.cursor()
    # cursor.execute('SELECT email,pin FROM account_details WHERE email=? AND pin=?', (email,pin))
    # data = cursor.fetchall()
    # account_details['email'] = data[0][0]
    # account_details['pin'] = data[0][1]
    # return account_details['email'] == email and account_details['pin'] == pin 

    # for testing
    account_details = {'email':'a@gmail.com',
                       'pin':1234}
    email = account_details['email']
    pin = account_details['pin']
    return account_details['email'] == email and account_details['pin'] == pin

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
        ip_port = request.host.split(':')
        host = ip_port[0] +'\t'+ip_port[1]
        logText = str(datetime.datetime.now())+'\t'+host+'\t'+username + '\t'+password+'\n'
        f.write(logText)
        f.close()
        # log(logText, )
        if len(username) == 0:
            return render_template('login_page.html', error='Username Field cannot be blank')
        elif len(password) == 0:
            return render_template('login_page.html', error='Password Field cannot be blank')

        if searchDB('users.db', username) and password == getPassword(username):
            session['user'] = username
            return redirect(url_for('logged_in'))
            # return redirect(url_for('logged_in', username=username))
        else:
            return render_template('login_page.html', error='Incorrect Credentials.')

    return render_template('login_page.html')

# change this route to '/' then do a homepage at path '/home'?
@app.route('/account', methods=['GET', 'POST'])
def logged_in():
    # bug fix #2
    # check if user exists
    username = session['user']

    # global ids
    # generated_id = random.randint(1,999999)
    # torf = True
    # while torf:
    #     if id[generated_id] is not None:
    #         generated_id = random.randint(1,999999)
    #     torf = False

    # session['id'] = generated_id
    # id[generated_id] = True

    if not searchDB('users.db', username):
        session['logged_in'] = True
        return render_template('login_page.html', error='Incorrect Credentials.')
    
    # get data on user from a database
    account_details = get_account_details(username)
    return render_template('account_page.html', first_name=account_details['first_name'], 
                           balance=account_details['balance'],
                           account_number=account_details['account_number'],
                           email=account_details['email'],
                           zipcode=account_details['zipcode'] 
                           )


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
        
        # TODO:
        # # password complexity check
        # instance = Complexity(values[1])
        # if not instance.test_password_complexity():
        #     return render_template('create_account.html', error='Password does not meet complexity requirements.')

        sqliteConnection = sqlite3.connect('users.db')
        cursor = sqliteConnection.cursor()
        # check if user exists in the database already
        cursor.execute('SELECT password FROM users WHERE username=?', (values[0],))
        database_password = cursor.fetchall()
        found_username = len(database_password) != 0

        #if not searchDB('users.db', username):
        if not found_username:
            # insert new user into db
            cursor.execute('INSERT INTO users VALUES (?, ?, ?)',values)
            sqliteConnection.commit()
            sqliteConnection.close()
            return redirect(url_for('account_created_successfully'))
        else:
            return render_template('create_account.html',error='Username already exists')
        
    return render_template('create_account.html', error='')

@app.route('/reset', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        # check database if user exists
        email = request.form['email']
        pin = request.form['pin']

        # if reset_password_get_data(email, pin):
        if reset_password_get_data(email=email, pin=pin):
            # send an email to the emial address for password reset link
            # set timer for it to be 10 minutes
            # log on server side
            log(email, pin, True)
            a = 1
        else:
            # do nothing
            a = 1
            # log error on server side
            log(email, pin, False)

    return redirect(url_for('post_post_pwd_reset'))
    
@app.route('/account_created_successfully', methods=['GET', 'POST'])
def account_created_successfully():
    return render_template('account_created_successfully.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logged_out_user = session['user']
    session['user'] = None
    session['logged_in'] = False
    idz = session['id']
    global id
    id.pop(session['id'])
    session['id'] = 'None'
    
    return render_template('logged_out.html', logged_out_user=idz)

if __name__=='__main__':
#    app.run(ssl_context=('cert.pem', 'key.pem'), host='127.0.0.1')
   app.run(host='127.0.0.1')