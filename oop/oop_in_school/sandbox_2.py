class Person:
    def __init__(self, name: str, age: int, woman: bool = True):
        self.name = name
        self.age = age
        self.woman = woman
        self.health = 100

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

    def physical_hit(self, damage: int):
        self.health -= damage

    def emotional_hit(self, damage: int):
        self.health -= damage * 1.2


class Dancer(Person):
    def __init__(self, name, age, woman=True, group_name="No Group"):
        super().__init__(name, age, woman)
        self.group_name = group_name

    def learn(self):
        super().learn()
        print("I'm learning how to dance.")

    def emotional_hit(self, damage):
        super().emotional_hit(damage)
        self.health -= damage * 0.8


danial_obj = Dancer(name="Danial", age=23, woman=False, group_name="25 Band")
sajad_obj = Person("Sajad", 18, False)

print(danial_obj.name)
print(danial_obj.health)
danial_obj.physical_hit(20)
danial_obj.emotional_hit(15)
print(danial_obj.health)


print(sajad_obj.name)
print(sajad_obj.health)
sajad_obj.physical_hit(20)
sajad_obj.emotional_hit(15)
print(sajad_obj.health)
