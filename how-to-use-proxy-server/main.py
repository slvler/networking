import requests

proxies = {
    'https': 'https://xxxxxxxx'
}

response = requests.get("https://ipinfo.io/json", proxies=proxies)
print(response.text)
print(response.json()['country'])
print(response.json()['region'])