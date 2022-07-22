import requests

API_KEY = "207aa44bccceada5026035fbc69941e4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 2)

    print("Weather: " + weather)
    print("Temperature:", temp)
else:
    print("an error has occurred")



# how data is formated, it's a dictionary so access it through []
# {'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 292.86, 'feels_like': 292.61, 'temp_min': 290.53, 'temp_max': 295.13, 'pressure': 1019, 'humidity': 66}, 'visibility': 10000, 
# 'wind': {'speed': 7.2, 'deg': 90}, 'rain': {'1h': 0.19}, 'clouds': {'all': 20}, 'dt': 1658495492, 'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1658462970, 'sunset': 1658520242}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}