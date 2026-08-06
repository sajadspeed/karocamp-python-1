def show_grades(grades):
    print("----- Grades -----")

    if len(grades) > 0:
        for grade in grades:
            print(grade)
    else:
        print("No grades available")


def get_grades():
    grades_from_input = []

    while True:
        grade = float(input("Enter grade (-1 to finish): "))

        if grade < 0:
            break

        if grade > 20:
            print("! Grade must be between 0 to 20.")
            continue

        grades_from_input.append(grade)


        total += grade
        count += 1

        if highest_grade is None or grade > highest_grade:
            highest_grade = grade

        if lowest_grade is None or grade < lowest_grade:
            lowest_grade = grade

    return grades_from_input


first_name = None
last_name = None
student_id = None


total = 0
count = 0
highest_grade = None
lowest_grade = None

grades = []

while True:
    print("\n------------ UN Managment ------------")
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

        # Print student report
        print("\n----- Student Report -----")
        print(f"Name: {first_name} {last_name}")
        print(f"Student ID: {student_id}")
        print(f"Average: {average:.2f}")
        print(f"Status: {status}")
        print(f"Highest Grade: {highest_grade}")
        print(f"Lowest Grade: {lowest_grade}")

    # Show grades
    elif choice == "4":
        show_grades(grades)

    # Remove grade
    elif choice == "5":

        show_grades(grades)

        print("------------------")

        grade = int( input("Enter your grade for remove: ") )
        grades.remove(grade)

        print("------------------")

        show_grades(grades)

    # Exit
    elif choice == "0":
        print("Good bye my friend.")
        break

    else:
        print("Wrong command.")
