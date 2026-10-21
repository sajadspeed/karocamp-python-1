from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def save(self, message: str) -> None:
        pass


class ReportTextFile(Report):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, message: str) -> None:
        with open(self.file_path, "a") as file:
            file.write(message + "\n")


class ReportPrint(Report):
    def save(self, message: str) -> None:
        print(message)


class ReportSMS(Report):
    def save(self, message: str) -> None:
        print("SEND SMS: ", message)
