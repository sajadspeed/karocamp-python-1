import os
from settings import user_login_path


def show_grades(grades):
    """ This fucntion get your grades and print them. """
    print("----- Grades -----")

    if len(grades) > 0:
        for grade in grades:
            print(grade)
    else:
        print("No grades available")

def get_grades():
    """
    This function get grades from input and return them in list. By.
    """
    grades_from_input = []

    while True:
        grade = float(input("Enter grade (-1 to finish): "))

        if grade < 0:
            break

        if grade > 20:
            print("! Grade must be between 0 to 20.")
            continue

        grades_from_input.append(grade)

    return grades_from_input

def show_info(
        first_name, 
        last_name="Folan Famil", 
        student_id=None, 
        average=None, 
        status=None, 
        highest_grade=None, 
        lowest_grade=None
    ):
    # Print student report
    show_separator("Student Report")
    if first_name is not None or last_name is not None:
        print(f"Name: {first_name} {last_name}")

    if student_id is not None:
        print(f"Student ID: {student_id}")

    if average is not None:
        print(f"Average: {average:.2f}")

    if status is not None:
        print(f"Status: {status}")
    
    if highest_grade is not None:
        print(f"Highest Grade: {highest_grade}")
    
    if lowest_grade is not None:
        print(f"Lowest Grade: {lowest_grade}")

def show_separator(title=""):
    print(f"\n-----------{title}-----------\n")

def is_login(username, password):
    username_org = None
    password_org = None
    
    with open(user_login_path) as file:
        username_org = clear_string(file.readline())
        password_org = clear_string(file.readline())

    print("LOG", username_org, password_org)

    if username == username_org and password == password_org:
        return True
    else:
        return False

def clear_cmd():
    os.system("cls")

def clear_string(string: str) -> str:
    """
    Clear \\n and witespace from string and return cleared string.
    """
    return string.replace("\n", "")