import random

choices = ["rock", "paper", "scissors"]

while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    computer_choice = random.choice(choices)

    user_number_choice = int(input("Your choice: "))
    user_choice = choices[user_number_choice - 1]

    # computer_choice and user_choice is a clean variables from choices list

    if user_choice == computer_choice:
        print("Draw!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose.")
