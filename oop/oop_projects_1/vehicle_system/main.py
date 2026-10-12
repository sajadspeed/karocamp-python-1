from models import Car, Motorcycle, Vehicle


my_car = Car(brand="Toyota", model="Corolla", year=2022, fuel_capacity=50.0, doors_count=4)
my_bike = Motorcycle(brand="Honda", model="CB250", year=2021, fuel_capacity=14.0, has_abs=True)

city = [my_car, my_bike]
for v in city:
    print(f"\nTesting: {v.brand} {v.model} ({v.year})")
    v.start_engine()
    v.drive(50)
    print(f"Remaining Fuel: {v.get_fuel_level():.2f}L")
