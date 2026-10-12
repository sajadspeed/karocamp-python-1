from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name: str, age: int, energy: int = 100):
        self.name = name
        self.age = age
        
        self._energy = max(0, min(100, energy))

    @abstractmethod
    def speak(self) -> None:
        pass

    @abstractmethod
    def perform_duty(self) -> None:
        pass

    def get_energy(self) -> int:
        return self._energy

    def rest(self, hours: int) -> None:
        gained = hours * 15
        self._energy = min(100, self._energy + gained)
        print(f"Human {self.name} rested for {hours} hours. Energy restored to {self._energy}%.")


class SoftwareEngineer(Human):
    def __init__(self, name: str, age: int, programming_language: str):
        super().__init__(name, age)
        self.programming_language = programming_language

    def speak(self) -> None:
        print(f"Software Engineer {self.name} says: 'Hello! I am coding in {self.programming_language}.'")

    def perform_duty(self) -> None:
        if self._energy >= 25:
            self._energy -= 25
            print(f"Software Engineer {self.name} successfully fixed bugs and wrote unit tests. Energy left: {self._energy}%.")
        else:
            print(f"Software Engineer {self.name} is too tired to code! Needs coffee and rest.")


class Doctor(Human):
    def __init__(self, name: str, age: int, specialization: str):
        super().__init__(name, age)
        self.specialization = specialization

    def speak(self) -> None:
        print(f"Doctor {self.name} ({self.specialization}) says: 'Take care of your health and stay safe!'")

    def perform_duty(self) -> None:
        if self._energy >= 30:
            self._energy -= 30
            print(f"Doctor {self.name} examined patients at the hospital. Energy left: {self._energy}%.")
        else:
            print(f"Doctor {self.name} is exhausted from long shifts! Needs rest.")
