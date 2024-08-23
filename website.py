from flask import Flask, session, render_template, redirect, request, url_for
import sqlite3
import datetime
import os
import random
import re
from complexity import Complexity

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_SENDER'] = os.environ.get('MAIL_SENDER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')

# mail = Mail(app)
global ids
ids = {}

# bug fix #2
# check if user exists
# returns true if value exists
# TODO: remove the paramater 'database_name' as this function 
# always connects to users.db
def search_users_DB(database_name: str, username: str) -> bool:
    sqliteConnection = sqlite3.connect(database='users.db')
    cursor = sqliteConnection.cursor()
    # check if user exists in the database
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    database_results = cursor.fetchall()
    # returns true if value exists
    return len(database_results) != 0


def getPassword(username: str) -> str:
    # should always be 'users.db'
    sqliteConnection = sqlite3.connect('users.db')
    cursor = sqliteConnection.cursor()
    # check if user exists in the database already    
    cursor.execute('SELECT password FROM users WHERE username=?', (username,))
    database_password = cursor.fetchall()
    return database_password[0][0]

    # if search_users_DB(database_name='users.db', username=username):
    #     database_password = cursor.fetchall()
    #     return database_password[0][0]    

# TODO:
def log(data: dict) -> list:
    error = [False, 'Successfully Logged']
    # check for logtype field
    # TODO: make field length counts here as well
    if data['type_of_log'] is None:
        return ['True', 'Malformed log data.']
    
    path = 'Logs\\'
    logText = {}
    data_length = len(data)
    type_of_log = data['type_of_log']

    # delete after/add to documentation
    # logon --> 7 --> logtype, datetime, host, port, username, password, status
    # logout --> ? --> logtype, datetime, host, port, username, status, placeholder
    # password reset --> ? --> logtype, datetime, host, port, username, field_updated, status
    # update data on profile -->  ? --> logtype, datetime, host, port, username, field_updated, status
    # register account -->  ? --> logtype, datetime, host, port, username, field_updated, status

    # logtype, datetime, host, port, action, username, password, info, status
    # action --> ['logon', 'logout', 'password_reset', ]

    # TODO: add lengths for additional check
    if type_of_log == 'logon' and data_length == 7:
        file_name = path+'logs.txt'
        logText = f'{data["type_of_log"]}\t' \
                    f'{data["date_time"]}\t' \
                        f'{data["host"]}\t' \
                            f'{data["port"]}\t' \
                                f'{data["username"]}\t' \
                                    f'{data["password"]}\t' \
                                        f'{data["status"]}\n'

    # TODO:
    elif type_of_log == 'logout':
        file_name = path+'logout.txt'
        logText = f'{data["type_of_log"]}\t' \
                        f'{data["date_time"]}\t' \
                            f'{data["host"]}\t' \
                                f'{data["port"]}\t' \
                                    f'{data["username"]}\t' \
                                        f'{data["status"]}\n'
    
    # TODO:
    elif type_of_log == 'password_reset':
        file_name = path+'password_reset_logs.txt'
        logText = f'{data["type_of_log"]}\t' \
                        f'{data["date_time"]}\t' \
                            f'{data["host"]}\t' \
                                f'{data["port"]}\t' \
                                    f'{data["username"]}\t' \
                                                f'{data["status"]}\n'


    # TODO:
    elif type_of_log == 'update_account':
        file_name = path+'update_account_logs.txt'
        logText = f'{data["type_of_log"]}\t' \
                        f'{data["date_time"]}\t' \
                            f'{data["host"]}\t' \
                                f'{data["port"]}\t' \
                                    f'{data["username"]}\t' \
                                        f'{data["updated_field"]}\t' \
                                            f'{data["updated_data"]}\t' \
                                                f'{data["status"]}\n'
    
    # TODO:
    elif type_of_log == 'register_account':
        file_name = path+'register_account_logs.txt'
        logText = f'{data["type_of_log"]}\t' \
                        f'{data["date_time"]}\t' \
                            f'{data["host"]}\t' \
                                f'{data["port"]}\t' \
                                    f'{data["username"]}\t' \
                                        f'{data["status"]}\n'

    else:
        file_name = None

    try:
        f1 = open(file_name, 'a')
        # Note, master logs are not the same length for each type
        # will have to make a tool to parse them
        f2 = open('Logs\\master_logs.txt', 'a')
        
        f1.write(logText)
        f2.write(logText)

        f1.close()
        f2.close()

    except:
        error = [True, f'{Exception}']

    return error

