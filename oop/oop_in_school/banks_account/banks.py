import datetime


class BankAccount:
    def __init__(self, name, mojoodi: float, reporters, aghazade=False, masdoodi=False):
        self.name = name
        self.__mojoodi = mojoodi
        self.__reporters = reporters
        self.aghazade = aghazade
        self.masdoodi = masdoodi

    def bardasht(self, mablagh: float):
        if self.__validate_bardasht(mablagh):
            self.__mojoodi -= mablagh
            return True

        return False

    def variz(self, mablagh: float):
        """Hooora"""
        if self.__validate_variz(mablagh):
            self.__mojoodi += mablagh
            return True

        return False

    def show_mojoodi(self):
        print(f"{self.name} {self.__mojoodi} Mojoodi darad.")

    def kart_be_kart(self, maghsad, mablagh: float):
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

    def __validate_variz(self, mablagh: float):
        if self.aghazade == False and mablagh >= 200 or self.masdoodi:
            return False

        return True

    def __validate_bardasht(self, mablagh: float):
        if mablagh > self.__mojoodi or self.masdoodi:
            return False
        return True


class BlueBank(BankAccount):
    bank_name = "Blue Bank"


class TegaratBank(BankAccount):
    bank_name = "Tegarat Bank"


class MelatBank(BankAccount):
    bank_name = "Melat Bank"
