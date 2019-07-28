import os
import json
import requests


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
IMAGE_PATH = os.path.join(os.getcwd(), "logo.jpg")


def without_token():
    get_endpoit = ENDPOINT + str(2)
    post_data = json.dumps({'content': "Some random content"})

    r = requests.get(get_endpoit)
    print(r.text)

    r2 = requests.get(ENDPOINT)
    print(r.status_code)

    post_headers = {
        'content-type': 'application/json'
    }

    post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
    print(post_response.text)


# without_token()


def get_token():
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        'username': 'admin',
        'password': 'password123'
    }
    r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
    token = r.json()['token']
    print(r.json())
    return token


get_token()


def refresh_token():
    headers = {
        "content-type": "application/json"
    }
    data = {
        'username': 'admin',
        'password': 'password123'
    }
    r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
    token = r.json()['token']

    refresh_data = {
        'token': token
    }
    new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
    new_token = new_response.json()
    print(new_token)


# refresh_token()


def create_status():
    headers = {
        # "Content-Type": "application/json",
        "Authorization": "JWT" + ' ' + get_token(),
    }

    with open(IMAGE_PATH, 'rb') as image:
        file_data = {
            'image': image
        }
        post_data = {'content': "Some random content"}
        print(headers)
        post_response = requests.post(ENDPOINT, data=post_data, headers=headers, files=file_data)
        print(post_response.text)


# create_status()
