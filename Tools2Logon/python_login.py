import requests
from faker import Faker

fake = Faker()

url = 'http://127.0.0.1:5000/'
data = {'username': 'admin',
        'password': 'admin'}

fake_arr = [fake.user_name(), fake.password(), fake.email()]

data_new_user = {'username': fake_arr[0],
                 'password': fake_arr[1],
                 'email': fake_arr[2]}
# new user
response = requests.post(url=url + 'create_account', data=data_new_user, allow_redirects=True)

# login
# response = requests.post(url=url+'login_page?', data=data, allow_redirects=True)

if response.status_code == 200:
    print('Successful action.')
elif response.status_code == 302:
    print('Redirect action')
else:
    print('Failed action')

print(response.content)
