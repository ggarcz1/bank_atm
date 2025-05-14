# bank_atm

Welcome to the README for the Bank Website application, ATM, and the underlying directories

Steps to run:

1. Download
2. Move the folder to the appropriate directory
3. Run `pip install -r requirements.txt`
4. Run `python ./website.py`
5. Vist associated host and port, default is ```http://127.0.0.1:5000```

`python_login.py` is a auto login/add new user based on requests library

`databaseTest\test_database.py` tests the database contents

### Current To-Do Items ###

1. Make the README Better
2. Add a database for bank account details
3. MFA or email to reset password
4. Log IP Address that has logon to the website --> done 
5. Lockout counter for brute force logon attempts --> in process
6. check for potential SQL injections via the logs (SQLMap)
7. Encrypt database usernames and passwords
8. Logging method


## Accounts Loaded For Database (account_details.db) testing \
```first_name, last_name, balance, email, account_number, pin, zipcode```

```
('tom', 'tom', 43232.82, 'tom@tom.com', 839284661, 8392, 75234)
('admin', 'admin', None, 'admin@admin.com', None, None, None)
('JOE', 'doe', 100.0, 'joe@joe.com', 123456789, 1234, 12345)
```