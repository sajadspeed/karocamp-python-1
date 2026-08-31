from functions import attempts_to_score
import random

max_range = 50
difficulty = "Easy"

print("1. Easy 1-50")
print("2. Normal 1-100")
print("3. Hard 1-1000")
print("4. IRAN MODE 1-100000")
difficulty_choice = input("Choose your difficulty: ")

if difficulty_choice == "1":
    max_range = 50
    difficulty = "Easy"
elif difficulty_choice == "2":
    max_range = 100
    difficulty = "Normal"
elif difficulty_choice == "3":
    max_range = 1000
    difficulty = "Hard"
elif difficulty_choice == "4":
    max_range = 100000
    difficulty = "IRAN MODE"

computer_number = random.randint(1, max_range)

print(f"Guess my number between 1 to {max_range}.")

attempts = 0

while True:
    guess = int(input("Your guess? "))
    attempts += 1

    if guess == computer_number:
        print("🎉🎉🎉 YOU WIN. 🎉🎉🎉")
        break
    elif guess > computer_number:
        print("Too High.")
    else:
        print("Too Low.")

    if attempts_to_score(attempts) <= 0:
        print("😢 You Lose 😢")
        print(f" 😒   The number is {computer_number}. You are such a loser.   😒 ")
        break


print("------ Your Stats ------")
print("Your difficulty:", difficulty)
print("Attempts:", attempts)
print("Score:", attempts_to_score(attempts))