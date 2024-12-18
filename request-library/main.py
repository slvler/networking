import requests

response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.json())

data = {
    'name': 'john',
    'password': 123
}
r1 = requests.post("https://httpbin.org/post", data=data)
print(r1.status_code)
print(r1.json())

r2 = requests.get("https://httpbin.org/status/404")
if r2.status_code == requests.codes.not_found:
    print("not found")
else:
    print(response.status_code)

r3 = requests.get("https://httpbin.org/user-agent")
print(r3.text)

headers = {
    "User-Agent": "Mozilla/5.0 (platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version",
}
r4 = requests.get("https://httpbin.org/user-agent", headers=headers)
print(r4.text)

r5 = requests.get("https://httpbin.org/delay/5", timeout=4)
print(r5.text)