from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int, hunger_level: int = 50):
        self.name = name
        self.age = age
        
        self._hunger_level = max(0, min(100, hunger_level))

    @abstractmethod
    def make_sound(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass

    def get_hunger_level(self) -> int:
        return self._hunger_level

    def feed(self, food_amount: int) -> None:
        self._hunger_level = max(0, self._hunger_level - food_amount)
        print(f"Fed {self.name}. Hunger level decreased to {self._hunger_level}%.")


class Cat(Animal):
    def __init__(self, name: str, age: int, favorite_toy: str):
        super().__init__(name, age)
        self.favorite_toy = favorite_toy

    def make_sound(self) -> None:
        print(f"Cat {self.name} purrs and meows: 'Meow! Purr...'")

    def move(self) -> None:
        print(f"Cat {self.name} gracefully jumps and walks silently across the room.")

    def scratch_post(self) -> None:
        print(f"Cat {self.name} is scratching its post using {self.favorite_toy}.")


class Eagle(Animal):
    def __init__(self, name: str, age: int, wingspan_meters: float):
        super().__init__(name, age)
        self.wingspan_meters = wingspan_meters

    def make_sound(self) -> None:
        print(f"Eagle {self.name} screeches sharply from high above!")

    def move(self) -> None:
        print(f"Eagle {self.name} soars gracefully through the sky with its {self.wingspan_meters}m wingspan.")

    def hunt(self) -> None:
        print(f"Eagle {self.name} dives down swiftly to catch prey.")
