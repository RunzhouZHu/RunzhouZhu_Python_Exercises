import requests


# https://openweathermap.org/api
request = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=75d2735cb3fbcc1bf21a88ba28aff09c"
response = requests.get(request).json()

print(response)