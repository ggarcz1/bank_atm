import requests
url = 'http://127.0.0.1:5000/login_page?'


data = {'username': 'admin', 'password': 'admin'}
response = requests.post(url=url, data=data)
print(response.text)