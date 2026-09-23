# ============================================================
# user_manager.py
# ============================================================

from storage import load_users, save_users


users = load_users()


def find_user(username):
    for user in users:
        if user["username"] == username:
            return user

    return None


def register_user(username, password, name, age, city, skills, is_verified):
    if find_user(username) is not None:
        return False

    user = {
        "username": username,
        "password": password,
        "is_verified": is_verified,
        "skills": skills,
        "profile": {
            "name": name,
            "age": age,
            "city": city
        }
    }

    users.append(user)
    save_users(users)

    return True


def get_users():
    return users


def update_profile(username, name, age, city):
    user = find_user(username)

    if user is None:
        return False

    user["profile"]["name"] = name
    user["profile"]["age"] = age
    user["profile"]["city"] = city

    save_users(users)

    return True


def add_skill(username, skill):
    user = find_user(username)

    if user is None:
        return False

    user["skills"].append(skill)

    save_users(users)

    return True


def change_verification(username):
    user = find_user(username)

    if user is None:
        return False

    user["is_verified"] = not user["is_verified"]

    save_users(users)

    return True


def delete_user(username):
    user = find_user(username)

    if user is None:
        return False

    users.remove(user)
    save_users(users)

    return True
