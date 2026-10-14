class BankAccount:
    def __init__(self, name, mojoodi: float, aghazade=False):
        self.name = name
        self.__mojoodi = mojoodi
        self.aghazade = aghazade

    def bardasht(self, mablagh: float):
        if self.__validate_tarakonesh(mablagh):
            self.__mojoodi -= mablagh
        else:
            print("Motabar nist.")

    def variz(self, mablagh: float):
        """Hooora"""
        if self.__validate_tarakonesh(mablagh):
            self.__mojoodi += mablagh
        else:
            print("Motabar nist.")

    def show_mojoodi(self):
        print(f"{self.name} {self.__mojoodi} Mojoodi darad.")

    def __validate_tarakonesh(self, mablagh: float):
        if mablagh > self.__mojoodi:
            return False
        if self.aghazade == False and mablagh >= 200:
            return False

        return True


danial_account = BankAccount("Dnial", 1.5, True)

danial_account.show_mojoodi()
danial_account.variz(1.5)
danial_account.show_mojoodi()


sajad_account = BankAccount("Sajad", 6.4)

paria_account = BankAccount("Paria", 1.7)

paria_account.bardasht(1)
paria_account.variz(10)
paria_account.show_mojoodi()

danial_account.bardasht(6)
danial_account.show_mojoodi()

danial_account.__mojoodi -= 6
