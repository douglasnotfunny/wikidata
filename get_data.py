import requests
import json

from save_data import DBAccess

QUERY = """
    SELECT DISTINCT ?film ?filmLabel ?imdbid ?date WHERE {
    ?film wdt:P31 wd:Q11424.
    ?film wdt:P345 ?imdbid.
    ?film wdt:P577 ?date.
    FILTER(YEAR(?date) > 2013).
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    } GROUP BY ?film ?filmLabel ?imdbid ?date
    """

URL = "https://query.wikidata.org/sparql"

PARAMS = {
    "format": "json",
    "query": QUERY
}

def get_movies():
    response = requests.post(URL, data=PARAMS)
    data = json.loads(response.text)
    return data["results"]["bindings"]

def create_table():
    db = DBAccess()
    mydb = None
    try:
        mydb = db.create()
    except Exception:
        return None
    return mydb

def save(val):
    db = DBAccess()
    mydb = None
    try:
        mydb = db.save(val)
    except Exception:
        return None
    return mydb

def mount_tuple(movie):
    imdb_id = movie['imdbid']['value']
    title = movie['filmLabel']['value']
    uri = movie['film']['value']
    year = movie['date']['value'].split('-')[0]
    
    return (title, imdb_id, uri, year)

def insert():
    data = get_movies()
    mydb = create_table()
    
    if not mydb:
        raise Exception("Error to connection")
    
    for movie in data:
        val = mount_tuple(movie)
        if not save(val):
            raise Exception("Erro to save data")

if __name__ == '__main__':
    insert()
