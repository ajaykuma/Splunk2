import json
import requests
api_key = "16e162e1928380c1e7e0eaa269d6782f"
page_number = range(0,13)
for i in page_number:
	parameters = {"api_key": api_key, "page_number": i}
	response = requests.get('https://api.themoviedb.org/3/movie/upcoming',parameters)
	data = response.json()
	print(json.dumps(data["results"]))