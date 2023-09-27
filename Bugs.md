Bug #1:

Traversal to a user without authentication:
http://127.0.0.1:5000/user/{username}
enumeration via bruteforce of usernames of this address and an apprpriate response (200)
See bug_1.py for exploit


Bug #2:
all users are valid using bug#1, there is no check for this --> further development of the backend database