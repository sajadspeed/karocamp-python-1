try:
    with open("Chert.txt") as file:
        file.read()
except FileNotFoundError:
    with open("Chert.txt", "w") as file:
        file.write("Chert and Pert")


def signup(username, name, password):
    if len(username) < 8:
        raise Exception("Username is too short.")
    if len(name) < 3:
        raise Exception("Name is too short.")
    if len(password) < 12:
        raise Exception("Password is too short.")

    # Singup...
    return True


while True:
    try:
        username = input("Username: ")
        name = input("Name: ")
        password = input("Password: ")
        result = signup(username, name, password)
        break
    except Exception as e:
        print(e)
