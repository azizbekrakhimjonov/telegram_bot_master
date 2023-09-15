import requests

# response = requests.get("http://randomfox.ca/floof")
# print(response.status_code)
# print(response.text)
# print(response.json())
# fox = response.json()
# print(fox['image'])

# import requests
# import os
# from datetime import datetime
#
# user_api = os.environ['current_weather_data']
# location = input('enter the city name: ')
#
# complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+user_api
# api_link = requests.get(complete_api_link)
# api_data = api_link.json()
#
# if api_data['cod'] == '404':
#     print("invalid City: {}, Please check you City name".format(location))
# else:
#     temp = ((api_data['main']['temp']-273.15))
#     weather_desc = api_data['weather'][0]['description']
#     hmdt = api_data['main']['humidity']
#     wind_spd = api_data['wind']['speed']
#     date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S:%p")
#
#     print("Weather stats for - {} || {}".format(location.upper(), date_time))
#
#     print("current temperature is {:.2f} deg C".format(temp))
#     print("current weather des  :", weather_desc)
#     print("current hunidity     :", hmdt, "%")
#     print("Current wind speed   :", wind_spd, "kmph")

