#!/usr/bin/env python3
import requests

def get_all_users(base_url: str) -> list[dict]:
    response = requests.get(base_url).json().get("results", None)
    if response is None:
        print("Could not get users. Is the backend running?")
        exit()

    return response

def reset_single_chore(base_url: str, user_dict: dict):
    PATCH_DATA = {'done': False, 'done_date': None}
    response = requests.patch(f"{base_url}/{user_dict['id']}/", PATCH_DATA).text

    return response

if __name__ == "__main__":
    BASE_URL = "http://localhost:8000/piglify/users"
    users = get_all_users(BASE_URL)

    for user in users:
        reset_single_chore(BASE_URL, user)
    
    print("Reset all chores.")
