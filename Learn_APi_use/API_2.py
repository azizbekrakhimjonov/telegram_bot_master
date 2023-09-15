# import json, requests
#
# url = requests.get("https://github.com/fawazahmed0/quran-api")
# text = url.text
#
# data = json.loads(text)
# user = data[1]
#
# address = user['address']
# print(address)

import requests
from getpass import getpass

with requests.Session() as session:
    session.auth = ('username', getpass())
    response = session.get('https://api.github.com/user')

print(response.headers)
print(response.json())