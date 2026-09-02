import json

LETTERS = ["A", "B", "C", "D"]

correct_answers = 0
wrong_answers = 0

with open("data.json", "r") as file:
    data = json.load(file)
    questions = data["questions"]

counter = 1

for question in questions:
    print(f"{counter}. {question["question"]}")

    counter_option = 0
    # Print options
    for option in question["options"]:
        print(f"{LETTERS[counter_option]}) {option}")
        counter_option += 1

    answer = input("enter your answer: ")

    # Correct answer
    if answer.upper().strip() == question["answer"].upper().strip():
        print("✅ BarikAllah")
        correct_answers += 1
    else:
        print("👎 Niaz be talash bishtar")
        wrong_answers += 1

    print("\n---------------------------\n")
    counter += 1


print("\n======================================\n")
print("Correct answer:", correct_answers)
print("Wrong answer:", wrong_answers)
