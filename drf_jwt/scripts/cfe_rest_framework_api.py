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


# get_token()


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


def auth():
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "JWT" + ' ' + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY0MzEwMzI4LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NjQzMTAwMjh9.TI4Xa-csIUVPZwwXd7r6IjHXtdo2LpKpFWTZzpT1lmM",
    }
    data = {
        'username': 'admin@example.com',
        'password': 'password123'
    }
    r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
    print(r.json())


# auth()


def register():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "JWT" + ' ' + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcm5hbWUiOiJjZmU4IiwiZXhwIjoxNTY0MzcxMjY4LCJlbWFpbCI6ImNmZThAMTYzLmNvbSIsIm9yaWdfaWF0IjoxNTY0MzcwOTY4fQ.9_VKbpqR0TAN5_RGZEGIGv-yvdxRFOEo8toC7Omx4yE"
    }
    data = {
        'username': 'cfe8',
        'email': 'cfe8@163.com',
        'password': 'password123',
        'password2': 'password123',
    }
    r = requests.post(AUTH_ENDPOINT + "register/", data=json.dumps(data), headers=headers)
    print(r.json())


register()
