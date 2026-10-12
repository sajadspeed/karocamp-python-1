from abc import ABC, abstractmethod

class Delivery(ABC):
    def __init__(self, destination):
        self.destination = destination
        self._status = "waiting"

    def get_status(self):
        return self._status

    def start(self):
        if self._status == "waiting":
            self._status = "in progress"
            return True
        return False

    @abstractmethod
    def calculate_time(self):
        pass


class BikeDelivery(Delivery):
    def calculate_time(self):
        return 40

    def start(self):
        super().start()
        print(f"Bike delivery started to {self.destination}.")


class CarDelivery(Delivery):
    def calculate_time(self):
        return 20

    def start(self):
        super().start()
        print(f"Car delivery started to {self.destination}.")
