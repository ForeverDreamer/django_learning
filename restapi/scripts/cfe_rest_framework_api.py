import json
import requests


ENDPOINT = "http://127.0.0.1:8000/api/status/"


# def do(method='get', data={}, id=1, is_json=True):
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT + "?id=" + str(id), data=data)
#     print(r.text)
#     return r

def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers["content-type"] = "application/json"
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.status_code)
    print(r.text)
    return r


do(method='post', data={'user': 1, 'content': "Create content"})
# do(data={'id': 2})
# do(method='put', data={'id': 4, 'user': 1, 'content': "Some cool new content"})
# do(method='delete', data={'id': 5})


