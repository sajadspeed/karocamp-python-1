from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

    def show_info(self):
        print(f"{self.name} - salary: {self._salary}")

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        return "Writing and maintaining software."


class Designer(Employee):
    def work(self):
        return "Designing user interfaces."


class Manager(Employee):
    def work(self):
        return "Planning work and coordinating the team."
