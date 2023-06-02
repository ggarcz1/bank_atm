# python requests login
import requests

url = 'http://127.0.0.1:5000/login_page?'
data = {'username':'admin',
        'password':'admin'}

response = requests.post(url=url, data=data, allow_redirects=True)

if response.status_code == 200:
    print('Successful login.')
elif response.status_code == 302:
    print('Redirect login')
else:
    print('Failed login')

print(response.content)
