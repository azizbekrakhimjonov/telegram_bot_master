import requests
from pprint import pprint as print
# url = "https://shazam-core.p.rapidapi.com/v1/artists/details"
#
# querystring = {"artist_id":"78630"}
#
# headers = {
# 	"X-RapidAPI-Key": "0b765b51b6msh59006515055e2b2p1e1facjsnfa954e780c20",
# 	"X-RapidAPI-Host": "shazam-core.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.json())



url = "https://t-one-youtube-converter.p.rapidapi.com/api/v1/createProcess"

querystring = {"url":"https://youtu.be/dVG5WwMiG-Y","format":"mp3","responseFormat":"json","regenerate":"true","volume":"50","lang":"en"}

headers = {
	"X-RapidAPI-Key": "0b765b51b6msh59006515055e2b2p1e1facjsnfa954e780c20",
	"X-RapidAPI-Host": "t-one-youtube-converter.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())