# ============================================================
# commands.py
# ============================================================

import user_manager


def show_user(user):
    print("--------------------")
    print(f"Username: {user['username']}")
    print(f"Password: {user['password']}")

    if user["is_verified"]:
        print("Verified: 🍓")
    else:
        print("Verified: 🥕")

    print("Skills:")

    if len(user["skills"]) == 0:
        print("No skills")
    else:
        for skill in user["skills"]:
            print(f"- {skill}")

    print("Profile:")
    print(f"Name: {user['profile']['name']}")
    print(f"Age: {user['profile']['age']}")
    print(f"City: {user['profile']['city']}")


def register():
    print("\n===== Register =====")

    username = input("Username: ")
    password = input("Password: ")
    name = input("Name: ")
    age = int(input("Age: "))
    city = input("City: ")

    skills_input = input("Skills (separate with comma): ")

    skills = []

    if skills_input:
        skills = skills_input.split(",")

        for i in range(len(skills)):
            skills[i] = skills[i].strip()

    verified_input = input("Is user verified? (y/n): ")

    is_verified = False

    if verified_input == "y":
        is_verified = True

    result = user_manager.register_user(
        username,
        password,
        name,
        age,
        city,
        skills,
        is_verified
    )

    if result:
        print("User registered successfully.")
    else:
        print("This username already exists.")


def show_users():
    print("\n===== Users =====")

    users = user_manager.get_users()

    if len(users) == 0:
        print("No users found.")
        return

    for user in users:
        show_user(user)

    print("--------------------")


def search_user():
    print("\n===== Search User =====")

    username = input("Username: ")

    user = user_manager.find_user(username)

    if user is None:
        print("User not found.")
        return

    print("\nUser found:")
    show_user(user)


def update_profile():
    print("\n===== Update Profile =====")

    username = input("Username: ")

    user = user_manager.find_user(username)

    if user is None:
        print("User not found.")
        return

    name = input("New name: ")
    age = int(input("New age: "))
    city = input("New city: ")

    user_manager.update_profile(
        username,
        name,
        age,
        city
    )

    print("Profile updated successfully.")


def add_skill():
    print("\n===== Add Skill =====")

    username = input("Username: ")

    user = user_manager.find_user(username)

    if user is None:
        print("User not found.")
        return

    skill = input("Skill: ")

    user_manager.add_skill(username, skill)

    print("Skill added successfully.")


def verify_user():
    print("\n===== Verify User =====")

    username = input("Username: ")

    result = user_manager.change_verification(username)

    if result:
        print("User verification status changed.")
    else:
        print("User not found.")


def delete_user():
    print("\n===== Delete User =====")

    username = input("Username: ")

    user = user_manager.find_user(username)

    if user is None:
        print("User not found.")
        return

    confirm = input("Are you sure? (y/n): ")

    if confirm != "y":
        print("Delete cancelled.")
        return

    user_manager.delete_user(username)

    print("User deleted successfully.")
