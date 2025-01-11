import requests
import os
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()

def get_base_url():
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("آدرس پنل تنظیم نشده است! از دستور /set_panel استفاده کنید.")
    return base_url

def get_token(username, password):
    url = f"{get_base_url()}/api/admins/token"
    data = {"username": username, "password": password}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("access_token")
    return None

def get_all_admins(token, page_size=100):
    url = f"{get_base_url()}/api/admins"
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
    url = f"{get_base_url()}/api/users"
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
