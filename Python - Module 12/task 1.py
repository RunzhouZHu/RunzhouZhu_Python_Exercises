import requests


# https://api.chucknorris.io/jokes/random
request = "https://api.chucknorris.io/jokes/random"
respones = requests.get(request).json()
print(respones["value"])


