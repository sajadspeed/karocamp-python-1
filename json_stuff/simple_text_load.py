from functions import clear_string


with open("data_test.txt") as f:
    for line in f:

        grade = {
            "name": None,
            "score": None,
            "absent": None
        }

        line = clear_string(line)

        line_list = line.split(sep=",")

        grade["name"] = line_list[0]
        grade["score"] = line_list[1]
        grade["absent"] = line_list[2]

        print("--------------------")
        print(f"Name: {grade["name"]}")
        print(f"Score: {grade["score"]}")
        print(f"Gheybaaat: {grade["absent"]}")