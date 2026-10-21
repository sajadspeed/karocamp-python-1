class NimisarfedError(Exception):
    """
    This a Esfahani Error. Do not user outside this city.
    """

    def __init__(self, message="Nimisarfed inkar. Vakhy amoo."):
        self.message = message
        super().__init__(self.message)


def calc(number1, number2, oprator):
    """
    Esfahani calc
    """
    if number1 > 10 or number2 > 10:
        raise NimisarfedError()

    if oprator == "+":
        return number1 + number2
    elif oprator == "-":
        return number1 - number2
    elif oprator == "*":
        return number1 * number2
    elif oprator == "/":
        return number1 / number2
    else:
        raise Exception("Oprator is wrong.")


zero_division_attempts = 3

while True:
    try:
        number1 = int(input("Number1: "))
        oprator = input("Oprator: ")
        number2 = int(input("Number2: "))

        result = calc(number1, number2, oprator)
        print(result)
        break
    except NimisarfedError as e:
        print(e)
        break
    except ZeroDivisionError as e:
        zero_division_attempts -= 1
        print("Remain attempts:", zero_division_attempts)
        if zero_division_attempts <= 0:
            break
    except ValueError as e:
        print("Asisam eshtebah addad vard kardi bishtar deghat kon.")
    except Exception as e:
        print(e)
