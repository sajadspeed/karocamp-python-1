from __future__ import annotations

import datetime

from reports import Report


class BankAccount:
    def __init__(
        self,
        name: str,
        mojoodi: float,
        reporters: list[Report],
        aghazade: bool = False,
        masdoodi: bool = False,
    ):
        self.name = name
        self.__mojoodi = mojoodi
        self.__reporters = reporters
        self.aghazade = aghazade
        self.masdoodi = masdoodi

    def bardasht(self, mablagh: float) -> bool:
        if self.__validate_bardasht(mablagh):
            self.__mojoodi -= mablagh
            return True

        return False

    def variz(self, mablagh: float) -> bool:
        """Hooora"""
        if self.__validate_variz(mablagh):
            self.__mojoodi += mablagh
            return True

        return False

    def show_mojoodi(self) -> None:
        print(f"{self.name} {self.__mojoodi} Mojoodi darad.")

    def kart_be_kart(self, maghsad: BankAccount, mablagh: float) -> bool:
        if self.bardasht(mablagh):
            if maghsad.variz(mablagh):
                for reporter in self.__reporters:
                    reporter.save(
                        f"KBK {self.name} {mablagh} be {maghsad.name} | {datetime.datetime.now()}"
                    )
                return True
            else:
                self.variz(mablagh)

        return False

    def __validate_variz(self, mablagh: float) -> bool:
        if self.aghazade == False and mablagh >= 200 or self.masdoodi:
            return False

        return True

    def __validate_bardasht(self, mablagh: float) -> bool:
        if mablagh > self.__mojoodi or self.masdoodi:
            return False

        return True

    @staticmethod
    def rial_to_tooman(rial):
        return rial / 10

    def __str__(self):
        return f"{self.name} ({self.__mojoodi})"

    def __add__(self, other):
        return self.__mojoodi + other.__mojoodi


class BlueBank(BankAccount):
    bank_name: str = "Blue Bank"


class TegaratBank(BankAccount):
    bank_name: str = "Tegarat Bank"


class MelatBank(BankAccount):
    bank_name: str = "Melat Bank"
