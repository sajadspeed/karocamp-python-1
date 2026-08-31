import random

choices = ["rock", "paper", "scissors"]

while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    computer_choice = random.choice(choices)

    user_number_choice = int(input("Your choice: "))
    user_choice = choices[user_number_choice-1]


    # computer_choice and user_choice is a clean variables from choices list

    
