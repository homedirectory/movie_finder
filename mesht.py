import http.client
import json


def get_json(source):
    key = "1fd32d15"
    conn = http.client.HTTPSConnection("http://www.omdbapi.com/?i=tt3896198&apikey={}".format(key))
    conn.request("GET", source)
    res = conn.getresponse()
    json_data = res.read().decode("utf-8")
    json_data = json.loads(json_data)
    return json_data