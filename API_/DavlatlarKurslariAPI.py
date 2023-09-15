
# // https://v6.exchangerate-api.com/v6/02d4ef225a35eeb8c8dbce23/latest/USD
# import requests
# from pprint import pprint as print
# url = 'https://v6.exchangerate-api.com/v6/02d4ef225a35eeb8c8dbce23/latest/USD'
# response = requests.get(url)
# data = response.json()
# # print(data)
# print(data.get('conversion_rates').get('UZS'))


import requests
from pprint import pprint as print

API_KEY = '02d4ef225a35eeb8c8dbce23'
currency='USD'

# url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS'

response = requests.get(url)
# print(response.status_code)
# print(response.json())

jsondata = response.json()
kurs = jsondata['conversion_rate']
print(f"Bugungi kurs: 1$ = {kurs} so'm")