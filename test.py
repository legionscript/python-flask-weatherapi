import requests
import json

city = "Indianapolis"
country = "US"

api_key = "###"

weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

weather_data = weather_url.json()