def get_account_details(username: str) -> str:      
    if not search_users_DB('users.db', username=username):
        return None
    else:
        if username == 'admin':
            return 'admin'
        else:
            account_details = {'first_name':'',
                        'last_name':'',
                        'balance': 0.0,
                        'email':'',
                        'account_number': '',
                        'pin':'',
                        'zipcode':0}
            
            sqliteConnection = sqlite3.connect('account_details.db')
            cursor = sqliteConnection.cursor()
            cursor.execute('SELECT * FROM account_details WHERE first_name=?', (username,))
            data = cursor.fetchall()
            #string
            account_details['first_name'] = data[0][0]
            #string
            account_details['last_name'] = data[0][1]
            #double
            account_details['balance'] = "{:,}".format(data[0][2])
            # account_details['balance'] = data[0][2]
            #string
            account_details['email'] = data[0][3]
            #string of 10 digits and upper/lowercase characters
            account_details['account_number'] = data[0][4]
            #number of 4 digits
            account_details['pin'] = data[0][5]
            #number with 5 digits
            account_details['zipcode'] = data[0][6]

        
        # for testing 
    # account_details = {'first_name':'FirstName',
    #                     'last_name':'LastName',
    #                     'balance': 23344.12,
    #                     'email':'email@domain.com',
    #                     'account_number': '12345678',
    #                     'pin': 1234,
    #                     'zipcode': 12345}

    return account_details


# TODO:
def send_mfa(email: str) -> str:
    # via: https://chat.openai.com/c/8944d330-e1ec-490c-acf4-797ac2971e8a
    # Regular expression pattern for matching email addresses
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    torf = re.findall(email_regex, email)
    if torf:
        # do MFA Stuff
        return True
    else:
        # return false, do not do MFA stuff
        return False


# TODO:
def reset_password_get_data(email: str, pin: int) -> bool:
    account_details = {'email': '',
                       'pin': 0}

    # sqliteConnection = sqlite3.connect('account_details.db')
    # cursor = sqliteConnection.cursor()
    # cursor.execute('SELECT email,pin FROM account_details WHERE email=? AND pin=?', (email,pin))
    # data = cursor.fetchall()
    # account_details['email'] = data[0][0]
    # account_details['pin'] = data[0][1]
    # return account_details['email'] == email and account_details['pin'] == pin 

    # for testing
    account_details = {'email': 'a@gmail.com',
                       'pin': 1234}
    email = account_details['email']
    pin = account_details['pin']
    return account_details['email'] == email and account_details['pin'] == pin

# TODO:
# alert on possible brute force
def failure_count():
    # time
    global logon_failures
    logon_failures += 1
    if logon_failures > 10:
        print()
    return None

#TODO:
def send_admin_logon_alert():
    return

def display(filename):
    # if file exist
    f = open(f'Logs//{filename}')
    file_contents = ''
    for each in f:
        file_contents += f'{each}'

    return file_contents

# ----------------------------------------
# begin webpages code 
# ----------------------------------------

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/review_logs', methods=['GET'])
def review_logs():
    # check auth
    # MFA?
    f = open('Logs\\logs.txt')
    directory = 'Logs'  # Specify your directory here
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

    return render_template('logs.html', files=files)

