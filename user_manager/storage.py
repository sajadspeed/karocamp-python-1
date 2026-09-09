# ============================================================
# storage.py
# ============================================================

import json


FILE_NAME = "users.json"


def load_users():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)
