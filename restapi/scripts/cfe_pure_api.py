import json
import requests  # http requests

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list(id=None):  # --> Lists all this out
    data = json.dumps({})
    if id is not None:
        data = json.dumps({"id": id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200: # not found
        print('probably not good sign?')
    data = r.json()
    return data


# print(get_list())


def create_update():
    new_data = {
        'user': 1,
        "content": "Another new cool content"
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


# print(create_update())


def delete_update():
    r = requests.delete(BASE_URL + ENDPOINT)
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


print(delete_update())
