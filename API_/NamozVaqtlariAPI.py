# import requests
# from pprint import pprint as print
# url = "https://aladhan.p.rapidapi.com/timingsByCity"
# querystring = {"country":"Uzbekistan","city":"Toshkent","method":"8","latitudeAdjustmentMethod":"2"}
# headers = {
# 	"X-RapidAPI-Key": "0b765b51b6msh59006515055e2b2p1e1facjsnfa954e780c20",
# 	"X-RapidAPI-Host": "aladhan.p.rapidapi.com"
# }
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.json())

import requests
from pprint import pprint as print
sura=1
oyat=4
tafsir='uzb-muhammadsodikmu'
#
# # url_sura=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
# # r = requests.get(url_sura)
# # print(r.status_code)
# # res = r.json()
# # print(res)
#
url_oyat=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"
r = requests.get(url_oyat)
print(r.status_code)
print(r.json()['text'])