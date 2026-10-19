from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def save(message: str):
        pass


class ReportTextFile(Report):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, message):
        with open(self.file_path, "a") as file:
            file.write(message + "\n")


class ReportPrint(Report):
    def save(self, message):
        print(message)


class ReportSMS(Report):
    def save(self, message):
        print("SEND SMS: ", message)