@app.route('/login_page', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # f = open('Logs\\logs.txt', 'a')
        ip_port = request.host.split(':')
        host = ip_port[0]
        port = ip_port[1]

        if len(username) == 0:
            return render_template('login_page.html', error='Username Field cannot be blank')
        elif len(password) == 0:
            return render_template('login_page.html', error='Password Field cannot be blank')

        if search_users_DB('users.db', username) and password == getPassword(username):
            session['user'] = username
            # true logon
            status = 'SUCCESS'
            # logon --> 7 --> logtype, datetime, host, port, username, password, status
            log(data= {'type_of_log': 'logon',
                    'date_time': str(datetime.datetime.now()), 
                    'host': host,
                    'port': port, 
                    'username': username, 
                    'password': password,
                    'status': status})
            #TODO:
            # change this to be a flag from db
            if username == 'admin' and password == 'admin':
                send_admin_logon_alert()

            return redirect(url_for('logged_in'))
        else:
            status = 'FAILURE'
            # TODO: failure count
            # failure_count += 1
            log(data= {'type_of_log': 'logon',
                    'date_time': str(datetime.datetime.now()), 
                    'host': host,
                    'port': port, 
                    'username': username, 
                    'password': password,
                    'status': status})
            return render_template('login_page.html', error='Incorrect Credentials.')

    return render_template('login_page.html')


# change this route to '/' then do a homepage at path '/home'?
@app.route('/account', methods=['GET', 'POST'])
def logged_in():
    # bug fix #2
    # check if user exists
    try:
        username = session['user']
    except:
        return render_template('login_page.html', error='Incorrect Credentials.')

    # global ids
    # generated_id = random.randint(1,999999)
    # torf = True
    # while torf:
    #     if id[generated_id] is not None:
    #         generated_id = random.randint(1,999999)
    #     torf = False

    # session['id'] = generated_id
    # id[generated_id] = True

    if not search_users_DB('users.db', username):
        session['logged_in'] = False
        return render_template('login_page.html', error='Incorrect Credentials.')

    # get data on user from a database
    account_details = get_account_details(username)
    if account_details == 'admin':
        # session['logged_in'] = True
        # session['username'] = 'admin'
        return render_template('admin_pannel.html')
    
    else:
        return render_template('account_page.html', first_name=account_details['first_name'],
                           balance=account_details['balance'],
                           account_number=account_details['account_number'],
                           email=account_details['email'],
                           zipcode=account_details['zipcode']
                           )


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        error = username = None
        status = True
        values = [request.form['username'],
                  request.form['password'],
                  request.form['re_enter_password'],
                  request.form['email']
                  ]

        # TODO:
        # do i build it such that all are logged?
        # i.e., if a POST is missin all fields, what is logged?

        if len(values[0]) == 0:
            error = 'Username Field cannot be blank'
            status = False

        elif len(values[1]) == 0:
            error = 'Password Field cannot be blank'
            status = False

        elif len(values[2]) == 0:
            error = 'Re-Enter Password Field cannot be blank'
            status = False

        elif len(values[3]) == 0:
            error = 'Email Field cannot be blank'
            status = False

        # check password with re-entered password here
        # to break off before it is even sent to DB
        if values[1] != values[2]:
            error = 'Passwords do not match'
            status = False

        if not status:
            log(data= {'type_of_log': 'register_account',
                'date_time': str(datetime.datetime.now()), 
                    'host': host,
                        'port': port,
                            'username': 'None', 
                                'status': error})

            return render_template('create_account.html', error=error)
        
        # TODO:
        # password complexity check
        # if not Complexity.test_password_complexity(values[1]):
        #     return render_template('create_account.html', error='Password does not meet complexity requirements.')

        sqliteConnection = sqlite3.connect('users.db')
        cursor = sqliteConnection.cursor()
        # check if user exists in the database already
        cursor.execute('SELECT password FROM users WHERE username=?', (values[0],))
        database_password = cursor.fetchall()
        found_username = len(database_password) != 0

        # if not search_users_DB('users.db', username):
        if not found_username:
            # insert new user into db
            cursor.execute('INSERT INTO users VALUES (?, ?, ?)', values)
            sqliteConnection.commit()
            sqliteConnection.close()
            log(data= {'type_of_log': 'register_account',
            'date_time': str(datetime.datetime.now()), 
            'host': host,
            'port': port, 
            'username': values[0], 
            'status': 'Success'})
            return redirect(url_for('account_created_successfully'))
        else:
            error = 'Username already exists'
            log(data= {'type_of_log': 'register_account',
                'date_time': str(datetime.datetime.now()), 
                    'host': host,
                        'port': port, 
                            'username': values[0], 
                                'status': error})

            return render_template('create_account.html', error=error)

    return render_template('create_account.html', error='')


@app.route('/reset', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        # check database if user exists
        email = request.form['email']
        pin = request.form['pin']

        # if reset_password_get_data(email, pin):
        if reset_password_get_data(email=email, pin=pin):
            # email the email address for password reset link
            # set timer for it to be 10 minutes
            # log on server side
            log(email, pin, True)
            a = 1
            msg = Message('Password Reset', recipients=[email])
            mail.send(msg)
        else:
            # do nothing
            a = 1
            # log error on server side
            log(data= {'type_of_log': 'logon',
                    'date_time': str(datetime.datetime.now()), 
                    'host': host,
                    'port': port, 
                    'username': username, 
                    'password': password,
                    'status': status})
            log(email, pin, False)

    return redirect(url_for('post_post_pwd_reset'))


@app.route('/account_created_successfully', methods=['GET', 'POST'])
def account_created_successfully():
    return render_template('account_created_successfully.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logged_out_user = session['user']
    if logged_out_user is None or logged_out_user == 'None':
        log(data= {'type_of_log': 'logout',
                    'date_time': str(datetime.datetime.now()), 
                        'host': host,
                            'port': port, 
                                'username': 'None', 
                                        'status': 'Error. user "None" tried to logout.'})
        # return redirect('login_page.html', )
        return render_template('login_page.html', error='Error. user "None" tried to logout.')

    session['user'] = None
    session['logged_in'] = False

    status = 'Failure'

    if session['user'] == None:
        status = 'Success'
    else:
        status = 'Failure'

    log(data= {'type_of_log': 'logout',
                    'date_time': str(datetime.datetime.now()), 
                        'host': host,
                            'port': port, 
                                'username': logged_out_user, 
                                        'status': status})
    
    return render_template('logged_out.html', logged_out_user=logged_out_user)


if __name__ == '__main__':
    ## HTTPS item
    #    app.run(ssl_context=('cert.pem', 'key.pem'), host='127.0.0.1')
    host = '127.0.22.1'
    port = '9999'
    app.run(host=f'{host}', port=f'{port}')
