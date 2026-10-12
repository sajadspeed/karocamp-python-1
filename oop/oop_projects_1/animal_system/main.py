from models import Animal, Cat, Eagle

my_cat = Cat(name="Luna", age=3, favorite_toy="Feather Wand")
my_eagle = Eagle(name="Sky", age=5, wingspan_meters=2.1)

animals = [my_cat, my_eagle]
print("=== Wildlife Observation ===")
for animal in animals:
    print(f"\n--- Observing: {animal.name} ---")
    animal.make_sound()
    animal.move()
    animal.feed(20)
    print(f"Hunger Status: {animal.get_hunger_level()}%")
