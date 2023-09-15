import requests

BASE_URL = 'http://localhost:8080/v3/getPlan'
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImR"

headers = {'Authorization': "Bearer {}".format(token)}
auth_response = requests.get(BASE_URL, headers=headers)

print(auth_response.json())