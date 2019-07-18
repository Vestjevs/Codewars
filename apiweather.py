import requests
import json

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Input city: ")
units = input("Input your metric: ")

params = {
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': units
}

res = requests.get(api_url, params)

data = res.json()

with open("data.json", "w") as f:
    json.dump(data, f, indent=8)

print('Current temperature in {} is {}'.format(city, data["main"]["temp"]))
