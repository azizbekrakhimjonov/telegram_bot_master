from google.auth.transport import requests
import json

url = "https://google-translate20.p.rapidapi.com/translate"

payload = "text=The%20POST%20method%20has%20several%20advantages%20over%20GET%3A%20it%20is%20more%20secure%20because%20most%20of%20the%20request%20is%20hidden%20from%20the%20user%3B%20Suitable%20for%20big%20data%20operations.&tl=es&sl=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "google-translate20.p.rapidapi.com",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.json)