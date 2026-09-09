# ============================================================
# main.py
# ============================================================

import commands


while True:
    print()
    print("===== User Manager =====")
    print("1. Register")
    print("2. Show Users")
    print("3. Search User")
    print("4. Update Profile")
    print("5. Add Skill")
    print("6. Verify User")
    print("7. Delete User")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        commands.register()

    elif choice == "2":
        commands.show_users()

    elif choice == "3":
        commands.search_user()

    elif choice == "4":
        commands.update_profile()

    elif choice == "5":
        commands.add_skill()

    elif choice == "6":
        commands.verify_user()

    elif choice == "7":
        commands.delete_user()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
