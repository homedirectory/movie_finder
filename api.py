import http.client
import json


def get_json(source):
    conn = http.client.HTTPSConnection("www.omdbapi.com")
    conn.request("GET", source)
    res = conn.getresponse()
    json_data = res.read().decode("utf-8")
    json_data = json.loads(json_data)
    return json_data


json_data = get_json("/?i=tt3896198&apikey=1fd32d15")
json_data = json.dumps(json_data, indent=2)
print(json_data)
