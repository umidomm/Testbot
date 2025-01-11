import requests

BASE_URL = "https://console.hopn.ir"
TOKEN_ENDPOINT = "/api/admins/token"
ADMINS_ENDPOINT = "/api/admins"
USERS_ENDPOINT = "/api/users"

def get_token(username, password):
    url = f"{BASE_URL}{TOKEN_ENDPOINT}"
    data = {"username": username, "password": password}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("access_token")
    return None

def get_all_admins(token, page_size=100):
    url = f"{BASE_URL}{ADMINS_ENDPOINT}"
    headers = {"Authorization": f"Bearer {token}"}
    all_admins = []
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={"page": page, "size": page_size})
        if response.status_code == 200:
            admins = response.json().get("items", [])
            all_admins.extend(admins)
            if len(admins) < page_size:
                break
            page += 1
        else:
            break
    return all_admins

def get_all_users(token, page_size=100):
    url = f"{BASE_URL}{USERS_ENDPOINT}"
    headers = {"Authorization": f"Bearer {token}"}
    all_users = []
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={"page": page, "size": page_size})
        if response.status_code == 200:
            users = response.json().get("items", [])
            all_users.extend(users)
            if len(users) < page_size:
                break
            page += 1
        else:
            break
    return all_users
