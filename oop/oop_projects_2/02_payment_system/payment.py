from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self._amount = amount

    def get_amount(self):
        return self._amount

    @abstractmethod
    def pay(self):
        pass


class CardPayment(Payment):
    def pay(self):
        print(f"Paid {self._amount} using a bank card.")


class CashPayment(Payment):
    def pay(self):
        print(f"Paid {self._amount} in cash.")


class OnlinePayment(Payment):
    def pay(self):
        print(f"Paid {self._amount} using online payment.")
