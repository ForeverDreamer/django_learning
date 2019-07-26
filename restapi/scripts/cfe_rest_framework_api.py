import json
import requests
import os


ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = os.path.join(os.getcwd(), "logo.jpg")


# def do(method='get', data={}, id=1, is_json=True):
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT + "?id=" + str(id), data=data)
#     print(r.text)
#     return r

def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers["content-type"] = "application/json"
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {'image': image}
            r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)

    print(r.status_code)
    print(r.text)
    return r


# do_img(method='post', data={'user': 1, 'content': ''}, is_json=False, img_path=image_path)
do_img(method='put', data={'id': 9, 'user': 1, 'content': 'Some new content'}, is_json=False, img_path=image_path)


# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers["content-type"] = "application/json"
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.status_code)
#     print(r.text)
#     return r


# do(method='post', data={'user': 1, 'content': "Create content"})
# do(data={'id': 2})
# do(method='put', data={'id': 4, 'user': 1, 'content': "Some cool new content"})
# do(method='delete', data={'id': 5})


