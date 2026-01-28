import requests


BASE_URL = "http://localhost:8000"


def register_user(username, first_name, last_name, password):
    url = f"{BASE_URL}/user/"
    payload = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "password": password
    }
    response = requests.post(url, json=payload)
    return response


def get_jwt_token(username, password):
    url = f"{BASE_URL}/auth/token"
    form_data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=form_data)
    return response.json().get("jwt")


def get_all_users(token):
    url = f"{BASE_URL}/user/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()


