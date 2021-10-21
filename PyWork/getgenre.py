import sys,os
import splunk.Intersplunk
import json
import request as req

def tmdb_api_call(requestURL,parameters):
    response=req.get(url=requestURL,params=parameters)
    if response.status_code != 200:
	print('Status:',response.status_code,'Headers: ',response.headers,'Error Response: ',response.json())
	exit()
    data=response.json()
    return json.dumps(data)

def get_genre_dtl():
    genres = []
    api_key = '16e162e1928380c1e7e0eaa269d6782f'
    requestURL = "https://api.themoviedb.org/3/genre/movie/list"
    parameter = {"api_key": api_key}
    genre_list = tmdb_api_call(requestURL,parameter)
    data = json.loads(genre_list)
    for genre in data["genres"]:
	genres.append(genre)
    return genres

genres = get_genre_dtl()
splunk.Intersplunk.outputResults(genres)

		
