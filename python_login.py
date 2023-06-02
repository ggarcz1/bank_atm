import requests, faker

url = 'http://127.0.0.1:5000/login_page?'
data = {'username':'admin',
        'password':'admin'}

fake_user = faker.name()
fake_password = faker.password()
fake_email = faker.emai()

data_new_user = {'username':'',
                'password':'',
                'email':''}
# new user
response_new_user = requests.post(url=url, data=data_new_user, allow_redirects=True)

# login
response_login = requests.post(url=url, data=data, allow_redirects=True)

if response_login.status_code == 200:
    print('Successful login.')
elif response_login.status_code == 302:
    print('Redirect login')
else:
    print('Failed login')

print(response_login.content)
