from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int, fuel_capacity: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        
        self._fuel_level = fuel_capacity
        self._is_engine_on = False

    @abstractmethod
    def start_engine(self) -> None:
        pass

    def get_fuel_level(self) -> float:
        return self._fuel_level

    def refuel(self, amount: float) -> None:
        if amount <= 0:
            print("Refuel amount must be greater than zero.")
            return
        
        self._fuel_level += amount
        if self._fuel_level > self.fuel_capacity:
            self._fuel_level = self.fuel_capacity
        print(f"Refueled {self.brand} {self.model}. Current fuel level: {self._fuel_level:.2f}L.")

    def drive(self, distance: float) -> None:
        if not self._is_engine_on:
            print(f"Please start the engine of {self.brand} {self.model} first!")
            return
        
        consumed = distance * 0.08
        if self._fuel_level >= consumed:
            self._fuel_level -= consumed
            print(f"{self.brand} {self.model} drove {distance} km.")
        else:
            print(f"Not enough fuel for {self.brand} {self.model}! Please refuel.")
            self._is_engine_on = False


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, fuel_capacity: float, doors_count: int):
        super().__init__(brand, model, year, fuel_capacity)
        self.doors_count = doors_count

    def start_engine(self) -> None:
        if self._fuel_level > 0:
            self._is_engine_on = True
            print(f"Car {self.brand} {self.model} started with push button.")
        else:
            print(f"Cannot start {self.brand} {self.model}: fuel tank is empty.")


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, fuel_capacity: float, has_abs: bool):
        super().__init__(brand, model, year, fuel_capacity)
        self.has_abs = has_abs

    def start_engine(self) -> None:
        if self._fuel_level > 0:
            self._is_engine_on = True
            print(f"Motorcycle {self.brand} {self.model} started with kick/electric start.")
        else:
            print(f"Cannot start {self.brand} {self.model}: fuel tank is empty.")
