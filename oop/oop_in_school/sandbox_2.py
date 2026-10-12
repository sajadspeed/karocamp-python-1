class Person:
    def __init__(self, name: str, age: int, woman: bool = True):
        self.name = name
        self.age = age
        self.woman = woman

    def learn(self):
        print("I'm learning how to live.")

    def eat(self):
        print("I'm eating some food.")

    def walk(self):
        print("I'm walking.")

    def sleep(self):
        print("ZZZ")

    def show(self):
        print(f"I'm {self.name} and I am {self.age} years old.")


danial_obj = Person("Danial", 23, False)

danial_obj.show()
danial_obj.eat()

roya_obj = Person("Roya", 25)

roya_obj.show()
