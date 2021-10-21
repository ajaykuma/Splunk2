#to implement checkpointing

import json
import requests
import os

api_key = "16e162e1928380c1e7e0eaa269d6782f"
page_number = 1
checkpoint_file = os.path.join(os.environ["SPLUNK_HOME"],'etc','apps','tmdb_new1','bin','checkpoint','checkpoint.txt')
parameters = {"api_key": api_key, "page": page_number}
response = requests.get('https://api.themoviedb.org/3/movie/upcoming',parameters)
data = response.json()

#print(json.dumps(data["results"]))

def checkpoint(checkpoint_file,movie_id):
	with open(checkpoint_file,'r') as file:
		id_list = file.read().splitlines()
		return (movie_id in id_list)

def write_to_checkpoint_file(checkpoint_file,movie_id):
	with open(checkpoint_file,'a') as file:
		file.writelines(movie_id + "\n")

def stream_to_splunk(checkpoint_file,data):
	for dt in data:
		if checkpoint(checkpoint_file,str(dt["id"])):
			continue
		else:
			write_to_checkpoint_file(checkpoint_file,str(dt["id"]))
			print(json.dumps(dt))

stream_to_splunk(checkpoint_file,data["results"])