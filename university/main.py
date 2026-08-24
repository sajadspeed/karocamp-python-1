import os
from functions import get_grades, show_grades, show_info, show_separator, is_login, clear_cmd, clear_string
from settings import user_login_path, user_info_path

### Signup

if os.path.exists(user_login_path) == False:
    show_separator("Sign up")
    print("Enter your username and password for signup my dear.")

    username = input("Username: ")
    password = input("Password: ")

    with open(user_login_path, "w") as f:
        f.write(username + "\n")
        f.write(password + "\n")
        print("Your signup successful.")
    
    clear_cmd()


###

### LOGIN

show_separator("Login to my app")
username = input("Username: ")
password = input("Password: ")

if is_login(username, password) == False:
    print("To chizi le migi nisti. You are a lier. Go and fix your life.")
    quit()

clear_cmd()

###

first_name = None
last_name = None
student_id = None


total = 0
count = 0
highest_grade = None
lowest_grade = None

grades = []


### Load data. Load data from files.
if os.path.exists(user_info_path):
    with open(user_info_path, "r") as f:
        first_name = clear_string(f.readline())
        last_name  = clear_string(f.readline())
        student_id = clear_string(f.readline())
###


while True:
    show_separator("UN Managment")

    print("1. Insert Student Info")
    print("2. Insert Grades")
    print("3. Show Student Report")
    print("4. Show Grades")
    print("5. Remove grade")

    print("0. Exit")

    choice = input()


    # Insert Student Info
    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        student_id = input("Enter student ID: ")

        with open(user_info_path, "w") as f:
            f.write(first_name + "\n")
            f.write(last_name + "\n")
            f.write(student_id + "\n")

        print("Your info is seved!")

    # Insert grades
    elif choice == "2":
        grades = get_grades()

    # Show info
    elif choice == "3":
        average = 0
        if count > 0:
            average = total / count

        # Determine status
        if 17 <= average <= 20:
            status = "Excellent"
        elif 15 <= average < 17:
            status = "Good"
        elif 12 <= average < 15:
            status = "Average"
        else:
            status = "Failed"

        # show_info(first_name, last_name, student_id, average, status, highest_grade, lowest_grade)first_name, last_name, student_id, average, status, highest_grade, lowest_grade
        show_info(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            average=average,
            status=status,
            highest_grade=highest_grade,
            lowest_grade=lowest_grade
        )

    # Show grades
    elif choice == "4":
        show_grades(grades)

    # Remove grade
    elif choice == "5":

        show_grades(grades)

        show_separator()

        grade = int( input("Enter your grade for remove: ") )
        grades.remove(grade)

        show_separator()

        show_grades(grades)

    # Exit
    elif choice == "0":
        print("Good bye my friend.")
        break

    else:
        print("Wrong command.")
