import http.client
import json

class NoPoster(Exception):
    pass


def get_json(source):
    conn = http.client.HTTPSConnection("www.omdbapi.com")
    conn.request("GET", source)
    res = conn.getresponse()
    json_data = res.read().decode("utf-8")
    json_data = json.loads(json_data)
    return json_data

def get_poster(movie):
    try:
        json_data = get_json("/?t={}&apikey=1fd32d15".format("".join(e for e in movie if e.isalnum() or e == " ").replace(" ", "+").lower()))
    except:
        raise NoPoster
    return json_data["Poster"]
