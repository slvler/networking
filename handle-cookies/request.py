import requests

s = requests.session()

login_url = 'http://127.0.0.1:5000/login'
login_data = {'username': 'john', 'password': 'doe'}

res = s.post(login_url, json=login_data)


if res.json().get('successs'):
    print('login')
else:
    print('failed')


protected_url = 'http://127.0.0.1:5000/prorected'

res = s.get(protected_url)

if res.json().get('successs'):
    print('login')
else:
    print('failed')
