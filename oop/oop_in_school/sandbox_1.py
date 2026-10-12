class Car:
    def __init__(self, color, engine, model):
        self.color = color
        self.engine = engine
        self.model = model


my_car_1 = Car("red alb", "electric", "sedan")
my_car_2 = Car("blue", "electric", "sedan")
my_car_3 = Car("yellow", "disel", "pickup")

print(my_car_1)
print(type(my_car_1))
