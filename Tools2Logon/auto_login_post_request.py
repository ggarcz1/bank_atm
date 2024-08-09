import requests
import time

url = 'http://127.0.22.1:9999/login_page?'

lst1 = []
lst2 = []

if len(lst1) == 0 or len(lst2) == 0:
    print(f'Empty list found: \nList 1: {lst1}\nList 2: {lst2}')

for username in lst1:
    for password in lst2:
        data = {'username': f'{username}',
                'password': f'{password}'}
        response = requests.post(url=url, data=data)
        time.sleep(1)

data = {'username': 'sd',
        'password': 'ds'}
response = requests.post(url=url, data=data)
print(response.text)
