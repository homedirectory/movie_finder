import http.client
import json


def get_json(source):
    conn = http.client.HTTPSConnection("www.omdbapi.com")
    conn.request("GET", source)
    res = conn.getresponse()
    json_data = res.read().decode("utf-8")
    json_data = json.loads(json_data)
    return json_data

key = "1fd32d15"
json_data = get_json("/?y=2010&page=3&apikey={}".format(key))
json_data = json.dumps(json_data, indent=2)
print(json_data)