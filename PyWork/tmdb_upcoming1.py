import json
import requests
api_key = "16e162e1928380c1e7e0eaa269d6782f"
page_number = 1
parameters = {"api_key": api_key, "page": page_number}
response = requests.get('https://api.themoviedb.org/3/movie/upcoming',parameters)
data = response.json()
print(json.dumps(data["results"]))